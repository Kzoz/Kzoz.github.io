from flask import Flask 

def create_ws_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '77w7wldfwp[i3'

    return app

