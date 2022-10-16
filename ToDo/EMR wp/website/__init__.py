from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_ws_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '77w7wldfwp[i3'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

