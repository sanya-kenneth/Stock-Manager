from flask import Blueprint,request,jsonify,abort,json,make_response
from .models import Product
from ..auth.utility import login_required,admin_required
from ..auth.views import user_db



# create product blueprint
# blueprint will handle all product routes for the app
product = Blueprint('product',__name__)

product_db = [] #List will hold all products created in the app




@product.route('/products', methods=['POST'])
@login_required
def create_product(current_user):
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
        abort(401)

    if product_name == "" or product_quantity == "" or product_price == "" or product_description == "":
        abort(400)

    if (' ' in product_name) == True:
        abort(400)
    
    if type(product_price) != int or type(product_quantity) != int:
        abort(400)

    if product_price < 1 or product_quantity < 1:
        return jsonify({'Error':'Price or quantity must be greater than 1'}),400
  
    for product_item in product_db:
        if product_name == product_item['product_name'] and product_description == product_item['product_description'] and product_price == product_item['product_price']:
            product_item['product_quantity'] = product_item['product_quantity'] + product_quantity
            return jsonify({'message':'Product Updated Successfully'}),201

    product = Product(product_name,product_quantity,product_price,product_description)
    product_db.append(product.to_dict())

    return jsonify({'status':'Product created'}),201

@product.route('/products', methods=['GET'])
@login_required
def get_products(current_user):
    
    if len(product_db) == 0:
        abort(404)

    return jsonify({'Products-Available':product_db}),200
        

@product.route('/products/<product_id>', methods=['GET'])
@login_required
def get_product(current_user,product_id):   
    if len(product_db) == 0:
        abort(404)
    
    for product_item in product_db:
        if product_item['product_id'] == product_id:
            return jsonify({'result':product_item}),200

    abort(404)
       

#Custom error handlers
@product.app_errorhandler(404)
def not_found(error):
    """Function takes in HTTP error 404 and returns custom HTTP error 404 message """
    return make_response(jsonify({'error':':( Oops Nothing found'}),404)

@product.app_errorhandler(405)
def method_not_allowed(error):
    """HTTP error 405 handler """
    return make_response(jsonify({'Error':':( Oops Your trying to use a wrong HTTP Method'}),405)

@product.app_errorhandler(400)
def bad_request(error):
    """ 400 status_code error handler """
    return make_response(jsonify({'Stop':':( BAD REQUEST'}),400)

@product.app_errorhandler(401)    
def unauthorised(error):
    """ Returns custom 401 error message """
    return make_response(jsonify({'Oops':'You are not allowed to access this resource'}),401)





    









