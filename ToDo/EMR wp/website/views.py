import imp
from pydoc import render_doc
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/newpatient')
def newpatient():
    return render_template('newpatient.html')

@views.route('/patients')
def listOfPatients():
    return render_template('patients_list.html')

@views.route('/details')
def patientDetails():
    return render_template("/patient_detail.html")