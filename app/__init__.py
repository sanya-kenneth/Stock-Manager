from flask import Flask
from app.products.views import product

app = Flask(__name__)

app.register_blueprint(product, url_prefix='/api/v1' )