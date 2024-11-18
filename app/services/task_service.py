from datetime import datetime
from ..models import db, Task

class TaskService:
    @staticmethod
    def create_task(data):
        new_task = Task(
            entity_name=data['entity_name'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            task_type=data['task_type'],
            time=datetime.strptime(data['time'], '%H:%M').time() if 'time' in data else None,
            contact_person=data['contact_person'],
            phone_number=data['phone_number'],
            note=data.get('note', ''),
            status='open'
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    @staticmethod
    def get_all_tasks(filters=None):
        query = Task.query
        if filters:
            # Apply filtering logic
            pass
        return query.all()

    @staticmethod
    def update_task(task_id, data):
        task = Task.query.get(task_id)
        if task:
            for key, value in data.items():
                setattr(task, key, value)
            db.session.commit()
            return task
        return None

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False
