import json
import unittest
import requests

class TestOptionPriceCalculator(unittest.TestCase):
    
	# define the api-endpoint  
	API_ENDPOINT = "http://172.17.0.1:5000/api/calculator"
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	
	def create_data_to_post(self, call_put, current_price, option_maturity_years, risk_free_rate_percent, strike_price, volatility_percent):
		model_inputs = {"call_put": call_put, "current_price": current_price, 
		"option_maturity_years": option_maturity_years, "risk_free_rate_percent": risk_free_rate_percent, "strike_price": strike_price, "volatility_percent": volatility_percent}
		# data to be sent to api
		# create a dictionary to hold the model inputs
		data = json.dumps(model_inputs)
		return data

	def test_integration_calculate_option_price(self):
		# define the data to be posted to the endpoint
		call_put = "CALL"
		current_price = 100
		option_maturity_years = 1
		risk_free_rate_percent = 5
		strike_price = 105
		volatility_percent = 20
		
		# wrap the data as JSON
		data = self.create_data_to_post(call_put, current_price, option_maturity_years, risk_free_rate_percent, strike_price, volatility_percent)
		
		# sending post request and saving response as response object 
		response = requests.post(url = self.API_ENDPOINT, data = data, headers = self.headers, timeout = 30)
		response.raise_for_status()
	
		# extracting the response and print it
		actual_result = float(response.text)
		expected_result = 8.021
		self.assertEqual(expected_result, actual_result)

		
if __name__ == '__main__':
    unittest.main()
