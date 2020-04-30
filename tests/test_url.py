import unittest

# from boddle import boddle
# from server import get_url

from webtest import TestApp
from server import app

class TestAPIMethods(unittest.TestCase):
    def test_url(self):
        """Test GET /v1/urls/<hash_url>"""
        # with boddle(path="/v1/urls/test", method="GET"):
        #     self.assertEqual(get_url("test"), "test")
        test_app = TestApp(app)
        resp = test_app.get('/v1/urls/test')

        self.assertEqual(resp.status, "200 OKkjkj")
        self.assertEqual(resp.body, b"test")


if __name__ == '__main__':
    unittest.main()
