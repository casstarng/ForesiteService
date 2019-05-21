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

@bp.route('/foresite/getUserTickets', methods=['POST'])
def getUserTickets():
    # Check if user_name is present in request
    if not request.json or not 'user_name' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'User name is not present'}), 201
    query = {
        'user_name': request.json['user_name']
    }

    # Find with query
    cursor = db.ticket.find(query)

    results = list(cursor)

    listOfTickets = []

    # Converts ObjectId to string
    for r in results:
        tempObj = {
            'ticket_id': r['ticket_id'],
            'title': r['title'],
            'thumbnail_icon': r['thumbnail_icon'],
            'street': r['street'],
            'city': r['city'],
            'state': r['state'],
            'zip_code': r['zip_code'],
            'start_time': r['start_time'],
            'start_date': r['start_date'],
            'end_time': r['end_time'],
            'end_date': r['end_date'],
            'creation_date': r['creation_date']
        }
        listOfTickets.append(tempObj)

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'results': listOfTickets}), 201