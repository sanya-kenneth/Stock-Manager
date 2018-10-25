from flask import Blueprint,request,jsonify,json
from .models import User,Admin
from werkzeug.security import check_password_hash,generate_password_hash




# Users and authentication blueprint
# blueprint will handle all app user routes
auths = Blueprint('auths',__name__)

user_db = [] #List to hold user data
admin_db = [] #List to hold admin data


@auths.route('/users', methods=['POST'])
def create_store_attendant():
    data = request.data
    data = json.loads(data)
    user_name = data['user_name']
    user_password = str(data['user_password'])
    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if user_name == "" or user_password == "":
        return jsonify({'error':'username or password cannot be empty'}),400
    if not isinstance(user_name,str):
        return jsonify({'error':'username must be a string'}),400
    if (' ' in user_name) == True:
        return jsonify({'Error':'user name cannot contain a space'}),400
    # check_user(user_name,user_password)
    for fetch_user in user_db:
        if fetch_user['user_password'] == user_password or fetch_user['user_name'] == user_name:
            return jsonify({'error':'user already exists'}),400
    usr_password = generate_password_hash(user_password, method='sha256')
    #Initialise User object to add provided data
    store_attendant = User(user_name,usr_password)
    user_db.append(store_attendant.to_dict())
    return jsonify({'message':'Account was successfuly created'}),201


@auths.route('users/admin', methods=['POST'])  
def create_admin():
    admin_details = json.loads(request.data)
    admin_name = admin_details['admin_name']
    admin_password = str(admin_details['admin_password'])
    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if not admin_name or not admin_password:
        return jsonify({'error':'username or password cannot be empty'}),400
    if not isinstance(admin_name,str):
        return jsonify({'error':'username must be a string'}),400
    if (' ' in admin_name) == True:
        return jsonify({'Error':'user name cannot contain a space'}),400
    # check_user(admin_name, admin_password)
    for get_admin in admin_db:
        if admin_name == get_admin['user_name']:
            return jsonify({'error':'Admin exists'}),400
    adm_password = generate_password_hash(admin_password, method='sha256')
    #Initialise admin object to add provided data
    admin = Admin(admin_name,adm_password)
    admin_db.append(admin.to_dict())
    return jsonify({'message':'Account was successfuly created'}),201


@auths.route('/users/login',methods=['POST'])
def login():
    user_info = request.data
    login_info = json.loads(user_info)
    user_name = login_info['name']
    user_password = str(login_info['password'])
    if not user_name or not user_password:
        return jsonify({'error':'username or password cannot be empty'}),400
    if not isinstance(user_name, str):
        return jsonify({'error':'username must be a string'}),400
    if (' ' in user_name) == True:
        return jsonify({'Error':'user name cannot contain a space'}),400
    for user in user_db:
        password = user['user_password']
        if user['user_name'] == user_name and check_password_hash(password,user_password):
            user['loggedin'] = True
            return jsonify({'message':'You are now loggedin'}),200
    return jsonify({'error':'Wrong username or password'}),400

@auths.route('/users/login/admin',methods=['POST'])
def log_admin():
    admin_data = request.data
    sign_data = json.loads(admin_data)
    admin_user_name = sign_data['name']
    admin_user_password = str(sign_data['password'])
    if not admin_user_name or not admin_user_password:
        return jsonify({'error':'username or password cannot be empty'}),400
    if not isinstance(admin_user_name,str):
        return jsonify({'error':'username must be a string'}),400
    if (' ' in admin_user_name) == True:
        return jsonify({'Error':'user name cannot contain a space'}),400
    for user in admin_db:
        password = user['user_password']
        if user['user_name'] == admin_user_name  and check_password_hash(password,admin_user_password):
            user['loggedin'] = True
            return jsonify({'message':'You are now loggedin'}),200
    return jsonify({'error':'Wrong username or password'}),400