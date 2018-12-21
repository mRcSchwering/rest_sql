# this python file uses the following encoding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import pytest
import os
import time


# setup
FLASK_APP = os.environ.get('FLASK_APP')
host = '0.0.0.0' if FLASK_APP is None else FLASK_APP
server = 'http://%s:5000' % host

user = 'u1'
password = 'u1'
auth = HTTPBasicAuth(user, password)


# reset before starting tests
requests.get('http://0.0.0.0:5001/reset_testdata/')


# importing run_around_tests will automatically apply it
@pytest.fixture(autouse=True)
def run_around_tests():
    #db_before = get_db_content()
    yield
    #db_after = get_db_content()
    #diff = compare_content(db_before, db_after)
    #if diff:
    print('resetting db')
    requests.get('http://0.0.0.0:5001/reset_testdata/')


class Get:

    server = server
    auth = auth

    def __init__(self, uri):
        self.uri = uri

    def do(self):
        return requests.get(self.server + self.uri, auth=self.auth)


class Post:

    server = server
    auth = auth

    def __init__(self, uri, payload):
        self.payload = payload
        self.uri = uri

    def do(self):
        return requests.post(self.server + self.uri, json=self.payload, auth=self.auth)
