from flask import request,jsonify,json,make_response
from .models import Product
from app.auth.database import db_handler
from app.auth.views import protected_route
from app.auth.views import check_admin
from app.products import product
import re


products_list = []


@product.route('/products', methods=['POST'])
@protected_route
def create_product(current_user):
    """
    Function Adds a product to database given that the data input is valid
    If data input is not valid function will return a customise error message

    :params current_user:
    """
    data = request.data
    data = json.loads(data)
    product_name = data['product_name']
    product_quantity = data['product_quantity']
    product_price = data['product_price']
    product_description = data['product_description']
    if check_admin(current_user) is True:
        return jsonify({'error':'Access Denied. Please login as admin'}),401
    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if not product_name or not product_quantity or not product_price or product_description == "":
        return jsonify({'error':'One of the required fields is empty'}),400
    if not isinstance(product_price,int) or not isinstance(product_quantity,int) or product_price < 1 or product_quantity < 1:
        return jsonify({'error':'price or quantity must be a number and must be greater than 1'}),400
    if re.search(r'[\s]',product_name) != None:
        return jsonify({'error':'poductname cannot contain spaces'}),400
    products = db_handler().select_products()
    for product in products:
        if product_name == product[1] and product_description == product[4]:
            return jsonify({'error':'Product already exists'}),400
    product = Product(product_name,product_quantity,product_price,product_description)
    product.add_product()
    return jsonify({'status':'Product created'}),201
    
    

@product.route('/products', methods=['GET'])
@protected_route
def get_products(current_user):
    """
    Function returns products from the database
    If the database is empty, function will return a customised error
    """
    products = db_handler().select_products()
    if len(products) == 0:
        return jsonify({'message':'There no products at the moment'}),404
    keys = ['Product_id','Product_name','Product_quantity','Product_price','Product_description','Date_added']
    for product in products:
        products_list.append(dict(zip(keys,product)))
    return jsonify({'Products':products_list}),200
    

@product.route('/products/<productid>', methods=['GET'])
@protected_route
def get_product(current_user,productid): 
    """
    Function returns a specific product filtered by a product id
    :params product_id:
    """
    store_products = db_handler().select_products() 
    if len(store_products) == 0:
        return jsonify({'message':'There no products at the moment'}),404
    product_fetched = db_handler().select_a_product(productid)
    if product_fetched == None:
        return jsonify({'message':'Product was not found'}),404
    product = {
              'Product_id':product_fetched[0],
              'Product_name':product_fetched[1],
              'Product_quantity':product_fetched[2],
              'Product_price': product_fetched[3],
              'Product_description':product_fetched[4],
              'Date_added':product_fetched[5]
              }
    return jsonify({'Product':product}),200

@product.route('/products/<productid>', methods=['PUT'])
@protected_route
def update_product(current_user,productid):
    """
    Function updates a product if the provided productid is correct
    :params productid:
    """
    data = request.data
    data = json.loads(data)
    prodt_name = data['productname']
    prodt_quantity = data['productquantity']
    prodt_price = data['productprice']
    prodt_desc = data['productdescription']
    if check_admin(current_user) is True:
        return jsonify({'error':'Access Denied. Please login as admin'}),401
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if not prodt_name or not prodt_quantity or not prodt_price or not prodt_desc:
        return jsonify({'error':'required field cannot be empty'}),400
    if re.search(r'[\s]',prodt_name) != None:
        return jsonify({'error':'poductname cannot contain spaces'}),400
    if not isinstance(prodt_price,int) or not isinstance(prodt_quantity,int) or prodt_price < 1 or prodt_quantity < 1:
        return jsonify({'error':'price or quantity must be a number and must be greater than 1'}),400
    product_to_update = db_handler().select_a_product(productid)
    if product_to_update == None:
        return jsonify({'message':'Product not found'}),404
    if product_to_update[0] == int(productid):
        db_handler().update_product(productid,prodt_name,prodt_quantity,prodt_price,prodt_desc)
        product_updated = db_handler().select_a_product(productid)
        product = {
                    'Product_id':product_updated[0],
                    'Product_name':product_updated[1],
                    'Product_quantity':product_updated[2],
                    'Product_price':product_updated[3],
                    'Product_description':product_updated[4]
                    }
        return jsonify({'Product':product,'message':'Product successfully updated'}),201


@product.route('/products/<productid>', methods=['DELETE'])
@protected_route
def delete_product(current_user,productid):
    if check_admin(current_user) is True:
        return jsonify({'error':'Access Denied. Please login as admin'}),401
    selected_product = db_handler().select_a_product(productid)
    if selected_product == None:
        return jsonify({'message':'Product not found'}),404
    db_handler().delete_product(productid)
    return jsonify({'message':'Product was deleted successfuly'}),200
    
    
#custom error handler
@product.app_errorhandler(405)
def not_found(error):
    """ Customise HTTP 405 Method not allowed error to return custom message
        when ever an HTTP error 405 is raised.
    """
    return make_response(jsonify({'error':' :( Oops Method Not Allowed'})),405