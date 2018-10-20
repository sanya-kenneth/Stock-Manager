from flask import Blueprint,request,jsonify,abort,json,make_response
import datetime
from .models import Sale
from ..products.views import product_db
from ..auth.views import user_db
from ..auth.utility import login_required,admin_required


# create sales blueprint
# blueprint will handle all sales routes for the app and routes for sale records
sale_bp = Blueprint('sale_bp',__name__)


sale_records = [] #List to store sale records for the app


@sale_bp.route('/sales', methods=['POST'])
@login_required
def create_sale_order(current_user):
    data = request.data
    data = json.loads(data)
    product_name = data['product_name']
    product_quantity = data['product_quantity']

    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400

    if admin_required() == True:
        abort(401)

    if product_name == "" or product_quantity == "" or type(product_quantity) != int or product_quantity < 1 or (' ' in product_name) == True:
        abort(400)
  
    if len(product_db) == 0:
        abort(404)

    for product_item in product_db:
        if product_name != product_item['product_name']:
            abort(404)

        if product_item['product_quantity'] == 0 or product_quantity > product_item['product_quantity']:
            return jsonify({'error':'Sorry product is out of stock'}),400

        Total = int(product_item['product_price']) * product_quantity
        sale_record = Sale(current_user['user_id'],current_user['user_name'],product_name,product_quantity,product_item['product_price'],Total,datetime.datetime.utcnow())
        sale_records.append(sale_record.to_dict())
        new_quantity = product_item['product_quantity'] - product_quantity
        product_item['product_quantity'] = new_quantity

        return jsonify({'message':'Sale record created','result':sale_records}),201
    

@sale_bp.route('/sales', methods=['GET'])
@login_required
def get_sales(current_user):
    if admin_required() != True:
        abort(401)

    if len(sale_records) == 0:
        abort(404)
    
    return jsonify({'result':sale_records,'status':'Success'})


@sale_bp.route('/sales/<sale_id>', methods=['GET'])
@login_required
def get_sale(current_user,sale_id):
    for sale_made in sale_records:
        if current_user['admin_status'] == True or current_user['user_id'] == sale_made['attedt_id']:
            if sale_id == "":
                abort(400)
    
            if len(sale_records) == 0:
                abort(404)

            for sale_made in sale_records:
                if sale_id == sale_made['sale_id']:
                    return jsonify({'result':sale_made}),200
                else:
                    abort(404)
    
    abort(401)

@sale_bp.app_errorhandler(401)    
def unauthorised(error):
    """ Returns custom 401 error message """
    return make_response(jsonify({'Oops':'You are not allowed to access this resource'}),401)
    

