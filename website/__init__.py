from flask import Flask
from config import SECRET_KEY


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hi'

    from .views import views 
    
    app.register_blueprint(views, url_prefix='/')


    return app