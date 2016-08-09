import unittest

from app import app


class FlaskAppTestCase(unittest.TestCase):
    def test_index_route(self):
        self.assertEqual(0,1)

if __name__ == "__main__":
    unittest.main()
