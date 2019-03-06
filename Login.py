from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://admin:foresiteadmin@54.218.76.138/foresite")  # defaults to port 27017
db = client.foresite

@app.route('/foresite/login', methods=['POST'])
def login():

    if not request.json or not 'user_name' in request.json or not 'password' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'User name or password is not present'}), 400
    query = {
        'user_name': request.json['user_name'],
        'password': request.json['password']
    }
    cursor = db.user.find(query)

    results = list(cursor)
    if(len(results) == 1):
        return jsonify({'response': 'success',
                        'message': 'Authentication successful'}), 201
    else:
        return jsonify({'response': 'fail',
                        'message': 'Authentication failed'}), 400


@app.route('/foresite/createUser', methods=['POST'])
def createUser():

    if not request.json or not 'user_name' in request.json or not 'password' in request.json:
        return jsonify({'response': 'fail',
                        'message': 'User name or password is not present'}), 400
    query = {
        'user_name': request.json['user_name']
    }
    cursor = db.user.find(query)

    results = list(cursor)
    if(len(results) == 1):
        return jsonify({'response': 'fail',
                        'message': 'User name is already being used'}), 400

    query = {
        'user_name': request.json['user_name'],
        'password': request.json['password']
    }
    db.user.insert_one(query)
    return jsonify({'response': 'success',
                    'message': 'User ' + request.json['user_name'] + " has been inserted"}), 201

if __name__ == '__main__':
    app.run(debug=True)