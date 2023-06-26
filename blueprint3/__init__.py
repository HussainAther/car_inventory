from flask import Blueprint
from flask_login import LoginManager

blueprint3 = Blueprint('blueprint3', __name__, template_folder='blueprint3_folder')

# Create a LoginManager instance
login_manager = LoginManager()

# Configure Flask-Login
login_manager.init_app(blueprint3)
login_manager.login_view = 'blueprint3.login'

@blueprint3.route('/login')
def index():
    return render_template('login.html')

@blueprint3.route('/register')
def index():
    return render_template('register.html')