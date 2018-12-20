from flask_httpauth import HTTPBasicAuth
import json
import settings
import os

auth = HTTPBasicAuth()


# create local user
users = [{'name': 'u1', 'password': 'u1'}]
if not settings.TESTING and os.path.isfile('secrets/config.json'):
    with open('secrets/config.json') as inf:
        config = json.load(inf)
    if config.get('users') is not None:
        users = config['users']


@auth.verify_password
def verify_password(username, password):
    for user in users:
        if username == user['name'] and password == user['password']:
            return True
    return False
