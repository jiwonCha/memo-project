import logging
import json
from datetime import datetime
from flask import request, Blueprint, render_template, make_response, redirect
from flask.json import jsonify
from flask_restx import Namespace, Resource, Api, fields

from api import db
from api.memo.model import Memo, get_memos

memo = Blueprint("memo", __name__)
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

resource_fields = api_extension.model('Memo Resource', {
    'content': fields.String
})

@namespace.route("")
class Memos(Resource):
    @namespace.produces(["text/html"])
    def get(self):
        """Get Memo Lists"""
        logger.debug("Get Memo Lists")

        contents_list = get_memos()

        return make_response(render_template("view.html", result=contents_list), 200)

    @namespace.doc(body=resource_fields)
    @namespace.produces(["text/html"])
    def post(self):
        """Create Memo Instance"""
        logger.debug("Post Memo")

        data = request.form["content"]

        new_memo = Memo(content=data)
        db.session.add(new_memo)
        db.session.commit()

        contents_list = get_memos()

        return make_response(render_template("view.html", result=contents_list), 200)
