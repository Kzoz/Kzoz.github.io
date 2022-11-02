from . import db
from flask_login import UserMixin
import datetime


class MyDateTime(db.TypeDecorator):
    impl = db.DateTime
    def process_bind_param(self, value, dialect):
        if type(value) is str:
            x= datetime.datetime.strptime(value, '%Y-%m-%d').date()
            return x
        return value

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))
    date = db.Column(db.Date)
    notes = db.Column(db.String(10000))
    drugs = db.Column(db.String(2000))
    next_appo = db.Column(db.Date)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    familyname = db.Column(db.String(150), nullable=False)
    firstname = db.Column(db.String(150), nullable=False)
    #dob = db.Column(MyDateTime)
    dob = db.Column(db.Date)
    pob = db.Column(db.String(64))
    num = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100))
    emergency = db.Column(db.Integer)
    sex = db.Column(db.String(12))
    bloodtype = db.Column(db.String(12))
    allergy = db.Column(db.String(1000))
    conditions = db.Column(db.String(1000))
    notes = db.Column(db.String(10000))
    consultation = db.relationship('Record')

