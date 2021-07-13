
from api import db,create_app

if __name__ == "__main__":
    db.create_all(app=create_app())
    create_app().run(debug=True, host='0.0.0.0',port=5000, use_reloader=True)