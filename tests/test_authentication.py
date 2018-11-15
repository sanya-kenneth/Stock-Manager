from tests.base import BaseTest
from app.auth import views
import json


class AuthTestCase(BaseTest):   
    def test_returns_error_if_request_content_type_is_not_application_json(self):
        """ Method checks if the create attendant endpoint returns an error 
            if the request.content-type is not application/json """

        res = self.app.post('/api/v1/users', content_type="text", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_email = 'sanya@gmail.com',
                                                                                        user_password = '124')), headers = {'token':self.get_token_admin()})

        self.assertEqual(res.status_code,400)
        self.assertIn('Wrong content-type', str(res.data))

    def  test_returns_error_if_user_attempts_to_signup_with_one_of_the_fields_empty(self):
        """ Method checks if the create attendant endpoint returns an error 
            if the email field, name field or password field is empty """
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = '',
                                                                                        user_email = 'sanya@gmail.com',
                                                                                        user_password = '124')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400)
        self.assertIn('username,email or password cannot be empty', str(res.data))

        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_email = '',
                                                                                        user_password = '124')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400)
        self.assertIn('username,email or password cannot be empty', str(res.data))

        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_email = 'sanya@gmail.com',
                                                                                        user_password = '')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400)
        self.assertIn('username,email or password cannot be empty', str(res.data))

    def test_returns_error_if_username_has_white_space(self):
        """ Method tests if signup/login endpoint returns an error if a user inputs a username with white spaces"""
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'ke nss',
                                                                                        user_email = 'ken@gmail.com',
                                                                                        user_password = '23232')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 
        self.assertIn('Username cannot contain spaces', str(res.data))

    def test_returns_error_if_username_is_not_a_string(self):
        """ Method tests if signup endpoints return an error is username is not of type string"""
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 44,
                                                                                        user_email = 'ken@gmail.com',
                                                                                        user_password = '23232')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400) 
        self.assertIn('username or email must be a string', str(res.data))

    def test_creates_new_store_attendant_account(self):
        """ Method tests if a new store attendant can be added """
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'glen',
                                                                                         user_email = 'glen@gmail.com',
                                                                                        user_password = '23232')),  headers = {'token':self.get_token_admin()})
        self.assertIn('Store attendant was successfully registered',str(res.data)) 
        self.assertEqual(res.status_code,201)


    def test_returns_error_if_user_tries_to_create_an_account_that_already_exists(self):
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(dict(user_name = 'sanya',
                                                                                        user_email = 'sanya@gmail.com',
                                                                                        user_password = 'sanya')), headers = {'token':self.get_token_admin()})
        self.assertEqual(res.status_code,400)
        self.assertIn('user already exists',str(res.data))

        
    def test_login_returns_error_if_user_email_or_password_is_empty(self):
        """ Method tests if login endpoint returns an error if the useremail or password is empty"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(email = '',
                                                                                        password = 'sanya')))
        self.assertEqual(res.status_code,400) 
        self.assertIn('useremail or password cannot be empty', str(res.data))

        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(email = 'sanya@gmail.com',
                                                                                        password = '')))
        self.assertEqual(res.status_code,400) 
        self.assertIn('useremail or password cannot be empty', str(res.data))
# 
    def test_login_returns_error_if_useremail_is_not_a_string(self):
        """ Method tests if login endpoint returns an error if the useremail is not a string"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(email = 222,
                                                                                        password = 'sanya')))
        self.assertEqual(res.status_code,400) 
        self.assertIn('useremail must be a string', str(res.data))

    def test_login_returns_error_if_useremail_has_white_space(self):
        """ Methods tests if login endpoint returns an error if the useremail has white spaces"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(email = 'sanya kenneth@gmail.com',
                                                                                        password = 'sanya')))
        self.assertEqual(res.status_code,400) 
        self.assertIn('Invalid email', str(res.data))

    def test_login_returns_error_if_useremail_or_password_are_incorrect(self):
        """ Method tests if login endpoint returns an error if the useremail or password are incorrect"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(email = 'ssaa@gmail.com',
                                                                                        password = 'sanya')))
        self.assertEqual(res.status_code,400) 
        self.assertIn('Wrong useremail or password',str(res.data))

    def test_login_signs_in_a_user(self):
        """ Method tests if login endpoint can signin a user"""
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(dict(email = 'sanya@gmail.com',
                                                                                        password = 'sanya')))
        dataset = json.loads(res.data.decode())
        self.assertEqual(res.status_code,200) 
        self.assertEqual(dataset['message'], 'You are now loggedin')