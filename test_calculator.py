# TODO: change name of imported function
import json
import unittest
from calculator import calculate_call_option_price

class TestOptionPriceCalculator(unittest.TestCase):
    
    def test_calculate_call_option_price_positive_ir(self):
        # TODO: add parameter for call/put
        model_inputs = '{"strike_price":105, "option_maturity_years":1, "current_price":100, "volatility_percent":20, "risk_free_rate_percent":5}'
        json_in = json.loads(model_inputs)
        expected_result = 8.021
        actual_result = round(calculate_call_option_price(json_in),3)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_call_option_price_negative_ir(self):
        # TODO: add parameter for call/put
        model_inputs = '{"strike_price" : 105, "option_maturity_years" : 1, "current_price" : 100, "volatility_percent" : 20, "risk_free_rate_percent" : -5}'
        json_in = json.loads(model_inputs)
        expected_result = 4.185
        actual_result = round(calculate_call_option_price(json_in),3)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()