from tests.base import BaseTest
from app.auth import views
import json


class AuthTestCase(BaseTest):   
    def test_returns_error_if_request_content_type_is_not_application_json(self):
        """ Method checks if the create attendant and create admin endpoints return an error 
            if the request.content-type is not application/json """
        res = self.app.post('/api/v1/users', content_type="text", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '124')))

        self.assertEqual(res.status_code,400)
        self.assertIn('Wrong content-type', str(res.data))

        res = self.app.post('/api/v1/users/admin', content_type="text", data=json.dumps(dict(admin_name = 'sanya',
                                                                                        admin_password = '124')))

        self.assertEqual(res.status_code,400)
        self.assertIn('Wrong content-type', str(res.data))

    def  test_returns_error_if_user_attempts_to_signup_with_one_of_the_fields_empty(self):
        """ Method checks if the create attendant and create admin endpoints return an error 
            if the name field or password field is empty """
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = '',
                                                                                        user_password = '124')))
        self.assertEqual(res.status_code,400)
        
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '')))
        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = '',
                                                                                        admin_password = '1234')))
        self.assertEqual(res.status_code,400)

        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'ken',
                                                                                        admin_password = '')))
        self.assertEqual(res.status_code,400)

    def test_returns_error_if_username_has_white_space(self):
        """ Method tests if signup end points return an error if a user inputs a username with white spaces"""
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'ke nss',
                                                                                        user_password = '23232')))
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'zidane ',
                                                                                        admin_password = '23232')))
        self.assertEqual(res.status_code,400) 

    def test_returns_error_if_username_is_not_a_string(self):
        """ Method tests if signup endpoints return an error is username is not of type string"""
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 44,
                                                                                        user_password = '23232')))
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 44,
                                                                                        admin_password = '23232')))
        self.assertEqual(res.status_code,400) 

    def test_creates_new_store_attendant_account(self):
        """ Method tests if a new store attendant can be added """
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '23232')))
        self.assertEqual(res.status_code,201)

    def test_creates_admin_account(self):
        """ Method tests if a new admin account can be created""" 
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'admin',
                                                                                        admin_password = 'admin123')))
        self.assertEqual(res.status_code,201) 

    def test_returns_error_if_user_tries_to_create_an_account_that_already_exists(self):
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '23232')))
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '23232')))
        self.assertEqual(res.status_code,400)
        self.assertIn(':( BAD REQUEST',str(res.data))

    def test_returns_error_admin_tries_to_create_an_existing_admin_account(self):
        self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'admin',
                                                                                        admin_password = 'admin123')))
        res = self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(dict(admin_name = 'admin',
                                                                                        admin_password = 'admin123')))
        self.assertEqual(res.status_code,400)
        self.assertIn(':( BAD REQUEST',str(res.data))
        
        
    def test_login_returns_error_if_user_name_or_password_is_empty(self):
        """ Method tests if login endpoint returns an error if the username or password is empty"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = '',
                                                                                        password = '23232')))
        self.assertEqual(res.status_code,400) 

        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '')))
        self.assertEqual(res.status_code,400) 

    def test_login_returns_error_if_username_is_not_a_string(self):
        """ Method tests if login endpoint returns an error if the username is not a string"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 222,
                                                                                        password = 'sss')))
        self.assertEqual(res.status_code,400) 

    def test_login_returns_error_if_username_has_white_space(self):
        """ Methods tests if login endpoint returns an error if the username has white spaces"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'ss aa ',
                                                                                        password = 'ssss')))
        self.assertEqual(res.status_code,400) 

    def test_login_returns_error_if_username_or_password_are_incorrect(self):
        """ Method tests if login endpoint returns an error if the username or password are incorrect"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'ssaa',
                                                                                        password = 'ssss')))
        self.assertEqual(res.status_code,400) 
        self.assertIn('Wrong username or password',str(res.data))

    def test_login_signs_in_a_user(self):
        """ Method tests if login endpoint can signin a user"""
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_password = '23232')))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(name = 'sanya',
                                                                                        password = '23232')))
        self.assertEqual(res.status_code,200) 
        





        

        





        
        
