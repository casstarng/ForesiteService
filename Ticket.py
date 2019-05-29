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
            'amount_bought': r['amount_bought'],
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

@bp.route('/foresite/redeemTickets', methods=['POST'])
def redeemTickets():
    # Check if ticket_id is present in request
    if not request.json or not 'ticket_id' in request.json or not 'tickets_redeemed' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'Ticket_id is not present'}), 201
    query = {
        'ticket_id': request.json['ticket_id']
    }

    # Find with query
    result = db.ticket.find_one(query)

    # Converts ObjectId to string
    result['_id'] = str(result['_id'])
    event_id = result['event_id']
    amount_bought = result['amount_bought']
    tickets_redeemed = result['tickets_redeemed']
    if tickets_redeemed + request.json['tickets_redeemed'] > amount_bought:
        return jsonify({'response': 'error',
                        'message': 'Invalid redemption amount'}), 201

    db.ticket.update({'ticket_id': request.json['ticket_id']}, {'$set': {'tickets_redeemed': result['tickets_redeemed'] + request.json['tickets_redeemed']}})

    query = {
        'event_id': event_id
    }

    event_result = db.event.find_one(query)

    db.event.update({'event_id': event_id}, {'$set': {'attendance_live': event_result['attendance_live'] + request.json['tickets_redeemed']}})

    return jsonify({'response': 'success',
                    'message': 'Checked in'}), 201

@bp.route('/foresite/redeemAddOns', methods=['POST'])
def redeemAddOns():
    # Check if ticket_id is present in request
    if not request.json or not 'ticket_id' in request.json or not 'add_ons' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'Ticket_id is not present'}), 201
    query = {
        'ticket_id': request.json['ticket_id']
    }

    # Find with query
    ticket_res = db.ticket.find_one(query)
    event_id = ticket_res['event_id']
    res_add_ons = ticket_res['add_ons']

    for add in res_add_ons:
        num = add['quantity'] - findAddOns(request.json['add_ons'], add['name'])
        if num < 0:
            return jsonify({'response': 'error',
                            'message': 'Invalid add-on amount'}), 201
        add['quantity'] = num

    db.ticket.update({'ticket_id': request.json['ticket_id']}, {'$set': {'add_ons': res_add_ons}})

    # event update

    query = {
        'event_id': event_id
    }

    # Find with query
    event_res = db.event.find_one(query)

    event_add_ons = event_res['add_ons_live']

    for add in event_add_ons:
        num = add['quantity'] + findAddOns(request.json['add_ons'], add['name'])
        if num < 0:
            return jsonify({'response': 'error',
                            'message': 'Invalid add-on amount'}), 201
        add['quantity'] = num

    db.event.update({'event_id': event_id}, {'$set': {'add_ons_live': event_add_ons}})

    return jsonify({'response': 'success',
                    'message': 'Add Ons Checked in'}), 201

def findAddOns(request_add_ons, name):
    for adds in request_add_ons:
        if adds['name'] == name:
            return int(adds['quantity'])
    return 0

