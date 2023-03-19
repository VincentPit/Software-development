from flask import Flask, request, jsonify

app = Flask(__name__)

# Create a dictionary to store all groups and their members
groups = {}

# Endpoint to create a new group
@app.route('/groups', methods=['POST'])
def create_group():
    group_name = request.json['group_name']
    owner_id = request.json['owner_id']
    if group_name in groups:
        return jsonify({'error': 'Group already exists'}), 400
    groups[group_name] = {'owner_id': owner_id, 'members': []}
    return jsonify({'group_name': group_name, 'owner_id': owner_id})

# Endpoint to add a new member to an existing group
@app.route('/groups/<group_name>/members', methods=['POST'])
def add_member_to_group(group_name):
    member_id = request.json['member_id']
    if group_name not in groups:
        return jsonify({'error': 'Group not found'}), 404
    if member_id in groups[group_name]['members']:
        return jsonify({'error': 'Member already in group'}), 400
    groups[group_name]['members'].append(member_id)
    return jsonify({'group_name': group_name, 'member_id': member_id})

# Endpoint to retrieve all members of a group
@app.route('/groups/<group_name>/members', methods=['GET'])
def get_group_members(group_name):
    if group_name not in groups:
        return jsonify({'error': 'Group not found'}), 404
    return jsonify({'members': groups[group_name]['members']})

# Endpoint to retrieve all groups for a specific user
@app.route('/groups/user/<user_id>', methods=['GET'])
def get_user_groups(user_id):
    user_groups = []
    for group_name, group_info in groups.items():
        if user_id == group_info['owner_id'] or user_id in group_info['members']:
            user_groups.append(group_name)
    return jsonify({'groups': user_groups})


"""# Dummy data for chat groups, group owners, group members, and chat history
chat_groups = [
    {
        'id': 1,
        'name': 'Group 1',
        'owner': 'John',
        'members': ['Mary', 'Peter'],
        'chat_history': [
            {'sender': 'John', 'message': 'Hello Mary!'},
            {'sender': 'Mary', 'message': 'Hi John, how are you?'}
        ]
    },
    {
        'id': 2,
        'name': 'Group 2',
        'owner': 'Mary',
        'members': ['Peter', 'Sarah'],
        'chat_history': [
            {'sender': 'Mary', 'message': 'Hi everyone!'},
            {'sender': 'Peter', 'message': 'Hey Mary, what\'s up?'}
        ]
    }
]
"""
# API endpoint to get all chat groups
@app.route('/chat_groups', methods=['GET'])
def get_chat_groups():
    return jsonify({'chat_groups': chat_groups})

# API endpoint to get a specific chat group by ID
@app.route('/chat_groups/<int:group_id>', methods=['GET'])
def get_chat_group(group_id):
    group = [group for group in chat_groups if group['id'] == group_id]
    if len(group) == 0:
        return jsonify({'error': 'Chat group not found'}), 404
    return jsonify({'chat_group': group[0]})

# API endpoint to create a new chat group
@app.route('/chat_groups', methods=['POST'])
def create_chat_group():
    if not request.json or not 'name' in request.json or not 'owner' in request.json:
        return jsonify({'error': 'Name and owner are required fields'}), 400
    group = {
        'id': chat_groups[-1]['id'] + 1,
        'name': request.json['name'],
        'owner': request.json['owner'],
        'members': [],
        'chat_history': []
    }
    chat_groups.append(group)
    return jsonify({'chat_group': group}), 201

# API endpoint to add a member to a chat group
@app.route('/chat_groups/<int:group_id>/add_member', methods=['PUT'])
def add_member(group_id):
    group = [group for group in chat_groups if group['id'] == group_id]
    if len(group) == 0:
        return jsonify({'error': 'Chat group not found'}), 404
    if not request.json or not 'member' in request.json:
        return jsonify({'error': 'Member field is required'}), 400
    if request.json['member'] in group[0]['members']:
        return jsonify({'error': 'Member already exists in the group'}), 409
    group[0]['members'].append(request.json['member'])
    return jsonify({'chat_group': group[0]})

# API endpoint to send a message to a chat group
@app.route('/chat_groups/<int:group_id>/send_message', methods=['POST'])
def send_message(group_id):
    group = [group for group in chat_groups if group['id'] == group_id]
    if len(group) == 0:
        return jsonify({'error': 'Chat group not found'}), 404
    if not request.json or not 'sender' in request.json or not 'message' in request.json:
        return jsonify

if __name__ == '__main__':
    app.run()


"""
This API has four endpoints:

POST /groups - creates a new group with the specified group name and owner ID.
POST /groups/<group_name>/members - adds a new member to the specified group.
GET /groups/<group_name>/members - retrieves all members of the specified group.
GET /groups/user/<user_id> - retrieves all groups for the specified user (as an owner or member).
To test this API, you can use a tool like curl or Postman to send requests to the API.
{
    "group_name": "test_group",
    "owner_id": 123
}

For example, to create a new group called "test_group" with owner ID 123, you can send a POST request to http://localhost:5000/groups with a JSON payload containing the group name and owner ID, like this:
{
    "member_id": 456
}

"""