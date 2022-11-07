from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Patient, Record
from werkzeug.security import generate_password_hash, check_password_hash
from . import  db
from flask_login import login_required, login_user, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Bienvenue!', category=';success')
                login_user(user, remember=True)#the currently logged in user
                return redirect(url_for('views.home'))
            else:
                flash('Mot de passe incorrect. Veuillez essayer à nouveau', category='error')
        else:
            flash("Ce compte n\'existe pas.", category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        name = name.capitalize()
        password = request.form.get("password")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Cet compte existe déjà.',category='error')
        elif len(password) < 8 or len(password) > 20:
            flash('Votre mot de passe doit contenir au minimum 8 caractères (max 20).', category='error')
        elif len(password2) < 8 or len(password2) > 20:
            flash('Votre mot de passe doit contenir au minimum 8 caractères (max 20).', category='error')
        elif password != password2:
            flash('Les mots de passe saisis ne sont pas identiques.',category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Votre compte a été créé!', category='success')
            return redirect(url_for('auth.login'))


    return render_template("sign_up.html", user=None)