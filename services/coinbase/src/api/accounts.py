from flask import Blueprint, jsonify
from flask_restx import Api, Resource

from src.client import Client

accounts_blueprint = Blueprint('accounts', __name__)
api = Api(accounts_blueprint)

class Accounts(Resource):
    def get(self):
        client = Client()
        return client.get('accounts').json()

api.add_resource(Accounts, '/accounts')