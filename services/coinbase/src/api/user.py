from flask import Blueprint, jsonify
from flask_restx import Api, Resource

from src.client import Client

user_blueprint = Blueprint('user', __name__)
api = Api(user_blueprint)

class User(Resource):
    def get(self):
        client = Client()
        return client.get('user').json()


api.add_resource(User, '/user')