# from flask import Blueprint,request,jsonify,json
# import datetime
# from .models import Sale
# # from ..products.views import product_db
# # from ..auth.views import user_db,admin_db
# # from ..auth.utility import login_required,admin_required,login_admin_required


# # create sales blueprint
# # blueprint will handle all sales routes for the app and routes for sale records
# sale_bp = Blueprint('sale_bp',__name__)


# sale_records = [] #List to store sale records for the app


# @sale_bp.route('/sales', methods=['POST'])
# @login_required
# def create_sale_order(current_user):
#     """
#     Function creates a sale order given that the product name matches
#     with what is in the system 

#     :params current_user:
#     """
#     try:
#         data = request.data
#         data = json.loads(data)
#         product_name = data['product_name']
#         product_quantity = data['product_quantity']
#         #check if content type is application/json
#         if not request.content_type == 'application/json': 
#             return jsonify({'error':'Wrong content-type'}),400
#         if not product_name or not product_quantity or not isinstance(product_quantity,int) or product_quantity < 1 or (' ' in product_name) == True:
#             return jsonify({'error':'required field has invalid data'}),400
#         if len(product_db) == 0:
#             return jsonify({'error':'There no products yet'}),404
#         for prodt in product_db:
#             if prodt['product_name'] == product_name:
#                 if prodt['product_quantity'] == 0 or product_quantity > prodt['product_quantity']:
#                     return jsonify({'error':'Sorry product is out of stock'}),400
#                 Total = int(prodt['product_price']) * product_quantity
#                 sale_record = Sale(current_user['user_id'],current_user['user_name'],product_name,\
#                 product_quantity,prodt['product_price'],Total,datetime.datetime.utcnow())
#                 sale_records.append(sale_record.to_dict())
#                 new_quantity = prodt['product_quantity'] - product_quantity
#                 prodt['product_quantity'] = new_quantity
#                 return jsonify({'message':'Sale record created','result':sale_records}),201
#     except Exception:
#         return jsonify({'error':'required field/s missing'}), 400            
#     return jsonify({'error':'Product not found'}),404
    
        
# @sale_bp.route('/sales', methods=['GET'])
# @login_admin_required
# def get_sales(current_user):
#     """
#     Function retrieves all sale records from the database

#     :params current_user:
#     """
#     if admin_required() != True:
#         return jsonify({'error':'You are not allowed to access this resource'}),401
#     if len(sale_records) == 0:
#         return jsonify({'error':'No sales made yet'}),404
#     return jsonify({'result':sale_records,'status':'Success'}),200


# @sale_bp.route('/sales/<sale_id>', methods=['GET'])
# def get_sale(sale_id):
#     """
#     Function retrieves a sale given the input sale_id matches with
#     a sale id of one of the sale records in the database
#     """
#     if len(admin_db) == 0 and len(user_db) == 0:
#         return jsonify({'error':'login first'}),401   
#     for sold in sale_records:
#         if sold['sale_id'] == sale_id:
#             return jsonify({'result':sold}),200
#     return jsonify({'error':'Sale record doesnot exist'}),404