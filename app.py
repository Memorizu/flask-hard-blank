
from flask import Flask
from flask_restx import Api

from config import Config
from create_data import create_db

from setup_db import db
from views.movie import movie_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    create_data(app, db)
    # create_db()


def create_data(app, db):
    with app.app_context():
        db.create_all()
        # create_db()
        # with db.session.begin():
        #     create_db()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':

    app.run(host="localhost", port=10001, debug=True)
