from app.auth.database import Database


#Store attendant class model
class User(Database):
    def __init__(self,username,email,password,admin_status=False):
        Database.__init__(self,'postgres://postgres:psql@localhost:5432/store')
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
        self.c.execute(sql)
        return True
    
    def select_users(self):
        sql = ("""SELECT * from user_table """)
        self.c.execute(sql)
        rows = self.c.fetchall()
        return rows

    def select_a_user(self,user_id_in):
        sql = ("""SELECT * from user_table WHERE userid = {} """.format(user_id_in))
        self.c.execute(sql)
        row = self.c.fetchone()
        return row


