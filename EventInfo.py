from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
import datetime
import pymongo
import copy
from NBPattern import prediction

app = Flask(__name__)
CORS(app)

bp = Blueprint('eventInfo', __name__)

#client = pymongo.MongoClient("mongodb://admin:foresiteadmin@54.218.76.138/foresite")  # defaults to port 27017
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.foresite

@bp.route('/foresite/getEventList', methods=['POST'])
def getEventList():
    # Find with query
    cursor = db.event.find().limit(10)

    results = list(cursor)

    final_res = []

    # Converts ObjectId to string
    for r in results:
        tempobj = {
            '_id':  str(r['_id']),
            'event_id': r['event_id'],
            'thumbnail_icon': r['thumbnail_icon'],
            'title': r['title'],
            'street': r['street'],
            'city': r['city'],
            'state': r['state'],
            'zip_code': r['zip_code'],
            'start_time': r['start_time'],
            'end_time': r['end_time'],
            'start_date': r['start_date'],
            'end_date': r['end_date'],
            'is_tbd': r['is_tbd'],
            'subtotal_price': r['subtotal_price'],
            'add_ons': r['add_ons'],
            'survey_questions': r['survey_questions'],
            'event_tickets': r['event_tickets'],
            'creation_date': r['creation_date'],
            'last_updated': r['last_updated']
        }
        final_res.append(tempobj)

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'results': final_res}), 201

@bp.route('/foresite/getEventDetails', methods=['POST'])
def getEventDetails():
    # Check if event_id present in request
    if not request.json or not 'event_id' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'event_id not present'}), 201
    query = {
        'event_id': request.json['event_id']
    }

    # Find with query
    cursor = db.event.find(query)
    results = list(cursor)
    
    # Converts ObjectId to string
    for r in results:
        r['_id'] = str(r['_id'])

    if (len(results) == 1):
        return jsonify({'response': 'success',
                        'message': 'Query Success',
                        'results': results[0]}), 201
    else:
        return jsonify({'response': 'fail',
                        'message': 'Event ID does not exist'}), 201

@bp.route('/foresite/createEvent', methods=['POST'])
def createEvent():
    # Check if user
    if not request.json or not 'user_name' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'user_name not present'}), 201

    survey_prediction = []
    if 'survey_questions' in request.json:
        survey_prediction = copy.deepcopy(request.json['survey_questions'])
        for survey in survey_prediction:
            if survey['type'] == 'singleChoice' or survey['type'] == 'multipleChoice':
                new_answers = []
                for a in survey['answers']:
                    new_answers.append({a: 0})
                survey['answers'] = new_answers
            elif survey['type'] == 'freeResponse':
                survey['answers'] = []

    add_ons = []
    if 'add_ons' in request.json:
        add_ons = request.json['add_ons'].copy()
        for adds in add_ons:
            adds['quantity'] = 0

    query = {
        'event_id': request.json['event_id'] if 'event_id' in request.json else 'TEMP',
        'user_name': request.json['user_name'] if 'user_name' in request.json else '',
        'thumbnail_icon': request.json['thumbnail_icon'] if 'thumbnail_icon' in request.json else '',
        'title': request.json['title'] if 'title' in request.json else '',
        'street': request.json['street'] if 'street' in request.json else '',
        'city': request.json['city'] if 'city' in request.json else '',
        'state': request.json['state'] if 'state' in request.json else '',
        'zip_code': request.json['zip_code'] if 'zip_code' in request.json else '',
        'start_time': request.json['start_time'] if 'start_time' in request.json else '',
        'start_date': request.json['start_date'] if 'start_date' in request.json else '',
        'end_time': request.json['end_time'] if 'end_time' in request.json else '',
        'end_date': request.json['end_date'] if 'end_date' in request.json else '',
        'is_tbd': request.json['is_tbd'] if 'is_tbd' in request.json else 0,
        'category': request.json['category'] if 'category' in request.json else '',
        'description': request.json['description'] if 'description' in request.json else '',
        'max_purchase_quantity': request.json['max_purchase_quantity'] if 'max_purchase_quantity' in request.json else 0,
        'max_quantity_available': request.json['max_quantity_available'] if 'max_quantity_available' in request.json else 0,
        'subtotal_price': request.json['subtotal_price'] if 'subtotal_price' in request.json else 0,
        'add_ons': add_ons,
        'survey_questions': request.json['survey_questions'] if 'survey_questions' in request.json else {},
        'event_tickets': request.json['event_tickets'] if 'event_tickets' in request.json else [],
        'attendance_prediction': 0,
        'survey_prediction': survey_prediction,
        'creation_date': datetime.datetime.now(),
        'last_updated': datetime.datetime.now()

    }

    db.event.insert_one(query)

    result = db.event.find_one({'event_id': 'TEMP'})

    new_id = str(result['_id'])
    db.event.update({'event_id': 'TEMP'}, {'$set': {'event_id': str(result['_id'])}})

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'event_id': new_id}), 201


