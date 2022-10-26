from crypt import methods
from curses import flash
from operator import methodcaller
import re
from unicodedata import category
from webbrowser import get
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('home.html')

@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if len(password) < 8 or len(password) > 20:
            flash('Le mot de passe doit être entre 8 et 20 lettres', category='error')
        elif len(password2) < 8 or len(password2) > 20:
            flash('Le mot de passe doit être entre 8 et 20 lettres', category='error')
        else:
            flash('Votre compte a été créé!', category='success')
    return render_template("sign_up.html")