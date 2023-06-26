from flask import Flask
from .blueprint1.routes import blueprint1
from .blueprint2.routes import blueprint2

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint1, url_prefix='/blueprint1')
    app.register_blueprint(blueprint2, url_prefix='/blueprint2')

    return app

