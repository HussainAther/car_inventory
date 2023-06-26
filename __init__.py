import logging # For error handling

from flask import Flask
from .blueprint1.routes import blueprint1
from .blueprint2.routes import blueprint2
from .blueprint3.routes import blueprint3

from .blueprint3.models import User
from .config import config
from .models import db

from flask_login import current_user
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
    app.register_blueprint(blueprint3, url_prefix='/blueprint3')

    logging.info("Blueprints registered successfully")

    # Initialize database
    db.init_app(app)

    # Load the user database
    @app.before_first_request
    def load_user_database():
        with app.app_context():
            db.create_all()
            if not User.query.filter_by(username='admin').first():
                admin = User(username='admin')
                admin.set_password('password')
                admin.save()

    return app

