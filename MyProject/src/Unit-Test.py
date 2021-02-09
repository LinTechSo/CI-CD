#!/bin/python3
import app, unittest
class TestHello(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
        
    #get 200 status response from main page
    def test_status1(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')


    #Ensure ok response json behaves correctly given this correct credentials
    def test_ok_response(self):
        rv = self.app.get('/v1/ok')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'{"message":"ok"}\n')

    #Ensure login behaves correctly given this correct credentials
    def test_correct_login(self):
        response = self.app.post(
            '/', 
            data=dict(username="test", password="test"),
            follow_redirects=True
        )
        self.assertIn(b'Welcome back', response.data)

    #Ensure login behaves correctly given this incorrect credentials
    def test_incorrect_login(self):
        response = self.app.post(
            '/', 
            data=dict(username="t", password="t"),
            follow_redirects=True
        )
        self.assertIn(b'Incorrect username or password!', response.data)

    # Ensure logout behaves correctly
    def test_incorrect_login(self):
        response = self.app.post(
            '/', 
            data=dict(username="t", password="t"),
            follow_redirects=True
        )
        self.assertIn(b'Incorrect username or password!', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        self.app.post(
            '/', 
            data=dict(username="test", password="test"),
            follow_redirects=True
        )
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'Logged out', response.data)

    # Ensure that user can register correctly
    def test_user_registration(self):
        response = self.app.post('/register', data=dict(
            username='ali',
            email='ali@gmail.com',
            password='ali',
        ), follow_redirects=True)
        self.assertIn(b'You have successfully registered!', response.data)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()