from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
import pymongo

app = Flask(__name__)
CORS(app)

bp = Blueprint('login', __name__)

#client = pymongo.MongoClient("mongodb://admin:foresiteadmin@54.218.76.138/foresite")  # defaults to port 27017
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.foresite

@bp.route('/foresite/login', methods=['POST'])
def login():
    # Check if user_name and password are present in request
    if not request.json or not 'user_name' in request.json or not 'password' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'User name or password is not present'}), 201
    query = {
        'user_name': request.json['user_name'],
        'password': request.json['password']
    }

    # Find with query
    cursor = db.user.find(query)

    results = list(cursor)

    # If match found, then return success
    if(len(results) == 1):
        return jsonify({'response': 'success',
                        'message': 'Authentication successful'}), 201
    else:
        return jsonify({'response': 'fail',
                        'message': 'Authentication failed'}), 201


@bp.route('/foresite/createUser', methods=['POST'])
def createUser():

    # Check if user_name and password are present in request
    if not request.json or not 'first_name' in request.json \
            or not 'last_name' in request.json \
            or not 'email' in request.json \
            or not 'phone_number' in request.json \
            or not 'user_name' in request.json \
            or not 'password' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'Complete user info not present'}), 201

    # Check if user_name is already taken
    query = {
        'user_name': request.json['user_name']
    }
    cursor = db.user.find(query)

    results = list(cursor)
    if(len(results) == 1):
        return jsonify({'response': 'fail',
                        'message': 'User name is already being used'}), 201

    # Insert new data
    query = {
        'first_name':  request.json['first_name'],
        'last_name': request.json['last_name'],
        'email': request.json['email'],
        'phone_number': request.json['phone_number'],
        'user_name': request.json['user_name'],
        'password': request.json['password']
    }
    db.user.insert_one(query)
    return jsonify({'response': 'success',
                    'message': 'User ' + request.json['user_name'] + " has been inserted"}), 201
