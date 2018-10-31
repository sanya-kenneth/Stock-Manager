from flask import Blueprint,request,jsonify,json
from app.auth.models import User
from app.auth.database import Database,db
from werkzeug.security import check_password_hash,generate_password_hash




# Users and authentication blueprint
# blueprint will handle all app user routes
auths = Blueprint('auths',__name__)



#create a store attendant route
@auths.route('/users', methods=['POST'])
def create_store_attendant():
    """
    Function adds a store attendant to the system given that the data input is valid
    If data input is not valid function will return a customise error message

    """
    data = request.data
    data = json.loads(data)
    user_name = data['user_name']
    user_email = data['user_email']
    user_password = str(data['user_password'])
    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if user_name == "" or user_password == "":
        return jsonify({'error':'username or password cannot be empty'}),400
    if not isinstance(user_name,str):
        return jsonify({'error':'username must be a string'}),400
    # if (' ' in user_name) == True:
    #     return jsonify({'Error':'user name cannot contain a space'}),400
    usr_password = generate_password_hash(user_password, method='sha256')
    user = User(user_name,user_email,usr_password)
    users = db.select_users()
    for fetch_user in users:
        if fetch_user[1] == user_name or fetch_user[2] == user_email:
            return jsonify({'error':'user already exists'}),400
    user.insert_user()
    return jsonify({'message':'Account was successfuly created'}),201
    
                   
            
#Login route for store attendant and admin
@auths.route('/users/login',methods=['POST'])
def login():
    """
    Function to login a store attendant into the system
    if the store attendant account doesnot exist, an error is returned
    """
    user_info = request.data
    login_info = json.loads(user_info)
    user_email = login_info['email']
    user_password = str(login_info['password'])
    if not user_email or not user_password:
        return jsonify({'error':'username or password cannot be empty'}),400
    if not isinstance(user_email, str):
        return jsonify({'error':'username must be a string'}),400
    # if (' ' in user_name) == True:
    #     return jsonify({'Error':'user name cannot contain a space'}),400
    user_data = db.select_users()
    for user in user_data:
        if user[2] == user_email and check_password_hash(user[3],user_password):
            return jsonify({'message':'You are now loggedin'}),200
    return jsonify({'error':'Wrong username or password'}),400
     