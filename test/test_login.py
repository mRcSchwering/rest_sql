# this python file uses the following encoding: utf-8
import pytest
import requests
from requests.auth import HTTPBasicAuth
import test.utils as utils


def test_query_without_auth():
    response = requests.get(utils.server + '/posts/')
    assert response.status_code == 401, 'Should be UNAUTHORIZED'


def test_query_with_wrong_user():
    auth = HTTPBasicAuth('asd', 'asd')
    response = requests.get(utils.server + '/posts/', auth=auth)
    assert response.status_code == 401, 'Should be UNAUTHORIZED'


def test_query_with_wrong_password():
    auth = HTTPBasicAuth('u1', 'asd')
    response = requests.get(utils.server + '/posts/', auth=auth)
    assert response.status_code == 401, 'Should be UNAUTHORIZED'


def test_query_with_correct_user_and_password():
    auth = HTTPBasicAuth('u1', 'u1')
    response = requests.get(utils.server + '/posts/', auth=auth)
    assert response.status_code == 200, 'Should be OK'
