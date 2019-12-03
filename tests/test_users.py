import pytest
import Keyf
from Keyf.Entities import Shop

# https://flask.palletsprojects.com/en/1.1.x/testing/
# python3 -m pytest -v  : runs tests
# python3 -m pytest -vs : runs tests and displays sys out

@pytest.fixture
def client():
    Keyf.app.config['TESTING'] = True

    with Keyf.app.test_client() as client:
        return client

def test_get_user(client):
    pass