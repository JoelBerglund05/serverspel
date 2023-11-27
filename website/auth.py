from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .sign_in_up import Hash
from . import db   # Means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
#from Crypto.Cipher import AES
import sys 

auth = Blueprint('auth', __name__)

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
    else:
        return render_template('login.html', user=current_user)
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        password = [request.form.get('password1'), request.form.get('password2')]
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()
        if user:
            flash('username already exists.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password[0] != password[1]:
            flash('Passwords do not match.', category='error')
        elif len(password[0]) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(username=username, password=Hash.get_hash(password[0], 15))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return render_template('sign_up.html', user=current_user)

    return render_template('sign_up.html', user=current_user)

