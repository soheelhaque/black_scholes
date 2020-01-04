from unittest import TestCase
from calculator import calculate_call_option_price


class TestCalculate_call_option_price(TestCase):
    def test_calculate_call_option_price(self):
        price = calculate_call_option_price(strike_price=15, option_maturity_years=3.5, current_price=25,
                                            volatility_percent=20, risk_free_rate_percent=5)
        self.assertEqual(round(price, 3), 12.494)
