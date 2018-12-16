# this python file uses the following encoding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import pytest


ssl = False
protocol = 'https' if ssl else 'http'
host = '0.0.0.0'
port = '5000'
server = '%s://%s:%s' % (protocol, host, port)

auth = HTTPBasicAuth('u1', 'asd')


@pytest.fixture
def reset_database_after_test():
    yield
    requests.get(server + '/misc/reset_database', auth=auth)
