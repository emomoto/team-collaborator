from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

tasks = []
messages = []
users = []

DATABASE_URL = os.getenv('DATABASE_URL')

@app.route('/tasks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_tasks():
    if request.method == 'POST':
        task = request.json
        if not task.get('id'):
            return jsonify({'error': 'Missing task id'}), 400
        tasks.append(task)
        return jsonify(task), 201

    elif request.method == 'GET':
        return jsonify(tasks), 200

    elif request.method == 'PUT':
        updated_task = request.json
        if not updated_task.get('id'):
            return jsonify({'error': 'Missing task id'}), 400
        for task in tasks:
            if task['id'] == updated_task['id']:
                task.update(updated_task)
                return jsonify(task), 200
        return jsonify({'error': 'Task not found'}), 404

    elif request.method == 'DELETE':
        task_id = request.args.get('id')
        if not task_id:
            return jsonify({'error': 'Missing task id'}), 400
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                return jsonify({}), 204
        return jsonify({'error': 'Task not found'}), 404

@app.route('/messages', methods=['GET', 'POST', 'DELETE'])
def manage_messages():
    if request.method == 'POST':
        message = request.json
        if not message.get('id'):
            return jsonify({'error': 'Missing message id'}), 400
        messages.append(message)
        return jsonify(message), 201

    elif request.method == 'GET':
        return jsonify(messages), 200

    elif request.method == 'DELETE':
        message_id = request.args.get('id')
        if not message_id:
            return jsonify({'error': 'Missing message id'}), 400
        for message in messages:
            if message['id'] == message_id:
                messages.remove(message)
                return jsonify({}), 204
        return jsonify({'error': 'Message not found'}), 404

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_users():
    if request.method == 'POST':
        user = request.json
        if not user.get('id'):
            return jsonify({'error': 'Missing user id'}), 400
        users.append(user)
        return jsonify(user), 201

    elif request.method == 'GET':
        return jsonify(users), 200

    elif request.method == 'PUT':
        updated_user = request.json
        if not updated_user.get('id'):
            return jsonify({'error': 'Missing user id'}), 400
        for user in users:
            if user['id'] == updated_user['id']:
                user.update(updated_user)
                return jsonify(user), 200
        return jsonify({'error': 'User not found'}), 404

    elif request.method == 'DELETE':
        user_id = request.args.get('id')
        if not user_id:
            return jsonify({'error': 'Missing user id'}), 400
        for user in users:
            if user['id'] == user_id:
                users.remove(user)
                return jsonify({}), 204
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)