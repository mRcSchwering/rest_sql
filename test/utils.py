# this python file uses the following encoding: utf-8
from requests.auth import HTTPBasicAuth
from test.testdata import reset_database
import requests
import pytest

server = 'http://0.0.0.0:5000'
user = 'u1'
password = 'u1'
auth = HTTPBasicAuth(user, password)

# reset before starting tests
requests.get(server + '/reset_testdata/')


@pytest.fixture
def reset_database_after_test():
    yield
    requests.get(server + '/reset_testdata/')


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
