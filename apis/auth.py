from flask_httpauth import HTTPBasicAuth
import json
import settings

auth = HTTPBasicAuth()


users = [{'name': 'u1', 'password': 'u1'}]
if not settings.TESTING:
    with open('secrets/config.json') as inf:
        config = json.load(inf)
        users = config['users']


@auth.verify_password
def verify_password(username, password):
    for user in users:
        if username == user['name'] and password == user['password']:
            return True
    return False
