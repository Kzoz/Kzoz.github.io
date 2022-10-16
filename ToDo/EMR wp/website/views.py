import imp
from pydoc import render_doc
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('accueil.html')