import Login
from Main import app
from flask import request, jsonify, json
import unittest

class AccountTests(unittest.TestCase):
    def test_createUser(self):
        query = {
            'first_name':  'test',
            'last_name': 'test',
            'email': 'test',
            'phone_number': 'test',
            'user_name': 'test',
            'password': 'test'
        }

        response = app.test_client().post(
            '/foresite/createUser',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'success')

    def test_createUser_fail(self):
        query = {
            'first_name':  'test',
            'last_name': 'test',
            'email': 'test',
            'phone_number': 'test',
            'user_name': 'test',
            'password': 'test'
        }

        response = app.test_client().post(
            '/foresite/createUser',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'fail')


    def test_login(self):
        response = app.test_client().post(
            '/foresite/login',
            data = json.dumps({'user_name': 'test', 'password': 'test'}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'success')

    def test_login_fail(self):
        response = app.test_client().post(
            '/foresite/login',
            data=json.dumps({'user_name': 'test', 'password': 'tesssst'}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'fail')

    def test_getUserDetails(self):
        response = app.test_client().post(
            '/foresite/getUserDetails',
            data = json.dumps({'user_name': 'test'}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'success')

    def test_getUserDetails_fail(self):
        response = app.test_client().post(
            '/foresite/getUserDetails',
            data=json.dumps({'user_name': 'test12345'}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'fail')

    def test_editUserDetails(self):
        response = app.test_client().post(
            '/foresite/editUserDetails',
            data=json.dumps({'user_name': 'test', 'first_name': 'testest'}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'success')

    def test_editUserDetails_fail(self):
        response = app.test_client().post(
            '/foresite/editUserDetails',
            data=json.dumps({'first_name': 'testest'}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], 'fail')

if __name__ == '__main__':
    unittest.main()