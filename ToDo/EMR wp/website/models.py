from . import db
from flask_login import UserMixin

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    notes = db.Column(db.String(10000))
    drugs = db.Column(db.String(2000))
    nextappo = db.Column(db.String)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))