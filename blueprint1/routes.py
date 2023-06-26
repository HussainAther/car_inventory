from flask import Blueprint, render_template

blueprint1 = Blueprint('blueprint1', __name__, template_folder='blueprint1_folder')

@blueprint1.route('/test')
def index():
    return render_template('b1index.html')

