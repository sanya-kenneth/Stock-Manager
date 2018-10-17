from flask import Flask
from app.products.views import product
from app.auth.views import auth
from instance.config import app_config



def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    #Register Blueprints
    app.register_blueprint(product, url_prefix='/api/v1' )
    app.register_blueprint(auth,url_prefix='/api/v1')

    return app