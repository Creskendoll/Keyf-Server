import pytest
import Keyf
from Keyf.Entities import User

# https://flask.palletsprojects.com/en/1.1.x/testing/
# python3 -m pytest -v  : runs tests
# python3 -m pytest -vs : runs tests and displays sys out


@pytest.fixture
def client():
    Keyf.app.config["TESTING"] = True

    with Keyf.app.test_client() as client:
        return client


def test_all_users(client):
    resp = client.get("/users/-1")

    assert b"users" in resp.data


def test_get_user(client):
    resp = client.get("/users/1")
    resp_user = User(resp.json)

    assert resp_user.id == 1


def test_user_zero(client):
    resp = client.get("/users/0")

    assert resp.status_code == 404


def test_user_negative(client):
    assert False


def test_user_id(client):
    COUNT = 5
    assert False


def test_add_user(client):
    assert False


def test_update_user(client):
    assert False


def test_delete_user(client):
    assert False


def test_delete_non_existent(client):
    assert False
