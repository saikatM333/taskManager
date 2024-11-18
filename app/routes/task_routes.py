from flask import Blueprint, request, jsonify
from ..services.task_service import TaskService

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = TaskService.create_task(data)
    return jsonify({'message': 'Task created', 'task': new_task.id}), 201

@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    updated_task = TaskService.update_task(task_id, data)
    if updated_task:
        return jsonify({'message': 'Task updated', 'task': updated_task.id})
    return jsonify({'error': 'Task not found'}), 404

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if TaskService.delete_task(task_id):
        return jsonify({'message': 'Task deleted'})
    return jsonify({'error': 'Task not found'}), 404
