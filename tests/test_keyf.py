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


def test_home(client):
    """Test HTML"""

    resp = client.get('/')
    assert b"<!doctype html>" in resp.data

def test_all_shops(client):
    """Test all shops"""
    
    resp = client.get("/shops/-1")
    assert b"shops" in resp.data

def test_shop_zero(client):
    """Edge case"""
    resp = client.get("/shops/0")
    # TODO: Check for empty response
    assert b"" in resp.data

def test_shop_negative(client):
    "Test negative numbers"
    # TODO
    assert False

def test_shop_id(client):
    """Test shop ID"""
    COUNT = 5
    
    for i in range(1, COUNT):
        resp = client.get("/shops/{}".format(i))
        # Check if the id of the shop matches the index
        resp_shop = Shop(resp.json)
        assert resp_shop.id == i

def test_add_shop(client):
    """Test adding new shop"""
    # TODO: create an arbitrary shop
    assert False

def test_delete_shop(client):
    """Test deleting a shop"""
    # TODO
    assert False