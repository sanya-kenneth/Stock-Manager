#Store attendant class model
class User(object):
    def __init__(self,username,email,password,admin_status=False):
        """
        Class for creating the store attendant object

        :params user_name, email, user_password:
        """
        self.username = username
        self.email = email
        self.password = password
        self.admin_status = admin_status

    def to_dict(self):
        """
        Method converts the User class and Admin class instance variables 
        to a dictionary and returns them
        """
        return dict(
                user_name = self.username,
                user_email = self.email,
                user_password = self.password,
                admin_status = self.admin_status,
                )

#Admin/Owner class model
class Admin(User):
    """
    Class for creating the admin object
    Inherits from the User class
    sets admin_status instance variable to True

    :params admin_name, email, admin_password:
    """
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.username = args[0]
        self.email = args[1]
        self.password = args[2]
        self.admin_status = True



