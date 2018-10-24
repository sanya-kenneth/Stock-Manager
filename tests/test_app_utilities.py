from tests.base import BaseTest
from app.auth.utility import login_required,admin_required
from app.products import views
from app.auth.views import user_db,admin_db




class AppUtilityTests(BaseTest):
    def test_login_required_returns_error_user_is_not_logged_in(self):
        """ Methods tests if login_required function returns an error if a user accesses an endpoint without loggin in first"""
        user_db.append(dict(   user_id = '1102',
                user_name = 'sanya',
                user_password = 'wedq',
                admin_status = False,
                loggedin = False
                        ))

        res = self.app.get('/api/v1/products')
        self.assertEqual(res.status_code,401)
        self.assertIn('You are not logged in',str(res.data))

    def test_admin_required_rejects_user_if_user_is_not_an_admin(self):
        """ Methods tests if the admin_required function denies a user access to an endpoint if they are not an admin"""
        admin_db.append(dict(   user_id = '1102',
                user_name = 'sanya',
                user_password = 'wedq',
                admin_status = False,
                loggedin = False
                        ))
        
        self.assertEqual(admin_required(),False)
        

    

        


