from flask import Flask
import json

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config['SECRET_KEY'] = 'dfdfzfedsfsf'
    app.config.update(
        USERNAME=None,
        PASSWORD=None,
        DB_SERVER_NAME=None,
        DATABASE=None
    )

    app.config.from_file(r'C:\Users\tyler\Projects\CustomFantasyWebApp\instance\credentials.json', load=json.load)

    from .views import views
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/test')
    #app.register_blueprint(auth, url_prefix='/auth')

    return app
