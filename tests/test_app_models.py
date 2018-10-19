from app.auth.models import User,Admin
from app.products.models import Product
from app.sales.models import Sale
from tests import BaseTest



class Test_app_models(BaseTest):
    def test_user_object_is_created(self):
        """This method tests if the user object/ store attendant object can be created correctly """
        self.assertIsInstance(self.user,User)

    def test_user_object_returns_data_in_json_format(self):
        """ This tests if the user object returns data in json format"""
        self.assertIsInstance(self.user.to_dict(),dict)

    def test_admin_object_is_created(self):
        """This method tests if the admin object can be created correctly """
        self.assertIsInstance(self.admin,Admin)

    def test_admin_object_returns_data_in_json_format(self):
        """ This tests if the admin object returns data in json format"""
        self.assertIsInstance(self.admin.to_dict(),dict)

    def test_product_object_created(self):
        """This method tests if the product object can be created correctly """
        self.assertIsInstance(self.product,Product)

    def test_product_object_returns_data_in_json_format(self):
        """ This tests if the product object returns data in json format"""
        self.assertIsInstance(self.product.to_dict(),dict)

    def test_sale_object_created(self):
        """This method tests if the sale object can be created correctly """
        self.assertIsInstance(self.sale,Sale)

    def test_sale_object_returns_data_in_json_format(self):
        """ This tests if the sale object returns data in json format"""
        self.assertIsInstance(self.sale.to_dict(),dict)





    
