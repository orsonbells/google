#!/usr/bin/env python3

def best_time_to_buy_and_sell(prices: list[int]) -> int:
    """
    >>> best_time_to_buy_and_sell([7,1,5,3,6,4])
    5
    >>> best_time_to_buy_and_sell([7,6,4,3,1])
    0
    """

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)

    return max_profit
