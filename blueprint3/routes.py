from flask import render_template, redirect, url_for, Blueprint, render_template
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from .models import User

# blueprint3 = Blueprint('blueprint3', __name__)
blueprint3 = Blueprint('blueprint3', __name__, template_folder='blueprint3_folder')

@blueprint3.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        user.save()
        return redirect(url_for('blueprint3.login'))
    return render_template('register.html', form=form)

@blueprint3.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('blueprint3.index'))
    return render_template('login.html', form=form)

@blueprint3.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blueprint3.index'))

