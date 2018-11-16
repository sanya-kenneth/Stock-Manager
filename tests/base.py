import unittest
from app.auth.models import User
from app.auth.database import Database
from app.products.models import Product
from app.sales.models import Sale
from  app import create_app
import datetime
from werkzeug.security import generate_password_hash
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
        self.db.add_user('ben','ben@gmail.com',generate_password_hash('ben'),True)
        self.db.add_user('sanya','sanya@gmail.com',generate_password_hash('sanya'),False)
      
    def tearDown(self):
       self.db.drop_tables()
       self.db.remove_user('glen')
       self.db.remove_user('ben')
       self.db.remove_user('sanya')

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
        return data['token']

    
    
if __name__ == '__main__':
    unittest.main()