from flask import Flask
from app.products.views import product
from app.products import views
from app.auth import views
from app.sales import views
from app.auth.views import auths
from app.sales.views import sale_bp
from instance.config import app_config
from app.auth.database import Database
# import sys
# import os.path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # ctx = app.app_context()
    # ctx.push()
    
    #Register Blueprints
    app.register_blueprint(product, url_prefix='/api/v1' )
    app.register_blueprint(auths,url_prefix='/api/v1')
    app.register_blueprint(sale_bp,url_prefix='/api/v1')
    return app
    