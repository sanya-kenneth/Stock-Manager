from app.auth.models import User
from app.products.models import Product
from app.sales.models import Sale
from tests.base import BaseTest
# from app.auth.utility import validate_username




class Test_app_models(BaseTest):
    def test_user_object_is_created(self):
        """This method tests if the user object/ store attendant object can be created correctly """
        self.assertIsInstance(self.user,User)

    def test_product_object_created(self):
        """This method tests if the product object can be created correctly """
        self.assertIsInstance(self.product,Product)

    def test_sale_object_created(self):
        """This method tests if the sale object can be created correctly """
        self.assertIsInstance(self.sale,Sale)

