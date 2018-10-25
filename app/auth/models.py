import uuid



#Store attendant class model
class User(object):
    def __init__(self,username,password,admin_status=False):
        """
        Class for creating the store attendant object

        :params user_name, user_password:
        """
        self.user_id = uuid.uuid1()
        self.username = username
        self.password = password
        self.admin_status = admin_status
        self.loggedin = False

    def to_dict(self):
        """
        Method converts the User class and Admin class instance variables 
        to a dictionary and returns them
        """
        return dict(
                user_id = str(self.user_id.int)[:5],
                user_name = self.username,
                user_password = self.password,
                admin_status = self.admin_status,
                loggedin = self.loggedin
        )

#Admin/Owner class model
class Admin(User):
    """
    Class for creating the admin object
    Inherits from the User class
    sets admin_status instance variable to True

    :params admin_name, admin_password:
    """
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.user_id = uuid.uuid4()
        self.username = args[0]
        self.password = args[1]
        self.admin_status = True



