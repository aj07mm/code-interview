import unittest
from constants import DATE_FORMAT
from datetime import date, timedelta
from helpers import get_previous_dates, compose_redis_key


class TestGetPreviousDates(unittest.TestCase):
    def test_get_today(self):
        self.assertEqual(
            get_previous_dates(1)[-1], date.today().strftime(DATE_FORMAT)
        )

    def test_get_d_minus_3(self):
        self.assertEqual(
            get_previous_dates(3)[-1],
            ((date.today() - timedelta(2))).strftime(DATE_FORMAT)
        )

    def test_get_d_minus_7(self):
        self.assertEqual(
            get_previous_dates(7)[-1],
            ((date.today() - timedelta(6))).strftime(DATE_FORMAT)
        )


class TestComposeRedisKey(unittest.TestCase):
    def test_compose_one_string(self):
        self.assertEqual(compose_redis_key("USD"), "USD")

    def test_compose_two_string(self):
        self.assertEqual(compose_redis_key("USD", "BRL"), "USD:BRL")

    def test_compose_three_string(self):
        self.assertEqual(
            compose_redis_key("USD", "BRL", "2018-05-18"),
            "USD:BRL:2018-05-18"
        )


if __name__ == '__main__':
    unittest.main()
