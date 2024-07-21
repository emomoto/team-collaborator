import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = os.getenv('DATA_PATH', 'team_collaborator.json')

def read_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": [], "messages": [], "users": []}
    except json.JSONDecodeError:
        return {"tasks": [], "messages": [], "users": []}  # Assuming a corrupted file should behave like an empty one

def write_data(data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        return jsonify({"error": "Failed to write data", "message": str(e)}), 500

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json:
        return jsonify({"error": "Bad request", "message": "Request body is not JSON"}), 400
    data = read_idx_data()
    task = request.json
    # Validate id exists in task
    if 'id' not in task:
        return jsonify({"error": "Bad request", "message": "Task ID is missing"}), 400
    data['tasks'].append(task)
    resp = write_data(data)
    if resp: 
        return resp
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    data = read_data()
    return jsonify(data['tasks'])

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not request.json:
        return jsonify({"error": "Bad request", "message": "Request body is not JSON"}), 400
    data = read_data()
    task = next((task for task in data['tasks'] if task.get('id') == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    
    task_update = request.json
    task.update(task_update)
    resp = write_state(data)
    if resp:
        return resp
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    data = read_data()
    task_index = next((index for (index, d) in enumerate(data['tasks']) if d.get('id') == task_id), None)
    if task_index is None:
        return jsonify({'message': 'Task not found'}), 404
    
    del data['tasks'][task_index]
    resp = write_data(data)
    if resp:
        return resp
    return jsonify({'message': 'Task deleted'})

@app.route('/messages', methods=['POST'])
def create_message():
    if not request.json:
        return jsonify({"error": "Bad request", "message": "Request body is not JSON"}), 400
    data = read_data()
    message = request.json
    data['messages'].append(message)
    resp = write_data(data)
    if resp:
        return resp
    return jsonify(message), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    data = read_data()
    return jsonify(data['messages'])

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({"error": "Bad request", "message": "Request body is not JSON"}), 400
    data = read_data()
    user = request.json
    if 'id' not in user:
        return jsonify({"error": "Bad request", "message": "User ID is missing"}), 400
    data['users'].append(user)
    resp = write_data(data)
    if resp:
        return resp
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    data = read_data()
    return jsonify(data['users'])

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json:
        return jsonify({"error": "Bad request", "message": "Request body is not JSON"}), 400
    data = read_data()
    user = next((user for user in data['users'] if user.get('id') == user_id), None)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user_update = request.json
    user.update(user.update)
    resp = write_data(data)
    if resp:
        return resp
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = read_data()
    user_index = next((index for (index, d) in enumerate(data['users']) if d.get('id') == user_id), None)
    if user_index is None:
        return jsonify({'message': 'User not found'}), 404
    
    del data['users'][user_index]
    resp = write_data(data)
    if resp:
        return resp
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)