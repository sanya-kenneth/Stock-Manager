from flask import Blueprint,request,jsonify,json,make_response
from .models import Product
from ..auth.utility import admin_required,login_admin_required
from app.auth.views import admin_db,user_db




# create product blueprint
# blueprint will handle all product routes for the app
product = Blueprint('product',__name__)

product_db = [] #List will hold all products created in the app


@product.route('/products', methods=['POST'])
def create_product(current_user):
    """
    Function Adds a product to database given that the data input is valid
    If data input is not valid function will return a customise error message

    :params current_user:
    """
    try:
        data = request.data
        data = json.loads(data)
        product_name = data['product_name']
        product_quantity = data['product_quantity']
        product_price = data['product_price']
        product_description = data['product_description']
        #check if content type is application/json
        if not request.content_type == 'application/json': 
            return jsonify({'error':'Wrong content-type'}),400
        if admin_required() != True:
            return jsonify({'error':'You are not allowed to access this resource'}),400
        if not product_name or not product_quantity or not product_price or product_description == "":
            return jsonify({'error':'One of the required fields is empty'}),400
        if not isinstance(product_price,int) or not isinstance(product_quantity,int) or product_price < 1 or product_quantity < 1:
            return jsonify({'error':'price or quantity must be a number and must be greater than 1'}),400
        if (' ' in product_name) == True:
            return jsonify({'error':'poduct cannot contain spaces'}),400
        for product_item in product_db:
            if product_name == product_item['product_name'] and product_description == product_item['product_description']\
            and product_price == product_item['product_price']:
                product_item['product_quantity'] = product_item['product_quantity'] + product_quantity
                return jsonify({'message':'Product Updated Successfully'}),201
        product = Product(product_name,product_quantity,product_price,product_description)
        product_db.append(product.to_dict())
        return jsonify({'status':'Product created'}),201
    except Exception:
        return jsonify({'error':'required field/s missing'}), 400  
@product.route('/products', methods=['GET'])
def get_products():
    """
    Function returns products from the database
    If the database is empty, function will return a customised error
    """
    if len(admin_db) == 0 and len(user_db) == 0:
        return jsonify({'error':'login first'}),401
    if len(product_db) == 0:
        return jsonify({'error':'There no products at the moment'}),404
    return jsonify({'Products-Available':product_db}),200

@product.route('/products/<product_id>', methods=['GET'])
def get_product(product_id): 
    """
    Function returns a specific product filtered by a product id
    :params product_id:
    """
    if len(admin_db) == 0 and len(user_db) == 0:
        return jsonify({'error':'login first'}),401  
    if len(product_db) == 0:
        return jsonify({'error':'There no products at the moment'}),404
    for product_item in product_db:
        if product_item['product_id'] == product_id:
            return jsonify({'result':product_item}),200
    return jsonify({'error':'Product not found'}),404 

#custom error handler
@product.app_errorhandler(404)
def not_found(error):
    """ Customise HTTP 404 Not found error to return custom message
        when ever an HTTP error 404 is raised.
    """
    return make_response(jsonify({'error':' :( Oops nothing here'})),404