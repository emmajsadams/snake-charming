from flaskr import create_app
import json

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_view_single_get(client):
    response = client.get('/view?username=humble')
    assert json.loads(response.data) == { 'count': 1, 'views': [{ 'id': 1, 'username': 'humble' }] }

def test_view_multiple_gets(client):
    response_humble = client.get('/view?username=humble')
    response_bundle = client.get('/view?username=bundle')

    assert json.loads(response_humble.data) == { 'count': 1, 'views': [{ 'id': 1, 'username': 'humble' }] }
    assert json.loads(response_bundle.data) == { 'count': 2, 'views': [{ 'id': 1, 'username': 'humble' }, { 'id': 2, 'username': 'bundle' }] }