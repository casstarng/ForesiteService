import Login
from Main import app
from flask import request, jsonify, json

def login():
    response = app.test_client().post(
        '/foresite/login',
        data = json.dumps({'user_name': 'test', 'password': 'test'}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    print(data)

def createUser():
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

    print(data)

createUser()
login()
