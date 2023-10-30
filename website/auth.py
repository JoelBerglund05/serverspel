from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .sign_in_up import Hash
from . import db   # Means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
#from Crypto.Cipher import AES
import sys 

auth = Blueprint('auth', __name__)
key_crypt = b"\xd1=\x13l\xfa\xef{\xa7\x00\x87L\xd1\xc5\xb2Il\x88\x0e\x89\xf8\x0f\xbc\xca\xe8\xdb\x81\xdao|\xedZ'"


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if Hash.check_hash(password, user.password):
                login_user(user, remember=True)
                return render_template('login.html', user=current_user)
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('username does not exist.', category='error')

    return print("sad):")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('username already exists.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(username=username, password=Hash.get_hash(password, 15))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return print("successfully signed up")

    return print("sad):")