@bp.route('/foresite/signUp', methods=['POST'])
def signUp():
    # Check if event_id present in request
    if not request.json or not 'event_id' in request.json or not 'user_name' in request.json or not 'amount_bought' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'event_id or user_name not present'}), 201

    # Add onto event
    query = {
        'event_id': request.json['event_id']
    }

    event = db.event.find_one(query)

    # Create new Ticket
    query = {
        'ticket_id': request.json['ticket_id'] if 'ticket_id' in request.json else 'TEMP',
        'user_name': request.json['user_name'] if 'user_name' in request.json else '',
        'amount_bought': request.json['amount_bought'],
        'title': event['title'],
        'event_id': request.json['event_id'],
        'qr_code': request.json['qr_code'] if 'qr_code' in request.json else 'QR Code placeholder',
        'is_ticket_redeemed': 0,
        'add_ons': request.json['add_ons'] if 'add_ons' in request.json else [],
        'survey_questions': request.json['survey_questions'] if 'survey_questions' in request.json else {},
        'creation_date': datetime.datetime.now()
    }

    db.ticket.insert_one(query)
    ticket = db.ticket.find_one({'ticket_id': 'TEMP'})
    ticket_id = str(ticket['_id'])
    db.ticket.update({'ticket_id': 'TEMP'}, {'$set': {'ticket_id': str(ticket['_id'])}})

    # Add onto user event_tickets
    query = {
        'user_name': request.json['user_name']
    }

    user = db.user.find_one(query)
    event_tickets = user['event_tickets']
    event_tickets.append(ticket_id)

    db.user.update({'user_name': request.json['user_name']}, {'$set': {'event_tickets': event_tickets}})

    # Add onto event
    query = {
        'event_id': request.json['event_id']
    }

    event = db.event.find_one(query)
    event_tickets = event['event_tickets']
    event_tickets.append(ticket_id)

    db.event.update({'event_id': request.json['event_id']}, {'$set': {'event_tickets': event_tickets}})

    # Machine Learning Prediction
    # print(user['attendance_history'])
    history = user['attendance_history']
    if len(history) > 0:
        will_attend = prediction(user['attendance_history'])
        if will_attend >= 0.5:
            num = event['attendance_prediction'] + request.json['amount_bought']
            survey_prediction = event['survey_prediction']
            add_ons = event['add_ons']
            for survey in survey_prediction:
                if survey['type'] == 'singleChoice' or survey['type'] == 'multipleChoice':
                    answers = survey['answers']
                    # for k, v in answers.items():
                    #     answers[k] = v + findPredictionVal(request.json['survey_questions'], survey['question'], k)
                    for a in survey['answers']:
                        for key in a:
                            a[key] = a[key] + findPredictionVal(request.json['survey_questions'], survey['question'], key)
                elif survey['type'] == 'freeResponse':
                    newRes = findPredictionVal(request.json['survey_questions'], survey['question'], "")
                    merged = survey['answers'] + newRes
                    survey['answers'] = merged
            for adds in add_ons:
                newCount = findAddOns(request.json['add_ons'], adds['name'])
                adds['quantity'] = adds['quantity'] + newCount
            db.event.update({'event_id': request.json['event_id']}, {'$set': {'attendance_prediction': num, 'survey_prediction': survey_prediction, 'add_ons': add_ons}})


    return jsonify({'response': 'success',
                    'message': 'Sign Up Success',
                    'ticket_id': ticket_id}
                   ), 201


def findAddOns(add_ons, name):
    for adds in add_ons:
        if adds['name'] == name:
            return int(adds['quantity'])
    return 0


def findPredictionVal(event, question, answer):
    for survey in event:
        if survey['question'] == question:
            if survey['type'] == 'freeResponse':
                answers = survey['answers']
                res = []
                for a in answers:
                    res.append(a)
                return res
            else:
                answers = survey['answers']
                for k, v in answers.items():
                    if k == answer:
                        return int(v)


