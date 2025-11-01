from .user import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    company = db.Column(db.String(150))
    location = db.Column(db.String(150))
    description = db.Column(db.Text)
    url = db.Column(db.String(1024))
    embedding = db.Column(db.PickleType)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
