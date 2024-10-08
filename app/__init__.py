from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    mongo.init_app(app)

    with app.app_context():
        from .views import routes
        app.register_blueprint(routes.bp)

    return app
