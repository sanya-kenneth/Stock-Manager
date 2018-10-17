from flask import Blueprint,request,jsonify,make_response,abort,json
from .models import User,Admin
from werkzeug.security import check_password_hash,generate_password_hash



# Users and authentication blueprint
# blueprint will handle all app user routes
auth = Blueprint('auth',__name__)

user_db = [] #List to hold user data


@auth.route('/users', methods=['POST'])
def create_store_attendant():
    data = request.data
    data = json.loads(data)
    user_name = data['user_name']
    user_password = str(data['user_password'])

    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400

    if user_name == "" or user_password == "":
        abort(400)

    for user in user_db:
        if user['user_name'] == user_name or user['user_password'] == user_password:
            return jsonify({'message':'Account already exists'}),400

    usr_password = generate_password_hash(user_password, method='sha256')
    store_attendant = User(user_name,usr_password)
    user_db.append(store_attendant.to_dict())

    return jsonify({'message':'Account was successfuly created'}),201


@auth.route('users/admin', methods=['POST'])  
def create_admin():
    data = request.data
    data = json.loads(data)
    admin_name = data['admin_name']
    admin_password = str(data['admin_password'])

     #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400

    if admin_name == "" or admin_password == "":
        abort(400)

    for admin in user_db:
        if admin['user_name'] == admin_name or admin['user_password'] == admin_password:
            return jsonify({'message':'Account already exists'}),400

    adm_password = generate_password_hash(admin_password, method='sha256')
    admin = Admin(admin_name,adm_password)
    user_db.append(admin.to_dict())

    return jsonify({'message':'Account was successfuly created'}),201


@auth.route('/users/login',methods=['POST'])
@auth.route('/users/login/admin',methods=['POST'])
def login():
    data = request.data
    data = json.loads(data)
    user_name = data['name']
    user_password = str(data['password'])

    if user_name == "" or user_password == "":
        abort(400)

    for user in user_db:
        password = user['user_password']
        if user['user_name'] == user_name and check_password_hash(password,user_password):
            user['loggedin'] = True
            return jsonify({'message':'You are now loggedin'}),200

    return jsonify({'error':'Wrong username or password'}),400

    
        

