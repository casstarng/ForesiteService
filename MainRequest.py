from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)

@app.route('/foresite/getEventDetails', methods=['POST'])
def create_task():
    if not request.json or not 'event_id' in request.json:
        return jsonify({'error': 'fail'}), 400

    client = pymongo.MongoClient("mongodb://admin:foresiteadmin@34.221.254.81/foresite")  # defaults to port 27017

    db = client.foresite

    cursor = db.user.find()

    for doc in cursor:
        print(doc)

    return jsonify({'response': 'connection made!'}), 201

if __name__ == '__main__':
    app.run(debug=True)