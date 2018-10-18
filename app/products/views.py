from flask import Blueprint,request,jsonify,abort,json,make_response
from .models import Product


# create product blueprint
# blueprint will handle all product routes for the app
product = Blueprint('product',__name__)

product_db = [] #List will hold all products created in the app




@product.route('/products', methods=['POST'])
def create_product():
    data = request.data
    data = json.loads(data)
    product_name = data['product_name']
    product_quantity = int(data['product_quantity'])
    product_price = int(data['product_price'])
    product_description = data['product_description']

    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400

    if product_name == "" or product_quantity == "" or product_price == "" or product_description == "":
        abort(400)
  
    for product_item in product_db:
        if product_name == product_item['product_name'] and product_description == product_item['product_description'] and product_price == product_item['product_price']:
            product_item['product_quantity'] = product_item['product_quantity'] + product_quantity
            return jsonify({'message':'Product Updated Successfully'}),201

    product = Product(product_name,product_quantity,product_price,product_description)
    product_db.append(product.to_dict())

    return jsonify({'status':'Product created'}),201

@product.route('/products', methods=['GET'])
def get_products():
    if request.method != 'GET':
        abort(405)

    if len(product_db) == 0:
        abort(404)
    return jsonify({'Products-Available':product_db}),200
        

@product.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    if product_id == "":
        abort(400)
        
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
    return make_response(jsonify({'Error':':( Oops Nothing found'}),404)

@product.app_errorhandler(405)
def method_not_allowed(error):
    """Function takes in HTTP error 405 and returns custom HTTP error 405 message """
    return make_response(jsonify({'Error':':( Oops Your trying to use a wrong HTTP Method'}),405)

@product.app_errorhandler(400)
def bad_request(error):
    """Function takes in HTTP error 400 and returns custom HTTP error 400 message """
    return make_response(jsonify({'Error':':( BAD REQUEST'}),400)

@product.app_errorhandler(401)    
def unauthorised(error):
    """Function takes in HTTP error 401 and returns custom HTTP error 401 message """
    return make_response(jsonify({'Error':'You are not allowed to access this resource'}),401)

@product.app_errorhandler(500)
def internal_server_error(error):
    """Function takes in HTTP error 500 and returns custom HTTP error 500 message """
    return make_response(jsonify({'Error':'Server run into some error'}))

    









