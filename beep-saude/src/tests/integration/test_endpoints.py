import unittest
from app import app
from populate_database import populate_database
from settings import DATABASE_TEST


class TestEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        populate_database(DATABASE_TEST)
        app.config.update(DATABASE=DATABASE_TEST)
        cls.app = app

    def test_values_correctly_stored_as_numbers_on_database(self):
        response = self.app.test_client().get(
            '/exchange-rates?source=USD&currency=BRL'
        )
        response_json = response.get_json()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response_json['categories']), 7)
        self.assertEquals(len(response_json['series'][0]['data']), 7)
        self.assertEquals(response_json['series'][0]['name'], 'BRL')


if __name__ == '__main__':
    unittest.main()
