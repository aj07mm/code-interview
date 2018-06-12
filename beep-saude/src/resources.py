import json
from flask_cors import cross_origin
from flask import Blueprint, jsonify
from flask_restful import reqparse

from helpers import get_previous_dates, compose_redis_key
from constants import AVAILABLE_FROM_TO_CURRENCIES
from db import get_db


chart_api = Blueprint('chart_api', __name__)


# parser
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument(
    'source',
    type=str,
    required=True,
    help='Source cannot be empty'
)
parser.add_argument(
    'currency',
    type=str,
    required=True,
    action='append',
    help='Currencies cannot be empty'
)


@chart_api.route('/exchange-rates')
@cross_origin()
def exchange_rates():
    '''
        {
            name: 'USDBRL',
            series: [43934, 52503, 57177, 69658, 97031, 119931, 137133]
            categories: [
                "2018-05-18", "2018-05-17", "2018-05-16", "2018-05-15",
                "2018-05-14", "2018-05-13", "2018-05-12"
            ]
        }
    '''
    args = parser.parse_args()
    dates = get_previous_dates(7)
    all_dates = []

    for currency in filter(
        lambda x: x in args['currency'], AVAILABLE_FROM_TO_CURRENCIES
    ):
        payload = {"name": currency, "data": []}
        for date in dates:
            data = get_db().get(compose_redis_key("USD", currency, date))
            if data is None:
                raise Exception('Database not populated yet!')
            payload["data"].append(json.loads(data))
        all_dates.append(payload)

    return jsonify({"series": all_dates, "categories": dates})
