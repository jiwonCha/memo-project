from datetime import datetime
import pytest
import api.config as config

from api import create_app, db
from api.memo.model import Memo

TEST_CONFIG = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": config.test_db_uri()}


@pytest.fixture(scope="session")
def app():
    app = create_app(TEST_CONFIG)

    with app.app_context():
        db.create_all()
        memo = Memo(id=1, content="Frist Memos", created_at=datetime.now())

        db.session.add(memo)
        db.session.commit()

    return app.test_client()


def test_get_memos(app):
    res = app.get("/memo-service/memos")
    assert res.status_code == 200
    assert res.content_type == "text/html; charset=utf-8"


def test_post_memo(app):
    res = app.post("/memo-service/memos", data=dict(content="This is Memo"))
    assert res.status_code == 200
