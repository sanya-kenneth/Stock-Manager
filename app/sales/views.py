from flask import request,jsonify,json
import datetime
from .models import Sale
from app.auth.database import db_handler
from app.auth.utility import check_admin
from app.auth.views import protected_route
from app.sales import sale_bp


sales_list = []


@sale_bp.route('/sales', methods=['POST'])
@protected_route
def create_sale_order(current_user):
    """
    Function creates a sale order given that the product name matches
    with what is in the system 

    :params current_user:
    """
    # try:
    data = request.data
    data = json.loads(data)
    product_id = data['product_id']
    product_quantity = data['product_quantity']
    if check_admin(current_user) != True:
        return jsonify({'error':'Access Denied. Please login as a store attendant'}),401
    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if product_quantity < 1:
        return jsonify({'error':'Product quantity cannot be less than 1'}),400
    if not product_id or not isinstance(product_id,int) or not product_quantity or not isinstance(product_quantity,int):
        return jsonify({'error':'Product quantity or id cannot be empty and must be a number'}),400
    product_selected = db_handler().select_a_product(product_id)
    products = db_handler().select_products()
    if product_selected == None:
        return jsonify({'message':'Product not found'}),404
    if len(products) == 0:
        return jsonify({'message':'There no products in the system'}),404
    if product_selected[2] == 0 or product_quantity > product_selected[2]:
        return jsonify({'error':'Sorry product is out of stock or quantity selected is higher than quantity available'}),400
    Total = int(product_selected[3]) * product_quantity
    new_quantity = product_selected[2] - product_quantity
    sale_record = Sale(current_user[0],current_user[1],product_id,\
    product_selected[1],product_quantity,Total,datetime.datetime.utcnow())
    sale_record.add_sale()                 
    sale_display = {
            'Attendant_Id': sale_record.attedt_id,
            'Attendant_name': sale_record.attedt_name,
            'Product_Id': sale_record.product_id,
            'Product_name': sale_record.product_name,
            'Product_quantity':sale_record.product_quantity,
            'Total':sale_record.Total,
            'Sale_date':sale_record.sale_date 
                }
    db_handler().update_quantity(product_id,new_quantity)
    return jsonify({'Sale_record':sale_display,'message':'Sale was successfully made'}),201        
    # except Exception:
    #     return jsonify({'error':'Required field/s missing'}),400
    
        
@sale_bp.route('/sales', methods=['GET'])
@protected_route
def get_sales(current_user):
    """
    Function retrieves all sale records from the database

    :params current_user:
    """
    if check_admin(current_user) == True:
        return jsonify({'error':'Access Denied. Please login as admin'}),401
    keys = ['Sale_Id','Attendant_Id','Attendant_name','Product_Id','Product_name','Product_quantity','Total','Date_of_sale']
    sales = db_handler().select_sales()
    if len(sales) == 0:
        return jsonify({'message':'No sales made yet'}), 404
    for sale in sales:
        sales_list.append(dict(zip(keys,sale)))
    return jsonify({'Sales_records':sales_list}),200


@sale_bp.route('/sales/<sale_id>', methods=['GET'])
@protected_route
def get_sale(current_user,sale_id):
    """
    Function retrieves a sale given the input sale_id matches with
    a sale id of one of the sale records in the database
    """  
    sale_record = db_handler().select_sale(sale_id)
    if sale_record == None:
        return jsonify({'message':'Sale record doesnot exist'}),404
    returned_sale = {'Sale_Id':sale_record[0],
             'Attendant_Id':sale_record[1],
             'Attendant_name':sale_record[2],
             'Product_Id':sale_record[3],
             'Product_name':sale_record[4],
             'Product_quantity':sale_record[5],
             'Total':sale_record[6],
             'Date_of_sale':sale_record[7]
            }
    return jsonify({'Sale-record':returned_sale}),200
    