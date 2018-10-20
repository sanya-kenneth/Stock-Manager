from tests.base import BaseTest
import json
from app.products import views 
from app.products.views import product_db
from app.auth import views



class ProductTestCase(BaseTest):
    def test_returns_error_if_content_type_is_not_application_json(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))
        res = self.app.post('/api/v1/products', content_type="text", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))
        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_user_is_not_admin(self):
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))
                                                    
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))
        self.assertEqual(res.status_code,401) 

    def test_returns_error_if_product_name_quantity_price_description_is_empty(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = '',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= "",
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = "",
                                                                                                        product_description = 'good soap')))
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = '')))
        self.assertEqual(res.status_code,400) 

    def test_product_name_has_white_space(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soa p',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_price_or_quantity_are_not_of_type_int(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 'two',
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = '2000',
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_price_or_quantity_less_than_one(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 0,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 0,
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,400) 

    def test_updates_product(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,201) 

    def test_creates_product(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        self.assertEqual(res.status_code,201) 

    def test_returns_error_if_there_are_no_products(self):
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.get('/api/v1/products')
        self.assertEqual(res.status_code,404) 

    def test_gets_all_products(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')))

        res = self.app.get('/api/v1/products')
        self.assertEqual(res.status_code,200) 

    def test_returns_error_if_there_are_no_products_in_db(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))

        res = self.app.get('/api/v1/products/1')
        self.assertEqual(res.status_code,404) 

    def test_returns_error_if_product_ids_dont_match(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))
        product_db.append(dict(product_name = 'soap',product_quantity= 10,product_price = 2000,product_description = 'good soap',product_id = 1))

        res = self.app.get('/api/v1/products/2')
        self.assertEqual(res.status_code,404) 

    def test_returns_product_if_ids_match(self):
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))
        product_db.append(dict(product_name = 'soap',product_quantity= 10,product_price = 2000,product_description = 'good soap',product_id = 1))

        res = self.app.get('/api/v1/products/1')
        self.assertEqual(res.status_code,404) 



        







    
