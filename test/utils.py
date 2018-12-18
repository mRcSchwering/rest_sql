# this python file uses the following encoding: utf-8
from requests.auth import HTTPBasicAuth
from test.testdata import reset_database
import requests
import pytest

server = 'http://0.0.0.0:5000'
auth = HTTPBasicAuth('u1', 'u1')

requests.get(server + '/reset_testdata/')


@pytest.fixture
def reset_database_after_test():
    yield
    requests.get(server + '/reset_testdata/')
