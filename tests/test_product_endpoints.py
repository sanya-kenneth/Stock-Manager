from tests.base import BaseTest
import json
from app.products import views 
from app.products.views import products_list
from app.auth import views


class ProductTestCase(BaseTest):
    def test_returns_error_if_content_type_is_not_application_json(self):
        res = self.app.post('/api/v1/products', content_type="text", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 
        self.assertIn('Wrong content-type', str(res.data))

    def test_returns_error_if_user_is_not_admin(self):                                                    
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_user()})
        self.assertEqual(res.status_code,401) 
        self.assertIn('Access Denied. Please login as admin', str(res.data))

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
        self.assertIn('poductname cannot contain spaces', str(res.data))

    def test_returns_error_if_price_or_quantity_are_not_of_type_int(self):
        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 'two',
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400) 
        self.assertIn('price or quantity must be a number and must be greater than 1', str(res.data))

        res = self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 2,
                                                                                                        product_price = '2000',
                                                                                                        product_description = 'good soap')), headers = {'token':self.get_token_admin()})
        self.assertIn('price or quantity must be a number and must be greater than 1', str(res.data))
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

    def test_updates_product(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.put('/api/v1/products/1', content_type="application/json", data=json.dumps(dict(productname = 'wash',
                                                                                                        productquantity= 10,
                                                                                                        productprice = 2000,
                                                                                                        productdescription = 'good soap')), headers = {'token':self.get_token_admin()})

        dataset = json.loads(res.data.decode())
        self.assertEqual(dataset['message'], 'Product successfully updated')
        self.assertIsInstance(dataset['Product'], dict)
        self.assertEqual(res.status_code,201) 

    def test_creates_product(self):
        res = self.app.post('/api/v1/products', data=json.dumps(dict(product_name = 'geisha', product_quantity= 10, product_price = 2000,product_description = 'soap')), content_type='application/json', headers = {'token':self.get_token_admin()} )
        dataset = json.loads(res.data.decode())
        self.assertIn('Product created',str(res.data))
        self.assertTrue(dataset['status'], 'Product created')
        self.assertEqual(res.status_code,201) 

    def test_returns_error_if_there_are_no_products(self):
        res = self.app.get('/api/v1/products', headers = {'token':self.get_token_admin()})
        dataset = json.loads(res.data.decode())
        self.assertTrue(dataset['message'],'There no products at the moment')
        self.assertEqual(res.status_code,404) 


    def test_gets_all_products(self):                   
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})
                                                                          

        res = self.app.get('/api/v1/products', headers = {'token':self.get_token_admin()})
        dataset = json.loads(res.data.decode())
        self.assertIsInstance(dataset['Products'], list)
        self.assertIsInstance(products_list[0], dict)
        self.assertEqual(res.status_code,200) 

    def test_returns_error_if_there_are_no_products_in_db(self):
        res = self.app.get('/api/v1/products', headers = {'token':self.get_token_admin()})
        dataset = json.loads(res.data.decode())
        self.assertEqual(dataset['message'], 'There no products at the moment')
        self.assertEqual(res.status_code,404) 

    def test_returns_error_if_product_ids_dont_match(self):
        res = self.app.get('/api/v1/products/200', headers = {'token':self.get_token_admin()})
        dataset = json.loads(res.data.decode())
        self.assertTrue(dataset['message'], 'Product was not found')
        self.assertEqual(res.status_code,404) 

    def test_returns_product_if_ids_match(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        
        res = self.app.get('/api/v1/products/1',headers = {'token':self.get_token_admin()})
        dataset = json.loads(res.data.decode())
        self.assertIsInstance(dataset['Product'], dict)
        self.assertEqual(res.status_code,200) 

    def test_can_delete_a_product(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.delete('/api/v1/products/1',headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status, '200 OK')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Product was deleted successfuly', str(res.data))

    def test_returns_error_if_non_admin_tries_to_delete_a_product(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.delete('/api/v1/products/1',headers = {'token':self.get_token_user()})
        self.assertEqual(res.status_code, 401)
        self.assertIn('Access Denied. Please login as admin', str(res.data))

    def test_returns_error_if_user_tries_to_delete_a_product_that_does_not_exist(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.delete('/api/v1/products/4',headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code, 404)
        self.assertIn('Product not found', str(res.data))

    def test_returns_error_if_method_is_wrong(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})
        
        res = self.app.post('/api/v1/products/1',headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code, 405)
        self.assertIn(' :( Oops Method Not Allowed', str(res.data))




