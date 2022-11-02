from cgi import print_arguments
import json
import datetime
from .models import Patient, Record
from flask import Blueprint, render_template, request,redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from . import db


views = Blueprint('views', __name__)

superUsers = ['moussa@gmail.com']
patient_id = 1

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/newpatient', methods=['GET','POST'])
@login_required
def newpatient():
    allPatients = Patient.query.all()
    if current_user.email not in superUsers:
        flash('Vous n\'avez pas accés à cette fonctionnalité.',category='error')
        return redirect(url_for('views.home'))
    if request.method=='POST':
        familyname = request.form.get('familyName')
        surname = request.form.get('surname')
        birthday = datetime.datetime.strptime(
                     request.form['birthday'],
                     '%Y-%m-%d').date()
        birthplace = request.form.get('birthplace')
        num = request.form.get('num')
        email = request.form.get('email')
        emergency = request.form.get('emergency')
        bloodtype = request.form.get('bloodtype')
        sex = request.form.get('sex')
        allergy = request.form.get('allergy')
        sickness = request.form.get('sickness')
        memo = request.form.get('memo')
       
        new_patient = Patient(familyname = familyname, firstname=surname, dob=birthday,
        pob=birthplace, num=num, email=email, emergency=emergency, sex=sex, bloodtype=bloodtype,
        allergy=allergy, conditions=sickness, notes=memo)


   
        db.session.add(new_patient)
        db.session.commit()
        latestPatient = allPatients[-1].id
        
        flash('Un nouveau patient a été ajouté.', category='success')
        return redirect(url_for('views.listOfPatients',  patientId=latestPatient))
    return render_template('newpatient.html', methods=['GET','POST'], user=current_user)

@views.route('/patients/<int:patientId>', methods=['GET','POST'])
@login_required
def listOfPatients(patientId):
    patient = Patient.query.all()
    global patient_id
    patient_id = patientId
    
    current_patient=Patient.query.get_or_404(patientId)
    if request.method == 'POST':
        db.session.delete(current_patient)
        db.session.commit()
        return redirect(url_for('views.listOfPatients',  patientId=0))
    #current_patient = Patient.query.get_or_404(patient_id)
    return render_template('patients_list.html', user=current_user,patient=patient, current_patient=current_patient)



@views.route('/details/<int:patientId>', methods=['GET','POST'])
@login_required
def patientDetails(patientId):
    
    global patient_id
    patientId = patient_id
    
    currentPatient = Patient.query.get_or_404(patientId)
    #patient = Patient.query.all()

    if request.method=='POST':
        date = datetime.datetime.strptime(
                     request.form['notedate'],
                     '%Y-%m-%d').date()
        notes = request.form.get('note')
        drugs = request.form.get('drugs')
        next_appo = datetime.datetime.strptime(
                     request.form['nextappo'],
                     '%Y-%m-%d').date()

        new_consultation = Record(patient_id=patientId, date=date, notes=notes, drugs=drugs, next_appo=next_appo)
        db.session.add(new_consultation)
        db.session.commit()
        return redirect(url_for('views.patientDetails', patientId=currentPatient.id))
    return render_template("/patient_detail.html", user=current_user,  currentPatient=currentPatient)



@views.route('/update/<int:patientId>', methods=['GET','POST'])
@login_required
def updateInfo(patientId):

    if current_user.email not in superUsers:
        flash('Vous n\'avez pas accés à cette fonctionnalité.',category='error')
        return redirect(url_for('views.listOfPatients',  patientId=0))
    global patient_id
    patientId = patient_id
    currentPatient = Patient.query.get_or_404(patientId)

    if request.method=='POST':
        currentPatient.familyname = request.form.get('familyName')
        currentPatient.firstname = request.form.get('surname')
        currentPatient.dob = datetime.datetime.strptime(
                     request.form['birthday'],
                     '%Y-%m-%d').date()
        currentPatient.pob = request.form.get('birthplace')
        currentPatient.num = request.form.get('num')
        currentPatient.email = request.form.get('email')
        currentPatient.emergency = request.form.get('emergency')
        currentPatient.sex = request.form.get('sex')
        currentPatient.bloodtype = request.form.get('bloodtype')
        currentPatient.allergy = request.form.get('allergy')
        currentPatient.notes = request.form.get('sickness')
        currentPatient.conditions = request.form.get('memo')

        db.session.add(currentPatient)
        db.session.commit()
        flash('Les informations du patient ont été modifié.',category='success')
        return redirect(url_for('views.listOfPatients', patientId=currentPatient.id))

    return render_template("update_info.html", methods=['GET','POST'],user=current_user,currentPatient=currentPatient)



@views.route('/delete-history', methods=['POST'])
def deleteHistory():
    global patient_id
    print('Here it is',patient_id)
    history = json.loads(request.data)
    historyId = history['historyId']
    history = Record.query.get(historyId)
    print(history)
    if history:
        if history.patient_id == patient_id:
            db.session.delete(history)
            db.session.commit()
    return jsonify({})