# from tests.base import BaseTest
# from app.sales.views import *





# class AppUtilityTests(BaseTest):
    # def test_login_required_returns_error_user_is_not_logged_in(self):
    #     """ Methods tests if login_required function returns an error if a user accesses an endpoint without loggin in first"""
    #     payload = dict(   user_id = '1102',
    #             user_name = 'sanya',
    #             user_password = 'wedq',
    #             admin_status = False,
    #             loggedin = False
    #                     )
    #     product = {
    #                 'product_name':'soap',
    #                 'product_quantity':2
    #               }

    #     res = self.app.post('/api/v1/sales',content_type = 'application/json', data = json.dumps(product))
    #     self.assertIn('You are not logged in',str(res.data))
    #     self.assertEqual(res.status_code,401)
       

    # def test_admin_required_rejects_user_if_user_is_not_an_admin(self):
    #     """ Methods tests if the admin_required function denies a user access to an endpoint if they are not an admin"""
    #     admin_db.append(dict(   user_id = '1102',
    #             user_name = 'sanya',
    #             user_password = 'wedq',
    #             admin_status = False,
    #             loggedin = False
    #                     ))
        
    #     self.assertEqual(admin_required(),False)
        

    

        


