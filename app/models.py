from . import db

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    task_type = db.Column(db.Enum('call', 'meeting', 'video call', name='task_type_enum'), nullable=False)
    time = db.Column(db.Time, nullable=True)
    contact_person = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    note = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('open', 'closed', name='status_enum'), default='open')

    def to_dict(self):
        return {
            'id': self.id,
            'entity_name': self.entity_name,
            'date': self.date.isoformat() if self.date else None,
            'task_type': self.task_type,
            'time': self.time.isoformat() if self.time else None,
            'contact_person': self.contact_person,
            'phone_number': self.phone_number,
            'note': self.note,
            'status': self.status
        }
