from flask import Blueprint,request,jsonify,json
import datetime
from .models import Sale
from app.auth.database import db


# create sales blueprint
# blueprint will handle all sales routes for the app and routes for sale records
sale_bp = Blueprint('sale_bp',__name__)



@sale_bp.route('/sales', methods=['POST'])
def create_sale_order():
    """
    Function creates a sale order given that the product name matches
    with what is in the system 

    :params current_user:
    """
    try:
        data = request.data
        data = json.loads(data)
        product_id = data['product_id']
        product_quantity = data['product_quantity']
        #check if content type is application/json
        if not request.content_type == 'application/json': 
            return jsonify({'error':'Wrong content-type'}),400
        if not product_id or not product_quantity or not isinstance(product_quantity,int) or product_quantity < 1:
            return jsonify({'error':'required field has invalid data'}),400
        product_selected = db.select_a_product(product_id)
        if product_selected[0] == product_id:
            if product_selected[2] == 0 or product_quantity > product_selected[2]:
                return jsonify({'error':'Sorry product is out of stock or quantity selected is higher than quantity available'}),400
            Total = int(product_selected[3]) * product_quantity
            sale_record = Sale(current_user[0],product_id,\
            product_quantity,Total,datetime.datetime.utcnow())
            sale_record.add_sale()
            return jsonify({'message':'Sale record created','result':sale_records}),201        
        return jsonify({'error':'Product not found'}),404
    except Exception:
        return jsonify({'error':'Required field/s missing'}),400
    
        
@sale_bp.route('/sales', methods=['GET'])
def get_sales():
    """
    Function retrieves all sale records from the database

    :params current_user:
    """
    sales = db.select_sales()
    if len(sales) == 0:
        return jsonify({'error':'No sales made yet'}), 404
    return jsonify({'result':sales,'status':'Success'}),200


@sale_bp.route('/sales/<sale_id>', methods=['GET'])
def get_sale(sale_id):
    """
    Function retrieves a sale given the input sale_id matches with
    a sale id of one of the sale records in the database
    """  
    if not isinstance(sale_id, int):
        return jsonify({'error':'Sale id must be a number'}),400
    sale_record = db.select_sale(sale_id)
    if sale_record == None:
        return jsonify({'error':'Sale record doesnot exist'}),404
    return jsonify({'result':sale_record}),200
    