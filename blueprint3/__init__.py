from flask import Blueprint
from flask_login import LoginManager

blueprint3 = Blueprint('blueprint3', __name__)

# Create a LoginManager instance
login_manager = LoginManager()

# Configure Flask-Login
login_manager.init_app(blueprint3)
login_manager.login_view = 'blueprint3.login'
