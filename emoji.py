import emoji

# Replace emoji codes with actual emoji characters in a message
def replace_emojis(message):
    return emoji.emojize(message, use_aliases=True)

# Add a message to a group's chat history with support for emojis
@app.route("/groups/<group_name>/messages", methods=["POST"])
def add_message(group_name):
    if group_name in groups:
        sender = request.json["sender"]
        message = request.json
