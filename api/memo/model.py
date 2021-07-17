import json
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

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime):
            return str(z.strftime("%m/%d %H:%M"))
        else:
            return super().default(z)

def get_memos():
    memos = Memo.query.all()
    serialized_data = []

    for memo in memos:
        serialized_data.append(memo.serialize)

    json_serialized_data = json.dumps(serialized_data, cls=DateTimeEncoder)
    contents_list = []
    for data in json.loads(json_serialized_data):
        content = {}
        content["date"] = data["created_at"]
        content["contents"] = data["content"]
        contents_list.append(content)

    return contents_list



