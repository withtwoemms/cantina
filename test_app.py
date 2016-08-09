import cantina
import unittest


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = cantina.app.test_client()
        cantina.app.config['TESTING'] = True

    def test_index_route(self):
        assert self.app.get('/')._status_code == 200
        assert self.app.get('/').data == "Hello, World"

if __name__ == "__main__":
    unittest.main()
