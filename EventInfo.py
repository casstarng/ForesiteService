from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
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

    return jsonify({'response': 'success',
                    'message': 'Query Success',
                    'results': str(results)}), 201

@bp.route('/foresite/getEventDetails', methods=['POST'])
def getEventDetails():
    # Check if user_name and password are present in request
    if not request.json or not 'event_id' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'event_id not present'}), 201
    query = {
        'event_id': request.json['event_id']
    }

    # Find with query
    cursor = db.event.find(query)
    results = list(cursor)

    if (len(results) == 1):
        return jsonify({'response': 'success',
                        'message': 'Query Success',
                        'results': str(results[0])}), 201
    else:
        return jsonify({'response': 'fail',
                        'message': 'Event ID does not exist'}), 201

