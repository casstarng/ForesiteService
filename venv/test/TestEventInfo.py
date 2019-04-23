import EventInfo
from Main import app
from flask import request, jsonify, json
import unittest

detailedID = ''

class AccountTests(unittest.TestCase):
    def test_createEvent(self):
        global detailedID

        query = {
            'user_name': 'test',
            'title': 'test'
        }

        response = app.test_client().post(
            'foresite/createEvent',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))
        detailedID = data['event_id']
        self.assertEqual(data['response'], 'success')

    def test_createEvent_fail(self):
        global detailedID

        query = {
            'title': 'test'
        }

        response = app.test_client().post(
            'foresite/createEvent',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['response'], 'fail')

    def test_getEventList(self):
        query = {}

        response = app.test_client().post(
            'foresite/getEventList',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['response'], 'success')

    def test_getEventDetails(self):
        query = {
            'event_id': detailedID
        }

        response = app.test_client().post(
            'foresite/getEventDetails',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['response'], 'success')

    def test_getEventDetails_fail(self):
        query = {
            'event_id': '12312312'
        }

        response = app.test_client().post(
            'foresite/getEventDetails',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['response'], 'fail')

    def test_signUp(self):
        global detailedID
        query = {
            'event_id': detailedID,
            'user_name': 'test'
        }

        response = app.test_client().post(
            'foresite/signUp',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['response'], 'success')

    def test_signUp_fail(self):
        global detailedID
        query = {
            'user_name': 'test'
        }

        response = app.test_client().post(
            'foresite/signUp',
            data=json.dumps(query),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data['response'], 'fail')

if __name__ == '__main__':
    unittest.main()