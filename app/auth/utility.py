from .views import user_db,admin_db
from functools import wraps
from flask import jsonify



def login_required(function):
    @wraps(function)
    def decorate(*args,**kwargs):
        if len(user_db) == 0:
            return jsonify({'error':'Login first'}),401
        for user_dt in user_db:
                if user_dt['loggedin'] != True:
                    return jsonify({'Error':'You are not logged in'}),401 
                else:
                    current_user = user_dt            
        return function(current_user,*args,**kwargs)
    return decorate

def login_admin_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if len(admin_db) == 0:
            return jsonify({'error':'Sorry you must be an admin to access this resource'}),401
        for admin in admin_db:
            if admin['loggedin'] == False:
                return jsonify({'Error':'You are not logged in'}),401 
            current_admin = admin 
        return f(current_admin,*args,**kwargs)
    return decorated

        

def admin_required():
    for admin_dt in admin_db:
        if admin_dt['admin_status'] == True:
            return True
        else:
            return False