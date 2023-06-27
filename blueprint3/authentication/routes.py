from flask import Blueprint, render_template, redirect, url_for
from .forms import SignupForm
from .models import User
from car_inventory import db

authentication_bp = Blueprint('authentication', __name__)

@authentication_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authentication.login'))
    return render_template('register.html', form=form)

