from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.config import alchemy_uri

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = alchemy_uri()
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    
    CORS(app)

    db.init_app(app)
    db.create_all(app=app)

    from api.memo.blueprints.route import memo
    app.register_blueprint(memo)
    
    return app
