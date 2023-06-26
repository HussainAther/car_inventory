from flask import Blueprint, render_template

blueprint1 = Blueprint('blueprint1', __name__)

@blueprint1.route('/')
def index():
    return render_template('blueprint1/index.html')

