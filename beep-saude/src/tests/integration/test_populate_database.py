import unittest

from db import get_db
from populate_database import populate_database
from helpers import get_previous_dates, compose_redis_key
from settings import DATABASE_TEST


class TestPopulateDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dates = get_previous_dates(7)
        populate_database(DATABASE_TEST)

    def test_values_correctly_stored_as_numbers_on_database(self):
        self.assertTrue(
            get_db().get(compose_redis_key("USD", "BRL", self.dates[0]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )
        self.assertTrue(get_db().get(
            compose_redis_key("USD", "BRL", self.dates[1]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )
        self.assertTrue(
            get_db().get(compose_redis_key("USD", "BRL", self.dates[2]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )
        self.assertTrue(
            get_db().get(compose_redis_key("USD", "BRL", self.dates[3]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )
        self.assertTrue(
            get_db().get(compose_redis_key("USD", "BRL", self.dates[4]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )
        self.assertTrue(
            get_db().get(compose_redis_key("USD", "BRL", self.dates[5]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )
        self.assertTrue(
            get_db().get(compose_redis_key("USD", "BRL", self.dates[6]))
            .decode('utf-8').replace('.', '', 1).isdigit()
        )


if __name__ == '__main__':
    unittest.main()
