from api import db
from datetime import datetime


class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at,
        }
