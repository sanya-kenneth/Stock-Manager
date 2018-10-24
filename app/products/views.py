from flask import Blueprint,request,jsonify,json
from .models import Product
from ..auth.utility import login_required,admin_required,login_admin_required




# create product blueprint
# blueprint will handle all product routes for the app
product = Blueprint('product',__name__)

product_db = [] #List will hold all products created in the app




@product.route('/products', methods=['POST'])
@login_admin_required
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
        return jsonify({'error':'You are not allowed to access this resource'}),400
    if product_name == "" or product_quantity == "" or product_price == "" or product_description == "":
        return jsonify({'error':'One of the required fields is empty'}),400
    if not isinstance(product_price,int) or not isinstance(product_quantity,int) or product_price < 1 or product_quantity < 1:
        return jsonify({'error':'price or quantity must be a number and must be greater than 1'}),400
    if (' ' in product_name) == True:
        return jsonify({'error':'poduct cannot contain spaces'}),400
    for product_item in product_db:
        if product_name == product_item['product_name'] and product_description == product_item['product_description'] and product_price == product_item['product_price']:
            product_item['product_quantity'] = product_item['product_quantity'] + product_quantity
            return jsonify({'message':'Product Updated Successfully'}),201

    product = Product(product_name,product_quantity,product_price,product_description)
    product_db.append(product.to_dict())

    return jsonify({'status':'Product created'}),201

@product.route('/products', methods=['GET'])
def get_products():
    if len(product_db) == 0:
        return jsonify({'error':'There no products at the moment'}),404
    return jsonify({'Products-Available':product_db}),200

@product.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):   
    if len(product_db) == 0:
        return jsonify({'error':'There no products at the moment'}),404
    for product_item in product_db:
        if product_item['product_id'] == product_id:
            return jsonify({'result':product_item}),200
    return jsonify({'error':'Product not found'}),404 
       








    









