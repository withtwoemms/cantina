import cantina
import mock
import unittest
import yaml


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = cantina.app.test_client()
        cantina.app.config['TESTING'] = True

    def test_index_route(self):
        assert self.app.get('/')._status_code == 200
        assert '<!DOCTYPE html>' in self.app.get('/').data

    def test_hello_route(self):
        assert self.app.get('/hello').data == "Hello, World"

    @mock.patch('cantina.requests.get')
    def test_outside_post_route(self, mock_get):
        mock_resp = mock.Mock()
        expected_json = {
            'url': 'https://jsonplaceholder.typicode.com/posts/1',
            'status': 200,
            'posts': {
                'body': 'body for post with userId=1, id=1',
                'userId': 1,
                'id': 1,
                'title': 'POST 1:1'
            }
        }
        mock_resp.json.return_value = expected_json
        mock_resp.status_code = 200
        mock_get.return_value = mock_resp
        resp_with_post = yaml.load(self.app.get('/outside/posts/1').data)
        self.assertItemsEqual(resp_with_post.keys(), ['url', 'status', 'posts'])

    @mock.patch('cantina.requests.get')
    def test_outside_posts_route(self, mock_get):
        mock_resp = mock.Mock()
        expected_json = {
            'url': 'https://jsonplaceholder.typicode.com/posts',
            'status': 200,
            'posts': [
                {
                    'body': 'body for post with userid=1, id=1',
                    'userid': 1,
                    'id': 1,
                    'title': 'post 1:1'
                },
                {
                    'body': 'body for post with userid=1, id=2',
                    'userid': 1,
                    'id': 2,
                    'title': 'post 1:2'
                },
            ]
        }
        mock_resp.json.return_value = expected_json
        mock_resp.status_code = 200
        mock_get.return_value = mock_resp
        resp_with_posts = yaml.load(self.app.get('/outside/posts').data)
        self.assertItemsEqual(resp_with_posts.keys(), ['url', 'status', 'posts'])
        self.assertGreater(len(resp_with_posts.get('posts')), 1)


if __name__ == "__main__":
    unittest.main()
