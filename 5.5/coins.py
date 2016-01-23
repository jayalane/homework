"""Function to calculate change in coins from amounts less than one dollar

Usage:

>>> import coins
>>> coins.amount_in_coins_string(.99)
'3 quarters, 2 dimes, 4 pennies'
>>>
"""

import unittest

_COINS = [('quarter', 0.25),
          ('dime', .10),
          ('nickel', .05),
          ('penny', .01)]

def _amount_in_coins(in_value):
    """Returns a list of (coin, number of coins) tuples that add up to in_value in value"""
    cur_value = in_value
    if cur_value - round(cur_value, 2)  > 1e-10:  # less than 1e-10 will occur due to floating point
        raise Exception("Can't represent {} in US coins".format(in_value))
    result = []
    for coin, value in _COINS:
        if cur_value == 0:
            break
        num_coins = 0
        while value <= cur_value:
            cur_value -= value   # could have used modulus
            cur_value = round(cur_value, 2)  # floating point again
            num_coins += 1
        if num_coins:
            result.append((coin, num_coins))
    return result

def _coins_list_to_string(coins_list):
    result = []
    for coin, number in coins_list:
        if number == 0:
            continue
        if number > 1:
            if coin[-1] == 'y':
                coin_string = coin[:-1] + 'ies'
            else:
                coin_string = coin + 's'
        elif number > 0:
            coin_string = coin
        result.append(str(number) + " " + coin_string)
    res = ", ".join(result)
    res = ", and ".join(res.rsplit(", ", 1))
    if len(result) == 2:
        res = res.replace(',', '')
    return res


def amount_in_coins_string(in_value):
    return _coins_list_to_string(_amount_in_coins(in_value))


class TestCoinsr(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(amount_in_coins_string(0.76), '3 quarters and 1 penny')
        self.assertEqual(amount_in_coins_string(0.24), '2 dimes and 4 pennies')
        self.assertEqual(amount_in_coins_string(0), '')
        self.assertEqual(amount_in_coins_string(0.99), '3 quarters, 2 dimes, and 4 pennies')

if __name__ == '__main__':
    unittest.main()
