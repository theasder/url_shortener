from bottle import response
from webtest import TestApp

from ..server import app


def test_url():
    """Test GET /v1/urls/<hash_url>"""
    test_app = TestApp(app)
    resp = test_app.get('/v1/urls/test')

    # assert resp.body == 'test'
    assert resp.status == "200 OK"
    assert resp.body == b'test'