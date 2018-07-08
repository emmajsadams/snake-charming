from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

# should fail at first
def test_hello(client):
    response = client.get('/?username=poop')
    assert response.data == b'Hello, World!'