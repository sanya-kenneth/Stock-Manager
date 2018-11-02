from tests.base import BaseTest
import json
from app.products import views 
from app.auth import views



class ProductTestCase(BaseTest):
    def test_returns_error_if_content_type_is_not_application_json(self):
        res = self.app.post('/api/v1/products', content_type="text", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_user_is_not_admin(self):                                                    
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_user()})
        self.assertEqual(res.status_code,401) 

    def test_returns_error_if_product_name_quantity_price_description_is_empty(self):
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = '',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= "",
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = "",
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = '')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 

    def test_product_name_has_white_space(self):        
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soa p',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_price_or_quantity_are_not_of_type_int(self):
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 'two',
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = '2000',
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_price_or_quantity_less_than_one(self):
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 0,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 0,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400) 


    def test_creates_product(self):
        res = self.app.post('/api/v1/products', data=json.dumps(dict(product_name = 'soap', product_quantity= 10, product_price = 2000,product_description = 'good soap')), content_type='application/json', headers = {'token':self.get_token_admin()} )
        self.assertIn('Product created',str(res.data))
        self.assertEqual(res.status_code,201) 

    def test_gets_all_products(self):
        res = self.app.get('/api/v1/products', headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,200) 

    def test_returns_error_if_product_ids_dont_match(self):
        res = self.app.get('/api/v1/products/200', headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,404) 

    def test_returns_product_if_ids_match(self):
        res = self.app.get('/api/v1/products/5',headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,200) 
