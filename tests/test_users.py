import pytest
import Keyf
from Keyf.Entities import User
from helpers import createUser

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
    user = createUser(-1)
    resp = client.put("/users/0", user.serialize())

    # TODO: Replace
    assert b"insert" in resp.data


def test_user_id(client):
    COUNT = 5
    for i in range(COUNT):
        user = createUser(i)
        resp = client.put("/users/0", user.serialize())

        # TODO: Replace
        assert b"insert" in resp.data


def test_add_user(client):
    user = createUser(1)
    resp = client.put("/users/0", user.serialize())

    # TODO: Replace
    assert False


def test_update_user(client):
    user = createUser(1)
    resp = client.put("/users/0", user.serialize())

    # TODO: Replace
    assert b"insert" in resp.data


def test_delete_user(client):
    resp = client.delete("/users/1")

    # TODO: Replace
    assert False


def test_delete_non_existent(client):
    resp = client.delete("/users/9999")

    # TODO: Replace
    assert resp.status_code == 500
