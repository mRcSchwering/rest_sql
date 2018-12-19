# this python file uses the following encoding: utf-8
import pytest
import requests
from test.utils import Get, Post, reset_database_after_test

URI = '/posts'


def test_PostsByParameters_with_valid_id():
    response = Get(URI + '?id=1').do()
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    assert content['title'] == 'Hello Python!'


def test_PostsByParameters_with_non_existent_id():
    response = Get(URI + '?id=5').do()
    assert response.status_code == 404, 'Should be NOT FOUND'
    content = response.json()
    assert 'result was required but none was found' in content['message']


def test_get_AllPosts():
    response = Get(URI + '/').do()
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    assert len(content) == 2, 'Should be 2 posts'


def test_creating_new_post_by_post_AllPosts(reset_database_after_test):
    payload = {
        'title': 'test',
        'body': 'test',
        'category_id': 1
    }
    response = Post(URI + '/', payload).do()
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    assert content == 'post created'
    response = Get(URI + '/').do()
    assert response.status_code == 200, 'Should be OK'
    content = response.json()
    titles = [post['title'] for post in content]
    assert 'test' in titles, 'Newly created test post should be there'
