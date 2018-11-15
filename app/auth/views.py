from flask import Blueprint,request,jsonify,json
from flask import current_app as app
from app.auth.models import User
from app.auth.database import Database
import jwt
from werkzeug.security import check_password_hash,generate_password_hash
from validate_email import validate_email
import re
from functools import wraps
import datetime
from app.auth.utility import check_admin
from app.auth import auths



# Users and authentication blueprint
# blueprint will handle all app user routes



def protected_route(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({'message':'Token is missing'}),401
        try:
            data = jwt.decode(token,app.config['SECRET'])  
            db = Database(app.config['DATABASE_URI'])
            data_fetch = db.select_users()
            for user_info in data_fetch:
                if user_info[2] == data['user']:
                    current_user = user_info         
        except:
            return jsonify({'error':'Token is invalid'}),401
        return f(current_user,*args,**kwargs)
    return decorated

#create a store attendant route
@auths.route('/users', methods=['POST'])
@protected_route
def create_store_attendant(current_user):
    """
    Function adds a store attendant to the system given that the data input is valid
    If data input is not valid function will return a customise error message

    """
    # try:
    data = request.data
    data = json.loads(data)
    user_name = data['user_name']
    user_email = data['user_email']
    user_password = str(data['user_password'])
    # if check_admin(current_user) == True:
    #     return jsonify({'error':'Access Denied. Please login as admin'}),401
    #check if content type is application/json
    if not request.content_type == 'application/json': 
        return jsonify({'error':'Wrong content-type'}),400
    if user_name == "" or user_password == "" or user_email == "":
        return jsonify({'error':'username,email or password cannot be empty'}),400
    if type(user_name) != str or type(user_email) != str:
        return jsonify({'error':'username or email must be a string'}),400
    if re.search(r'[\s]',user_name) != None:
        return jsonify({'error':'Username cannot contain spaces'}),400
    if validate_email(user_email) == False:
        return jsonify({'error':'Invalid email'}),400
    usr_password = generate_password_hash(user_password, method='sha256')
    db = Database(app.config['DATABASE_URI'])
    user = User(user_name,user_email,usr_password)
    users = db.select_users()
    for fetch_user in users:
        if fetch_user[1] == user_name or fetch_user[2] == user_email:
            return jsonify({'error':'user already exists'}),400
    user.insert_user()
    return jsonify({'message':'Store attendant was successfully registered'}),201
    # except Exception:
    #     return jsonify({'error':'Required field/s missing'}),400
    
                   
            
#Login route for store attendant and admin
@auths.route('/users/login',methods=['POST'])
def login():
    """
    Function to login a store attendant into the system
    if the store attendant account doesnot exist, an error is returned
    """
    # try:
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
    db = Database(app.config['DATABASE_URI'])
    user_data = db.select_users()
    for user in user_data:
        if user[2] == user_email and check_password_hash(user[3],user_password):
            token = jwt.encode({'user':user_email,'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=24)},app.config['SECRET'])
            return jsonify({'message':'You are now loggedin','token':token.decode('UTF-8')}),200
    return jsonify({'error':'Wrong useremail or password'}),400
    # except Exception:
    #     return jsonify({'error':'Required field/s missing'}),400
