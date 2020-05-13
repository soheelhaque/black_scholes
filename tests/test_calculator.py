import json
import unittest

from context import black_scholes
from black_scholes.calculator import calculate_option_price


class TestOptionPriceCalculator(unittest.TestCase):
    
    def test_calculate_call_option_price_positive_ir(self):
        model_inputs = '{"call_put":"CALL", "strike_price":105, "option_maturity_years":1, "current_price":100, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":5}'
        json_in = json.loads(model_inputs)
        expected_result = 8.021
        actual_result = calculate_option_price(json_in)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_call_option_price_negative_ir(self):
        model_inputs = '{"call_put":"CALL", "strike_price":105, "option_maturity_years":1, "current_price":100, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":-5}'
        json_in = json.loads(model_inputs)
        expected_result = 4.185
        actual_result = calculate_option_price(json_in)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_put_option_price_positive_ir(self):
        model_inputs = '{"call_put":"PUT", "strike_price":105, "option_maturity_years":1, "current_price":100, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":5}'
        json_in = json.loads(model_inputs)
        expected_result = 7.900
        actual_result = calculate_option_price(json_in)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_put_option_price_negative_ir(self):
        model_inputs = '{"call_put":"PUT", "strike_price":105, "option_maturity_years":1, "current_price":100, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":-5}'
        json_in = json.loads(model_inputs)
        expected_result = 14.568
        actual_result = calculate_option_price(json_in)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_call_option_zero_maturity(self):
        model_inputs = '{"call_put":"CALL", "strike_price":105, "option_maturity_years":0, "current_price":100, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":5}'
        json_in = json.loads(model_inputs)
        self.assertRaises(ZeroDivisionError, calculate_option_price, model_inputs=json_in)
    
    def test_calculate_call_option_zero_strike(self):
        model_inputs = '{"call_put":"CALL", "strike_price":0, "option_maturity_years":1, "current_price":100, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":5}'
        json_in = json.loads(model_inputs)
        self.assertRaises(ZeroDivisionError, calculate_option_price, model_inputs=json_in)

    def test_calculate_call_option_zero_price(self):
        model_inputs = '{"call_put":"CALL", "strike_price":105, "option_maturity_years":1, "current_price":0, ' \
                       '"volatility_percent":20, "risk_free_rate_percent":5}'
        json_in = json.loads(model_inputs)
        self.assertRaises(ValueError, calculate_option_price, model_inputs=json_in)

if __name__ == '__main__':
    unittest.main()
