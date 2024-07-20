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

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = read_data()
    task = request.json
    data['tasks'].append(task)
    write_data(data)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    data = read_data()
    return jsonify(data['tasks'])

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = read_data()
    task = next((task for task in data['tasks'] if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    
    task_update = request.json
    task.update(task_update)
    write_data(data)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    data = read_data()
    task_index = next((index for (index, d) in enumerate(data['tasks']) if d['id'] == task_id), None)
    if task_index is None:
        return jsonify({'message': 'Task not found'}), 404
    
    del data['tasks'][task_index]
    write_data(data)
    return jsonify({'message': 'Task deleted'})

@app.route('/messages', methods=['POST'])
def create_message():
    data = read_data()
    message = request.json
    data['messages'].append(message)
    write controls(data)
    return jsonify(message), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    data = read_data()
    return jsonify(data['messages'])

@app.route('/users', methods=['POST'])
def create_user():
    data = read_data()
    user = request.json
    data['users'].append(user)
    write_data(data)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    data = read_data()
    return jsonify(data['users'])

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = read_data()
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user_update = request.json
    user.update(user_update)
    write_data(data)
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = read_data()
    user_index = next((index for (index, d) in enumerate(data['users']) if d['id'] == user_id), None)
    if user_index is None:
        return jsonify({'message': 'User not found'}), 404
    
    del data['users'][user_index]
    write_data(data)
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)