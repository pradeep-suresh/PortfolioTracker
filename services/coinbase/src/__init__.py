import os
from flask import Flask, jsonify
from flask_restx import Resource, Api

from src.client import Client

app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

from src.api.ping import ping_blueprint
app.register_blueprint(ping_blueprint)

from src.api.time import time_blueprint
app.register_blueprint(time_blueprint)

from src.api.accounts import accounts_blueprint
app.register_blueprint(accounts_blueprint)

from src.api.user import user_blueprint
app.register_blueprint(user_blueprint)

