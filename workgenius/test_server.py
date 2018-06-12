import requests_mock
from falcon import testing

from .server import queryUrl, create_server
from .test_data import GIPHY_SUCCESS_BODY

EXPECTED_API_SUCCESS_RESULT = [
    dict(height=100, url="https://media1.giphy.com/media/Pcwj0y1hkpJny/100.gif", width=178)
]


class GiphyApiTest(testing.TestCase):
    def setUp(self):
        super().setUp()
        self.app = create_server()

    def test_giphy_search_is_successful(self):
        with requests_mock.mock() as m:
            m.get(queryUrl, text=GIPHY_SUCCESS_BODY)
            result = self.simulate_get('/search', params={"search": "sphinx"})
            self.assertEqual(200, result.status_code)
            self.assertListEqual(result.json, EXPECTED_API_SUCCESS_RESULT)
