from config import Config
from flask import Flask
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.before_first_request
    def create_user():
        db.create_all()
        db.session.commit()

    return app
