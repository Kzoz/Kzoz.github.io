from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 
DB_NAME = 'database.db'

def create_ws_app():
    app = Flask(__name__)
    #app.secret_key = 'svbjn67dcs'
    app.config['SECRET KEY'] = '77w7wldfwpi3'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

