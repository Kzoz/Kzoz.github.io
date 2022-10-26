from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/newpatient')
def newpatient():
    return render_template('newpatient.html', methods=['GET','POST'])

@views.route('/patients')
def listOfPatients():
    return render_template('patients_list.html')

@views.route('/details')
def patientDetails():
    return render_template("/patient_detail.html")

@views.route('/update')
def updateInfo():
    return render_template("update_info.html", methods=['GET','POST'])