from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
import datetime
import pymongo

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
            'is_tbd': r['is_tbd'],
            'subtotal_price': r['subtotal_price'],
            'add_ons': r['add_ons']
        }
        final_res.append(tempobj)

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'results': str(final_res)}), 201

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
                        'results': str(results[0])}), 201
    else:
        return jsonify({'response': 'fail',
                        'message': 'Event ID does not exist'}), 201

@bp.route('/foresite/createEvent', methods=['POST'])
def createEvent():
    # Check if user
    if not request.json or not 'user_id' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'user_id not present'}), 201

    query = {
        'event_id': request.json['event_id'] if 'event_id' in request.json else '', #TODO
        'user_id': request.json['user_id'] if 'user_id' in request.json else '',
        'thumbnail_icon': request.json['thumbnail_icon'] if 'thumbnail_icon' in request.json else '',
        'title': request.json['title'] if 'title' in request.json else '',
        'street': request.json['street'] if 'street' in request.json else '',
        'city': request.json['city'] if 'city' in request.json else '',
        'state': request.json['state'] if 'state' in request.json else '',
        'zip_code': request.json['zip_code'] if 'zip_code' in request.json else '',
        'start_time': request.json['start_time'] if 'start_time' in request.json else '',
        'end_time': request.json['end_time'] if 'end_time' in request.json else '',
        'is_tbd': request.json['is_tbd'] if 'is_tbd' in request.json else 0,
        'category': request.json['category'] if 'category' in request.json else '',
        'description': request.json['description'] if 'description' in request.json else '',
        'max_purchase_quantity': request.json['max_purchase_quantity'] if 'max_purchase_quantity' in request.json else 0,
        'max_quantity_available': request.json['max_quantity_available'] if 'max_quantity_available' in request.json else 0,
        'subtotal_price': request.json['subtotal_price'] if 'subtotal_price' in request.json else 0,
        'add_ons': request.json['add_ons'] if 'add_ons' in request.json else {},
        'survey_questions': request.json['survey_questions'] if 'survey_questions' in request.json else {},
        'event_tickets': request.json['event_tickets'] if 'event_tickets' in request.json else [],
        'creation_date': datetime.datetime.now(),
        'last_updated': datetime.datetime.now()

    }

    db.event.insert_one(query)

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'event_id': request.json['event_id']}), 201
