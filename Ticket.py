from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
import pymongo
import datetime

app = Flask(__name__)
CORS(app)

bp = Blueprint('ticket', __name__)

#client = pymongo.MongoClient("mongodb://admin:foresiteadmin@54.218.76.138/foresite")  # defaults to port 27017
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.foresite

@bp.route('/foresite/getTicketDetails', methods=['POST'])
def getTicketDetails():
    # Check if ticket_id is present in request
    if not request.json or not 'ticket_id' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'Ticket_id is not present'}), 201
    query = {
        'ticket_id': request.json['ticket_id']
    }

    # Find with query
    result = db.ticket.find_one(query)

    # Converts ObjectId to string
    result['_id'] = str(result['_id'])

    # If match found, then return success
    if(result != None):
        return jsonify({'response': 'success',
                        'message': 'Query Success',
                        'results': result}), 201
    else:
        return jsonify({'response': 'fail',
                        'message': 'Ticket does not exist'}), 201

@bp.route('/foresite/editUserDetails', methods=['POST'])
def editUserDetails():
    # Check if user_name is present in request
    if not request.json or not 'user_name' in request.json :
        return jsonify({'response': 'fail',
                        'message': 'User name is not present'}), 201
    query = {
        'user_name': request.json['user_name']
    }

    edit_query = {}
    if 'first_name' in request.json:
        edit_query['first_name'] = request.json['first_name']
    if 'last_name' in request.json:
        edit_query['last_name'] = request.json['last_name']
    if 'email' in request.json:
        edit_query['email'] = request.json['email']
    if 'phone_number' in request.json:
        edit_query['phone_number'] = request.json['phone_number']
    if 'password' in request.json:
        edit_query['password'] = request.json['password']

    # Find with query
    db.user.update(query, {'$set': edit_query})

    return jsonify({'response': 'success',
                    'message': 'Edit Success'}), 201

@bp.route('/foresite/getUserCreatedEvents', methods=['POST'])
def getUserCreatedEvents():
    # Check if user_name is present in request
    if not request.json or not 'user_name' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'User name is not present'}), 201
    query = {
        'user_name': request.json['user_name']
    }

    # Find with query
    cursor = db.event.find(query)

    results = list(cursor)

    listOfEvents = []

    # Converts ObjectId to string
    for r in results:
        tempObj = {
            'event_id': r['event_id'],
            'title': r['title']
        }
        listOfEvents.append(tempObj)

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'results': listOfEvents}), 201