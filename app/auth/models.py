import uuid
from werkzeug.security import generate_password_hash,check_password_hash


class User(object):
    def __init__(self,username,password,admin_status=False):
        self.user_id = uuid.uuid1()
        self.username = username
        self.password = generate_password_hash(password,method='sha256')
        self.admin_status = admin_status

    def to_dict(self):
        return dict(
                user_id = self.user_id.int,
                user_name = self.username,
                user_password = self.password,
                admin_status = self.admin_status
        )

class Admin(User):
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.username = args[0]
        self.password = generate_password_hash(args[1], method='sha256')
        self.admin_status = True

