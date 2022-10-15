from flask import Flask 


def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '!@^GB3lopiurt42G^*^GJ342fsGhgfju63467'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
    