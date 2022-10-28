from flask import Blueprint, render_template, request,redirect, url_for, flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

superUsers = ["moussa@gmail.com"]

@views.route('/')
@login_required
def home():

    return render_template('home.html', user=current_user)

@views.route('/newpatient')
@login_required
def newpatient():
    if current_user.email not in superUsers:
        flash('Vous n\'avez pas accés à cette fonctionnalité.',category='error')
        return redirect(url_for('views.listOfPatients'))
    return render_template('newpatient.html', methods=['GET','POST'])

@views.route('/patients')
@login_required
def listOfPatients():
    return render_template('patients_list.html')

@views.route('/details')
@login_required
def patientDetails():
    return render_template("/patient_detail.html")

@views.route('/update')
@login_required
def updateInfo():
    if current_user.email not in superUsers:
        flash('Vous n\'avez pas accés à cette fonctionnalité.',category='error')
        return redirect(url_for('views.listOfPatients'))
    return render_template("update_info.html", methods=['GET','POST'])