""" Function to check if a year is a leap year
"""

import unittest

def is_leap_year(year):
    """ Takes a year and returns true if it is a leap year"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return  year % 4 == 0


class TestLeapYear(unittest.TestCase):
    def test_leap(self):
        self.assertTrue(is_leap_year(1992))
        self.assertTrue(is_leap_year(1996))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1967))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2200))
        self.assertFalse(is_leap_year(2300))
        self.assertTrue(is_leap_year(2400))

if __name__ == '__main__':
    unittest.main()
