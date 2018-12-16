from flask_httpauth import HTTPBasicAuth
import json

auth = HTTPBasicAuth()

with open('secrets/config.json') as inf:
    config = json.load(inf)


@auth.verify_password
def verify_password(username, password):
    users = config['users']
    for user in users:
        if username == user['name'] and password == user['password']:
            return True
    return False
