# this python file uses the following encoding: utf-8
import pytest
import requests
import test.utils as utils

reset_database_after_test = utils.reset_database_after_test
URL = utils.server + '/posts'


def test_PostsByParameters_with_valid_id():
    params = 'id=1'
    response = requests.get('%s?%s' % (URL, params), auth=utils.auth)
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    assert content['title'] == 'Hello Python!'


def test_PostsByParameters_with_non_existent_id():
    params = 'id=5'
    response = requests.get('%s?%s' % (URL, params), auth=utils.auth)
    assert response.status_code == 404, 'Should be NOT FOUND'
    response.reason
    content = response.json()
    assert 'result was required but none was found' in content['message']


def test_get_AllPosts():
    response = requests.get(URL + '/', auth=utils.auth)
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    assert len(content) == 2, 'Should be 2 posts'


def test_creating_new_post_by_post_AllPosts(reset_database_after_test):
    params = {
        'title': 'test',
        'body': 'test',
        'category_id': 1
    }
    response = requests.post(URL + '/', json=params, auth=utils.auth)
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    assert content == 'post created'
    response = requests.get(URL + '/', auth=utils.auth)
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    titles = [post['title'] for post in content]
    assert 'test' in titles, 'Newly created test post should be there'
