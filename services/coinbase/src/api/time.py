from flask import Blueprint, jsonify
from flask_restx import Api, Resource

from src.client import Client

time_blueprint = Blueprint('time', __name__)
api = Api(time_blueprint)

class Time(Resource):
    def get(self):
        client = Client()
        return client.get('time').json() 

api.add_resource(Time, '/time')