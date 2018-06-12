stockvalues = {
    1: 130,
    2: 90,
    3: 40,
    4: 85,
    5: 170,
}

def get_max_profit(stockvalues):
    max_profit = 0
    price_map = {}
    for time, value in stockvalues.items():
        if price_map.get(value, None) is None:
            price_map[value] = value
        for price_map_time, price_map_value in price_map.items():
            if value > price_map[price_map_value]:
                price_map[price_map_value] = value

    for key, value in price_map.items():
        profit = value - key
        if profit > max_profit:
            max_profit = profit

    return profit

print(get_max_profit(stockvalues))
