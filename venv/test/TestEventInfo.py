import EventInfo
from Main import app
from flask import request, jsonify, json

detailedID = ''

def createEvent():
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
    print(data)

def getEventList():
    query = {}

    response = app.test_client().post(
        'foresite/getEventList',
        data=json.dumps(query),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    print(data['response'])

def getEventDetails():
    query = {
        'event_id': detailedID
    }

    response = app.test_client().post(
        'foresite/getEventDetails',
        data=json.dumps(query),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    print(data)

def signUp():
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

    print(data)

createEvent()
getEventDetails()
getEventList()
signUp()