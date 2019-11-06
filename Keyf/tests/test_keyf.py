import os
import tempfile
import pytest
import Keyf

# https://flask.palletsprojects.com/en/1.1.x/testing/

@pytest.fixture
def client():
    db_fd, Keyf.app.config['DATABASE'] = tempfile.mkstemp()
    Keyf.app.config['TESTING'] = True

    with Keyf.app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(Keyf.app.config['DATABASE'])

def test_home(client):
    """Test html"""

    rv = client.get('/')
    assert b"<!doctype html>" in rv.data

def test_all_stores(client):
    """Test DB stores"""
    
    rv = client.get("/shops/-1")
    assert b"shops" in rv.data