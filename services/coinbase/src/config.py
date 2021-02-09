import os
import json

def load_env():
    with open(os.getcwd()+'/src/.env.json') as fobj:
        return json.load(fobj)

class BaseConfig:
    TESTING = True

class DevelopmentConfig(BaseConfig):
    API_KEY = load_env().get('development').get('API_KEY')
    SECRET_KEY = load_env().get('development').get('SECRET_KEY')


