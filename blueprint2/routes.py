from flask import Blueprint, render_template

blueprint2 = Blueprint('blueprint2', __name__, template_folder='blueprint2_folder')

@blueprint2.route('/test')
def index():
    return render_template('b2index.html')

