import logging
import json
from datetime import datetime
from flask import request, Blueprint, render_template, make_response, redirect
from flask.json import jsonify
from flask_restx import Namespace, Resource, Api

from api import db
from api.memo.model import Memo

memo = Blueprint("memo", __name__, url_prefix="memo-service")
logger = logging.getLogger(name="route")

api_extension = Api(
    memo,
    title="Memo Application",
    version="1.0",
    description="Memo Application API Documentation",
    doc="/doc",
)

namespace = Namespace("memos", "Memo related endpoints")
api_extension.add_namespace(namespace)

# hello_world_model = namespace.model('HelloWorld', {
#     'message': fields.String(
#         readonly=True,
#         description='Hello world message'
#     )
# })

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime):
            return (str(z.strftime("%m/%d %H:%M")))
        else:
            return super().default(z)


@namespace.route("")
class Memos(Resource):
    def get(self):
        """Get Memo Lists"""
        logger.debug("Get Memo Lists")
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

        return make_response(render_template("view.html", result=contents_list), 200)

    def post(self):
        """Create Memo Instance"""
        data = request.form['content']

        new_memo = Memo(content=data)
        db.session.add(new_memo)
        db.session.commit()

        return redirect("/memos")
