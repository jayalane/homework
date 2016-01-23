"""Provides two functions to do sales tax calculations: sales_tax and total_with_tax()
   that take an amount and perform the sales tax calculation for
"""


import unittest

_TAX_RATE = 0.0875


def sales_tax(total_price, tax_rate = _TAX_RATE):
    return round(total_price * tax_rate, 2)


def total_with_tax(total_sale, tax_rate = _TAX_RATE):
    return round(total_sale + total_sale * tax_rate, 2)


class TestTaxes(unittest.TestCase):
    def test_taxes(self):
        self.assertEqual(sales_tax(1), 0.09)
        self.assertEqual(sales_tax(0), 0.0)
        self.assertEqual(total_with_tax(1), 1.09)
        self.assertEqual(total_with_tax(1, tax_rate=0.04), 1.04)

if __name__ == '__main__':
    unittest.main()

