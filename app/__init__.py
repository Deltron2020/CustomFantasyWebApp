from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        USERNAME=None,
        PASSWORD=None,
        DB_SERVER_NAME=None,
        DATABASE=None,
        SECRET_KEY=None
    )

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
