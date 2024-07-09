from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

task_list = []
message_list = []
user_list = []

DB_CONNECTION_URL = os.getenv('DATABASE_URL')

# Helper Functions
def find_task(task_id):
    for task in task_list:
        if task['id'] == task_id:
            return task
    return None

def find_message(message_id):
    for message in message_list:
        if message['id'] == message_id:
            return message
    return None

def find_user(user_id):
    for user in user_list:
        if user['id'] == user_id:
            return user
    return None

# Route Functions
@app.route('/tasks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task_operations():
    try:
        if request.method == 'POST':
            return create_task()
        elif request.method == 'GET':
            return get_tasks()
        elif request.method == 'PUT':
            return update_task()
        elif request.method == 'DELETE':
            return delete_task()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_task():
    new_task = request.get_json(force=True)
    if not new_task.get('id'):
        return jsonify({'error': 'Missing task id'}), 400
    task_list.append(new_task)
    return jsonify(new_task), 201

def get_tasks():
    return jsonify(task_list), 200

def update_task():
    task_update = request.get_json(force=True)
    if not task_update.get('id'):
        return jsonify({'error': 'Missing task id'}), 400
    task = find_task(task_update['id'])
    if task:
        task.update(task_update)
        return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

def delete_task():
    target_task_id = request.args.get('id')
    if not target_task_id:
        return jsonify({'error': 'Missing task id'}), 400
    task = find_task(target_task_id)
    if task:
        task_list.remove(task)
        return jsonify({}), 204
    return jsonify({'error': 'Task not found'}), 404

@app.route('/messages', methods=['GET', 'POST', 'DELETE'])
def message_operations():
    try:
        if request.method == 'POST':
            return create_message()
        elif request.method == 'GET':
            return get_messages()
        elif request.method == 'DELETE':
            return delete_message()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_message():
    new_message = request.get_json(force=True)
    if not new_message.get('id'):
        return jsonify({'error': 'Missing message id'}), 400
    message_list.append(new_message)
    return jsonify(new_message), 201

def get_messages():
    return jsonify(message_list), 200

def delete_message():
    target_message_id = request.args.get('id')
    if not target_message_id:
        return jsonify({'error': 'Missing message id'}), 400
    message = find_message(target_message_id)
    if message:
        message_list.remove(message)
        return jsonify({}), 204
    return jsonify({'error': 'Message not found'}), 404

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_operations():
    try:
        if request.method == 'POST':
            return create_user()
        elif request.method == 'GET':
            return get_users()
        elif request.method == 'PUT':
            return update_user()
        elif request.method == 'DELETE':
            return delete_user()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_user():
    new_user = request.get_json(force=True)
    if not new_user.get('id'):
        return jsonify({'error': 'Missing user id'}), 400
    user_list.append(new_user)
    return jsonify(new_user), 201

def get_users():
    return jsonify(user_list), 200

def update_user():
    user_update = request.get_json(force=True)
    if not user_update.get('id'):
        return jsonify({'error': 'Missing user id'}), 400
    user = find_user(user_update['id'])
    if user:
        user.update(user_update)
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

def delete_user():
    target_user_id = request.args.get('id')
    if not target_user_id:
        return jsonify({'error': 'Missing user id'}), 400
    user = find_user(target_user_id)
    if user:
        user_list.remove(user)
        return jsonify({}), 204
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)