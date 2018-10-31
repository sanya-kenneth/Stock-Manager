from flask import Blueprint,request,jsonify,json
from app.auth.models import User
from app.auth.database import Database,db
from werkzeug.security import check_password_hash,generate_password_hash
from validate_email import validate_email
import re




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
    try:
        data = request.data
        data = json.loads(data)
        user_name = data['user_name']
        user_email = data['user_email']
        user_password = str(data['user_password'])
        #check if content type is application/json
        if not request.content_type == 'application/json': 
            return jsonify({'error':'Wrong content-type'}),400
        if user_name == "" or user_password == "" or user_email == "":
            return jsonify({'error':'username,email or password cannot be empty'}),400
        if type(user_name) != str or type(user_email) != str:
            return jsonify({'error':'username or email must be a string'}),400
        if re.search('[\s]',user_name) != None:
            return jsonify({'error':'Username cannot contain spaces'}),400
        if validate_email(user_email) == False:
            return jsonify({'error':'Invalid email'}),400
        usr_password = generate_password_hash(user_password, method='sha256')
        user = User(user_name,user_email,usr_password)
        users = db.select_users()
        for fetch_user in users:
            if fetch_user[1] == user_name or fetch_user[2] == user_email:
                return jsonify({'error':'user already exists'}),400
        user.insert_user()
        return jsonify({'message':'Account was successfuly created'}),201
    except Exception:
        return jsonify({'error':'Required field/s missing'}),400
    
                   
            
#Login route for store attendant and admin
@auths.route('/users/login',methods=['POST'])
def login():
    """
    Function to login a store attendant into the system
    if the store attendant account doesnot exist, an error is returned
    """
    try:
        user_info = request.data
        login_info = json.loads(user_info)
        user_email = login_info['email']
        user_password = str(login_info['password'])
        if not user_email or not user_password:
            return jsonify({'error':'useremail or password cannot be empty'}),400
        if not isinstance(user_email, str):
            return jsonify({'error':'useremail must be a string'}),400
        if validate_email(user_email) == False:
            return jsonify({'error':'Invalid email'}),400
        user_data = db.select_users()
        for user in user_data:
            if user[2] == user_email and check_password_hash(user[3],user_password):
                return jsonify({'message':'You are now loggedin'}),200
        return jsonify({'error':'Wrong useremail or password'}),400
    except Exception:
        return jsonify({'error':'Required field/s missing'}),400