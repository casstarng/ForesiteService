import Login, EventInfo, Ticket
from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS, cross_origin
import pymongo

app = Flask(__name__)
app.register_blueprint(Login.bp)
app.register_blueprint(EventInfo.bp)
app.register_blueprint(Ticket.bp)

if __name__ == "__main__":
    app.run()