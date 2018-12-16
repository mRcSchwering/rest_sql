# this python file uses the following encoding: utf-8
import pytest
import requests
from requests.auth import HTTPBasicAuth
import test.utils as utils


def test_query_without_auth():
    response = requests.get(utils.server + '/posts/')
    assert response.status_code == 401, 'Should be unauthorized'
    assert response.reason == 'UNAUTHORIZED', 'Should be unauthorized'


def test_query_with_wrong_user():
    auth = HTTPBasicAuth('asd', 'asd')
    response = requests.get(utils.server + '/posts/', auth=auth)
    assert response.status_code == 401, 'Should be unauthorized'
    assert response.reason == 'UNAUTHORIZED', 'Should be unauthorized'


def test_query_with_correct_user():
    auth = HTTPBasicAuth('u1', 'asd')
    response = requests.get(utils.server + '/posts/', auth=auth)
    assert response.status_code == 200, 'Should be ok'
    assert response.reason == 'OK', 'Should be ok'
    assert len(response.json()) == 2, 'Should include 2 posts'
