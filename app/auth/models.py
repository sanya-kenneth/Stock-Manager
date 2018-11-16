from flask import current_app as app
from app.auth.database import db_handler



#Store attendant class model
class User:
    def __init__(self,username,email,password,admin_status=False):
        """
        Class for creating the store attendant object

        :params user_name, email, user_password:
        """
        self.username = username
        self.email = email
        self.password = password
        self.admin_status = admin_status
    
    def insert_user(self):
        sql = ("""INSERT INTO user_table(username, useremail, userpassword,adminstatus) VALUES ('{}','{}','{}','{}')""" \
        .format(self.username, self.email, self.password, self.admin_status))
        db_handler().cursor.execute(sql)
        return True