from flask import Flask, jsonify, request

app = Flask(__name__)



# Get a list of all groups
@app.route("/groups")
def get_groups():

    # wait for extraction from Data Base
    return jsonify(groups)

# Get information about a specific group
@app.route("/groups/<group_name>")
def get_group(group_name):
    if group_name in groups:
        return jsonify(groups[group_name])
    else:
        return jsonify({"error": "Group not found"})

# Create a new group
@app.route("/groups", methods=["POST"])
def create_group():
    name = request.json["name"]
    owner = request.json["owner"]
    members = request.json["members"]
    history = []
    media = []
    groups[name] = {"name": name, "owner": owner, "members": members, "history": history, "media": media}
    return jsonify({"message": "Group created successfully"})

# Add a message to a group's chat history
@app.route("/groups/<group_name>/messages", methods=["POST"])
def add_message(group_name):
    if group_name in groups:
        sender = request.json["sender"]
        message = request.json["message"]
        time = request.json["time"]
        groups[group_name]["history"].append({"sender": sender, "message": message, "time": time})
        return jsonify({"message": "Message added to group history"})
    else:
        return jsonify({"error": "Group not found"})

# Upload media to a group
@app.route("/groups/<group_name>/media", methods=["POST"])
def upload_media(group_name):
    if group_name in groups:
        media_type = request.json["type"]
        data = request.json["data"]
        groups[group_name]["media"].append({"type": media_type, "data": data})
        return jsonify({"message": "Media uploaded successfully"})
    else:
        return jsonify({"error": "Group not found"})


