from .views import user_db
from functools import wraps
from flask import jsonify,abort



def login_required(f):
    def decorate(*args,**kwargs):
        if len(user_db) == 0:
            abort(401)
        for user_dt in user_db:
            if user_dt['loggedin'] != True:
                return jsonify({'Error':'You are not logged in'}),401    
            else:
                current_user = user_dt             
        return f(current_user,*args,**kwargs)
    return decorate

