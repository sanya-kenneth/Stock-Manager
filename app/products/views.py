from flask import Blueprint,request,jsonify,make_response,abort,json
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
    product_price = data['product_price']
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

    if len(product_db) <= 0:
        abort(404)
    return jsonify({'Products-Available':product_db}),200
        

@product.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    if product_id == "":
        abort(400)
        
    if len(product_db) <= 0:
        abort(404)
    
    for product_item in product_db:
        if product_item['product_id'] == product_id:
            return jsonify({'result':product_item}),200

    abort(404)
       

    









