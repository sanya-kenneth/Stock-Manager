from flask import Blueprint,request,jsonify,json,make_response
from .models import Product
from app.auth.database import db
from app.auth.views import protected_route
from app.auth.views import check_admin
import re



# create product blueprint
# blueprint will handle all product routes for the app
product = Blueprint('product',__name__)



@product.route('/products', methods=['POST'])
@protected_route
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
        if check_admin(current_user) == True:
            return jsonify({'error':'Access Denied. Please login as admin'}),401
        #check if content type is application/json
        if not request.content_type == 'application/json': 
            return jsonify({'error':'Wrong content-type'}),400
        if not product_name or not product_quantity or not product_price or product_description == "":
            return jsonify({'error':'One of the required fields is empty'}),400
        if not isinstance(product_price,int) or not isinstance(product_quantity,int) or product_price < 1 or product_quantity < 1:
            return jsonify({'error':'price or quantity must be a number and must be greater than 1'}),400
        if re.search('[\s]',product_name) != None:
            return jsonify({'error':'poductname cannot contain spaces'}),400
        products = db.select_products()
        for product in products:
            if product_name == product[1] and product_description == product[4]:
                return jsonify({'error':'Product already exists'}),400
        product = Product(product_name,product_quantity,product_price,product_description)
        product.add_product()
        return jsonify({'status':'Product created'}),201
    except Exception:
        return jsonify({'error':'Required field/s missing'}),400
    

@product.route('/products', methods=['GET'])
@protected_route
def get_products(current_user):
    """
    Function returns products from the database
    If the database is empty, function will return a customised error
    """
    products = db.select_products()
    if len(products) == 0:
        return jsonify({'error':'There no products at the moment'}),404
    return jsonify({'Products-Available':products}),200


@product.route('/products/<productid>', methods=['GET'])
@protected_route
def get_product(current_user,productid): 
    """
    Function returns a specific product filtered by a product id
    :params product_id:
    """
    store_products = db.select_products() 
    if len(store_products) == 0:
        return jsonify({'error':'There no products at the moment'}),404
    product_fetched = db.select_a_product(productid)
    if product_fetched == None:
        return jsonify({'error':'Product was not found'}),404
    return jsonify({'result':product_fetched}),200


@product.route('/products/<productid>', methods=['PUT'])
@protected_route
def update_product(current_user,productid):
    """
    Function updates a product if the provided productid is correct
    :params productid:
    """
    try:
        data = request.data
        data = json.loads(data)
        prodt_name = data['productname']
        prodt_quantity = data['productquantity']
        prodt_price = data['productprice']
        prodt_desc = data['productdescription']
        if not request.content_type == 'application/json': 
            return jsonify({'error':'Wrong content-type'}),400
        if not prodt_name or not prodt_quantity or not prodt_price or not prodt_desc:
            return jsonify({'error':'required field cannot be empty'}),400
        if re.search('[\s]',prodt_name) != None:
            return jsonify({'error':'poductname cannot contain spaces'}),400
        if not isinstance(prodt_price,int) or not isinstance(prodt_quantity,int) or prodt_price < 1 or prodt_quantity < 1:
            return jsonify({'error':'price or quantity must be a number and must be greater than 1'}),400
        product_to_update = db.select_a_product(productid)
        if product_to_update == None:
            return jsonify({'error':'Product not found'}),404
        if product_to_update[0] == int(productid):
            db.update_product(productid,prodt_name,prodt_quantity,prodt_price,prodt_desc)
            return jsonify({'message':'Product successfuly updated'}),201
    except Exception:
        return jsonify({'error':'Required field/s missing'}),400


@product.route('/products/<productid>', methods=['DELETE'])
@protected_route
def delete_product(current_user,productid):
    selected_product = db.select_a_product(productid)
    if selected_product == None:
        return jsonify({'error':'Product not found'}),404
    db.delete_product(productid)
    return jsonify({'message':'Product was deleted successfuly'})
    
    

#custom error handler
@product.app_errorhandler(405)
def not_found(error):
    """ Customise HTTP 405 Method not allowed error to return custom message
        when ever an HTTP error 405 is raised.
    """
    return make_response(jsonify({'error':' :( Oops Method Not Allowed'})),405