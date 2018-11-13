from tests.base import BaseTest
import json
from app.products import views 
from app.auth import views


class TestSales(BaseTest):
    def test_validation_on_create_sale_endpoint(self):
        # views.user_db.append({'user_name':'sanya',
        #                     'user_password':'123',
        #                     'admin_status':False,
        #                     'loggedin':True
        #                       })
        res = self.app.post('/api/v1/sales', content_type="text", data=json.dumps(dict(product_name = 'soap',
                                                                                        product_quantity = 2)))

        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = '',
                                                                                        product_quantity = 2)))
        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                        product_quantity = '')))
        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                        product_quantity = 'one')))
        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'so ap',
                                                                                        product_quantity = 2 )))
        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                        product_quantity = 0 )))
        self.assertEqual(res.status_code,400)

        # views.product_db = []

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                        product_quantity = 10 )))
        self.assertEqual(res.status_code,404)

        # product_db.append( {'product_name':'soap',
        #                     'product_price':2000,
        #                     'product_quantity':8 })

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'sugar',
                                                                                        product_quantity = 10 )))
        self.assertEqual(res.status_code,404)

        res = self.app.post('/api/v1/sales', content_type="application/json", data=json.dumps(dict(product_name = 'soap',
                                                                                        product_quantity = 13 )))
        self.assertEqual(res.status_code,400)
        