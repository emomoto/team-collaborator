from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

task_list = []
message_list = []
user_list = []

DB_CONNECTION_URL = os.getenv('DATABASE_URL')

@app.route('/tasks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task_operations():
    if request.method == 'POST':
        new_task = request.json
        if not new_task.get('id'):
            return jsonify({'error': 'Missing task id'}), 400
        task_list.append(new_task)
        return jsonify(new_task), 201

    elif request.method == 'GET':
        return jsonify(task_list), 200

    elif request.method == 'PUT':
        task_update = request.json
        if not task_update.get('id'):
            return jsonify({'error': 'Missing task id'}), 400
        for task in task_list:
            if task['id'] == task_update['id']:
                task.update(task_update)
                return jsonify(task), 200
        return jsonify({'error': 'Task not found'}), 404

    elif request.method == 'DELETE':
        target_task_id = request.args.get('id')
        if not target_task_id:
            return jsonify({'error': 'Missing task id'}), 400
        for task in task_list:
            if task['id'] == target_task_id:
                task_list.remove(task)
                return jsonify({}), 204
        return jsonify({'error': 'Task not found'}), 404

@app.route('/messages', methods=['GET', 'POST', 'DELETE'])
def message_operations():
    if request.method == 'POST':
        new_message = request.json
        if not new_message.get('id'):
            return jsonify({'error': 'Missing message id'}), 400
        message_list.append(new_message)
        return jsonify(new_message), 201

    elif request.method == 'GET':
        return jsonify(message_list), 200

    elif request.method == 'DELETE':
        target_message_id = request.args.get('id')
        if not target_message_id:
            return jsonify({'error': 'Missing message id'}), 400
        for message in message_list:
            if message['id'] == target_message_id:
                message_list.remove(message)
                return jsonify({}), 204
        return jsonify({'error': 'Message not found'}), 404

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_operations():
    if request.method == 'POST':
        new_user = request.json
        if not new_user.get('id'):
            return jsonify({'error': 'Missing user id'}), 400
        user_list.append(new_user)
        return jsonify(new_user), 201

    elif request.method == 'GET':
        return jsonify(user_list), 200

    elif request.method == 'PUT':
        user_update = request.json
        if not user_update.get('id'):
            return jsonify({'error': 'Missing user id'}), 400
        for user in user_list:
            if user['id'] == user_update['id']:
                user.update(user_update)
                return jsonify(user), 200
        return jsonify({'error': 'User not found'}), 404

    elif request.method == 'DELETE':
        target_user_id = request.args.get('id')
        if not target_user_id:
            return jsonify({'error': 'Missing user id'}), 400
        for user in user_list:
            if user['id'] == target_user_id:
                user_list.remove(user)
                return jsonify({}), 204
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)