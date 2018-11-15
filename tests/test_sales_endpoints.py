from tests.base import BaseTest
import json
from app.products import views 
from app.auth import views


class TestSales(BaseTest):
    def test_creates_sale_endpoint(self):
       
        
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})
        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        # self.assertIn("created",res.data)
        self.assertEqual(res.status_code, 201)

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = '',
        #                                                                                 product_quantity = 2)), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,400)

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
        #                                                                                 product_quantity = '')), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,400)

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
        #                                                                                 product_quantity = 'one')), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,400)

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'so ap',
        #                                                                                 product_quantity = 2 )), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,400)

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
        #                                                                                 product_quantity = 0 )), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,400)

        # views.product_db = []

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
        #                                                                                 product_quantity = 10 )), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,404)

        # product_db.append( {'product_name':'soap',
        #                     'product_price':2000,
        #                     'product_quantity':8 })

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
        #                                                                                 product_quantity = 10 )), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,404)

        # res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
        #                                                                                 product_quantity = 13 )), headers = {'token':self.get_token_user()})
        # self.assertEqual(res.status_code,400)

    def test_gets_all_sales(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        res = self.app.get('/api/v1/sales', headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,200) 

    def test_get_a_sale_by_id(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        res = self.app.get('/api/v1/sales/1', headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,200) 
    
    def test_returns_error_if_content_type_is_not_application_json(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.post('/api/v1/sales', content_type="text", data=json.dumps(dict(product_id = 1,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_product_quantity_is_less_than_1(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 0,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_product_id_is_not_a_number(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = "one",
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_product_id_is_empty(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = "",
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        self.assertEqual(res.status_code,400) 

    # def test_returns_error_if_product_quantity_is_empty(self):
    #     self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
    #                                                                                                     product_quantity= 10,
    #                                                                                                     product_price = 2000,
    #                                                                                                     product_description = 'good soap')),headers = {'token':self.get_token_admin()})

    #     res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
    #                                                                                     product_quantity = "")), headers = {'token':self.get_token_user()})

        
    #     self.assertEqual(res.status_code,400) 

    # def test_returns_error_if_product_quantity_is_not_a_number(self):
    #     self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
    #                                                                                                     product_quantity= 10,
    #                                                                                                     product_price = 2000,
    #                                                                                                     product_description = 'good soap')),headers = {'token':self.get_token_admin()})

    #     res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
    #                                                                                     product_quantity = "two")), headers = {'token':self.get_token_user()})

        
    #     self.assertEqual(res.status_code,400) 

    def test_returns_404_message_if_product_is_not_found(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 10,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        self.assertEqual(res.status_code,404) 

    def test_returns_404_message_if_there_no_products(self):
        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 10,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        self.assertEqual(res.status_code,404) 
    
    def test_returns_error_if_user_is_not_an_admin_on_get_all_sales(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})

        
        res = self.app.get('/api/v1/sales', headers = {'token':self.get_token_user()})
        self.assertEqual(res.status_code,401) 

    def test_returns_error_if_there_no_sales(self):
        # self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
        #                                                                                                 product_quantity= 10,
        #                                                                                                 product_price = 2000,
        #                                                                                                 product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        
        res = self.app.get('/api/v1/sales', headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,404) 

    def test_sale_returns_error_if_a_sale_doesnot_exist(self):
        self.app.post('/api/v1/products', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                                        product_quantity= 10,
                                                                                                        product_price = 2000,
                                                                                                        product_description = 'good soap')),headers = {'token':self.get_token_admin()})

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_id = 1,
                                                                                        product_quantity = 2)), headers = {'token':self.get_token_user()})


        res = self.app.get('/api/v1/sales/90', headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,404) 