import logging # For error handling

from flask import Flask
from .blueprint1.routes import blueprint1
from .blueprint2.routes import blueprint2
from .config import config
from .routes import main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Enable debug mode
    app.debug = True
    
    # # Register blueprints
    # app.register_blueprint(blueprint1)
    # app.register_blueprint(blueprint2)
    app.register_blueprint(main_blueprint)

    app.register_blueprint(blueprint1, url_prefix='/blueprint1')
    app.register_blueprint(blueprint2, url_prefix='/blueprint2')

    logging.info("Blueprints registered successfully")

    return app

