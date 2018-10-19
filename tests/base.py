import unittest
from app.auth.models import User,Admin
from app.products.models import Product
from app.sales.models import Sale
from app.auth.views import user_db
from app.products.views import product_db
from  app import create_app
# from flask import current_app
import datetime



class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        config_name = "Testing"
        self.app = create_app(config_name)
        self.app = self.app.test_client()
        self.user = User('ken','123')
        self.admin = Admin('sanya','2018')
        self.product = Product('soap',2,3000,'white star')
        self.sale = Sale('1215','Len','soap',3,4000,12000,datetime.datetime.utcnow())

    def tearDown(self):
        user_db.clear()
        product_db.clear()


    

    
    
if __name__ == '__main__':
    unittest.main()

   

