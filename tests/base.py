import unittest
from app.auth.models import User
from app.auth.database import Database
from app.products.models import Product
from app.sales.models import Sale
from  app import create_app
import datetime
import json



class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        self.app = create_app("Testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = Database(self.app.config['DATABASE_URI'])
        self.db.create_tables()
        self.app = self.app.test_client()
        # self.app.config['SECRET']
        # self.app.config['DATABASE_URI'] = 'postgres://postgres:psql@localhost:5432/test_store'
        # self.user = User('ken','sanyakenneth@gmail.com','123')
        # self.product = Product('soap',2,3000,'white star')
        # self.sale = Sale('1215','Len','soap',3,4000,12000,datetime.datetime.utcnow())

    
    def tearDown(self):
       self.db.drop_tables()
       self.db.remove_user('glen')

    def get_token_admin(self):
        user = {  
                "email":"ben@gmail.com",
                "password":"ben"
                }
        res = self.app.post('/api/v1/users/login',data=json.dumps(user))
        data = json.loads(res.data.decode())
        return data['token']

    def get_token_user(self):
        user = {  
                "email":"sanya@gmail.com",
                "password":"sanya"
                }
        res = self.app.post('/api/v1/users/login',data=json.dumps(user))
        data = json.loads(res.data.decode())
        # print(data['message'])
        return data['token']

   





    

    
    
if __name__ == '__main__':
    unittest.main()