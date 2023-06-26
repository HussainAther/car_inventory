from flask import Blueprint, render_template

blueprint2 = Blueprint('blueprint2', __name__)

@blueprint2.route('/')
def index():
    return render_template('blueprint2/index.html')

