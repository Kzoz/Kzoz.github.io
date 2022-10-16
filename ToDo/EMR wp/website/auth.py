from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/accueil')
def login():
    return render_template('accueil.html')