import pytest
import Keyf
from Keyf.Entities import Shop, MenuItem, Review
from flask.testing import FlaskClient
import json
from tests.helpers import createShop

# https://flask.palletsprojects.com/en/1.1.x/testing/
# python3 -m pytest -v  : runs tests
# python3 -m pytest -vs : runs tests and displays sys out


@pytest.fixture
def client():
    Keyf.app.config["TESTING"] = True

    with Keyf.app.test_client() as client:
        return client


def test_home(client):
    """Test HTML"""

    resp = client.get("/")
    assert b"<!doctype html>" in resp.data


def test_all_shops(client):
    """Test all shops"""

    resp = client.get("/shops/-1")
    assert b"shops" in resp.data


def test_shop_zero(client):
    """Edge case"""
    resp = client.get("/shops/0")
    assert resp.status_code == 404


def test_shop_negative(client):
    "Test negative numbers, -1 will return all the entries"
    resp = client.get("/shops/-5")
    assert resp.status_code == 404


def test_shop_id(client):
    """Test shop ID"""
    COUNT = 5

    for i in range(1, COUNT):
        resp = client.get("/shops/{}".format(i))
        # Check if the id of the shop matches the index
        resp_shop = Shop(resp.json)
        assert resp_shop.id == i


def test_add_shop(client: FlaskClient):
    """Test adding new shop"""
    shop = createShop(1)
    resp = client.put("/shops/0", data=json.dumps(shop.serialize()))

    # Ideally we should check the shop we've added to the shop
    # we would get using the id found in the response

    assert "insert" == resp.json["operation_type"]


def test_replace_shop(client: FlaskClient):
    """Test replacing (updating) an existing shop"""
    shop = createShop(1)
    resp = client.post("/shops/0", data=json.dumps(shop.serialize()))

    # Ideally we should check the shop we've updated to the shop
    # we would get using the id found in the response

    assert "replace" == resp.json["operation_type"]


def test_delete_shop(client):
    """Test deleting a shop"""
    resp = client.delete("/shops/0")
    assert b"OK" in resp.data


def test_delete_non_existent(client):
    """Test deleting a shop that doesn't exist"""
    resp = client.delete("/shops/999")
 
    assert resp.status_code == 404