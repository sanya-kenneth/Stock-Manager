from app.auth.database import Database
from flask import current_app as app



#Store attendant class model
class User(Database):
    def __init__(self,username,email,password,admin_status=False):
        Database.__init__(self,app.config['DATABASE_URI'])

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
        self.cursor.execute(sql)
        return True