# this python file uses the following encoding: utf-8
import pytest
import requests
from requests.auth import HTTPBasicAuth
import test.utils as utils

secured_endpoints = [
    utils.Get('/posts'),
    utils.Get('/posts/'),
    utils.Post('/posts/', {'title': '', 'body': '', 'category_id': 1})
]


@pytest.mark.parametrize('Call', secured_endpoints)
def test_call_should_be_secured(Call):
    Call.auth = None
    response = Call.do()
    print(Call.uri)
    print(Call)
    assert response.status_code == 401, 'Should be UNAUTHORIZED: no auth'

    Call.auth = HTTPBasicAuth('<!--!>', '<!--!>')
    response = Call.do()
    assert response.status_code == 401, 'Should be UNAUTHORIZED: user doesnt exist'

    Call.auth = HTTPBasicAuth(utils.user, '<!--!>')
    response = Call.do()
    assert response.status_code == 401, 'Should be UNAUTHORIZED: user doesnt exist'

    Call.auth = HTTPBasicAuth(utils.user, utils.password)
    response = Call.do()
    assert response.status_code == 200, 'Should be OK'
    requests.get(utils.server + '/reset_testdata/')
