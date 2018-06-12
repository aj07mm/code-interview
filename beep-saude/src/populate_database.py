import os
import sys
import json
import requests
from db import get_db
from helpers import get_previous_dates, compose_redis_key
from constants import AVAILABLE_FROM_TO_CURRENCIES


def populate_database(db_name):
    db_conn = get_db(db_name)
    dates = get_previous_dates(7)

    print("------------------------------------------")
    print("POPULATING DATABASE WITH 3RD PARTY API....")
    print("------------------------------------------")

    for date in dates:
        req = requests.get(
            "http://apilayer.net/api/historical",
            params={
                "access_key": os.environ.get("CURRENCY_LAYER_ACCESS_KEY"),
                "date": date,
                "source": "USD",
                "currencies": "BRL, EUR, ARS",
                "format": 1,
            }
        )

        req_json = req.json()

        # save raw json
        db_conn.set(date, json.dumps(req_json))
        print(date, json.dumps(req_json))

        # save amount by currency:date
        for currency in AVAILABLE_FROM_TO_CURRENCIES:
            db_conn.set(
                compose_redis_key("USD", currency, date),
                json.dumps(req_json['quotes']["USD{}".format(currency)])
            )
            print(
                compose_redis_key("USD", currency, date),
                json.dumps(req_json['quotes']["USD{}".format(currency)])
            )

    print("------------------------------------------")
    print("FINISH POPULATING DATABASE")
    print("------------------------------------------")


if __name__ == '__main__':
    populate_database(sys.argv[1])
