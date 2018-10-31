from flask import Flask

from web.views import webs


def create_app():

    app = Flask(__name__)
    
    # app.secret_key = 'some_secret'
    # register blueprints
    app.register_blueprint(webs)

    return app

