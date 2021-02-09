import os
from flask import Flask, jsonify
from flask_restx import Resource, Api

from src.client import Client

app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

class Ping(Resource):
    def get(self):
        return {
            'status' : 'success',
            'message': 'pong!'
        }

class Time(Resource):
    def get(self):
        client = Client()
        return jsonify(client.generate_cb_access_timestamp())


api.add_resource(Ping, '/ping')
api.add_resource(Time, '/time')