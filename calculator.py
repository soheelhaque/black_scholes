# Navigate to http://localhost:5000/api/ui/ to access the functions below from a webpage

import math
import scipy.stats

#TODO: change name to calculate_option_price
#TODO: add call/put to JSON
#TODO: add exception handling (ZeroDivisionException etc)
def calculate_call_option_price(model_inputs):
    """Summary of Description of the Function

    Calculates the price of a call option using the Black-Scholes option pricing formula

    Parameters:

    Returns:

    """
    # Unpack model input parameters from JSON
    strike_price = model_inputs.get("strike_price", None)
    option_maturity_years = model_inputs.get("option_maturity_years", None)
    current_price = model_inputs.get("current_price", None)
    volatility_percent = model_inputs.get("volatility_percent", None)
    risk_free_rate_percent = model_inputs.get("risk_free_rate_percent", None)

    d1 = (math.log(current_price / strike_price) + (risk_free_rate_percent / 100 +
                                                    (math.pow(volatility_percent / 100, 2)) / 2) *
          option_maturity_years) / (volatility_percent / 100 * math.pow(option_maturity_years, 0.5))
    d2 = d1 - volatility_percent / 100 * pow(option_maturity_years, 0.5)
    call_price = scipy.stats.norm.cdf(d1)*current_price - \
        scipy.stats.norm.cdf(d2)*strike_price*math.exp(-1*risk_free_rate_percent/100*option_maturity_years)

    return call_price

#TODO: delete function calculate_put_option_price
def calculate_put_option_price(model_inputs):
    """Summary of Description of the Function

    Calculates the price of a put option using the Black-Scholes option pricing formula

    Parameters:

    Returns:

    """
    # Unpack model input parameters from JSON
    strike_price = model_inputs.get("strike_price", None)
    option_maturity_years = model_inputs.get("option_maturity_years", None)
    current_price = model_inputs.get("current_price", None)
    volatility_percent = model_inputs.get("volatility_percent", None)
    risk_free_rate_percent = model_inputs.get("risk_free_rate_percent", None)

    d1 = (math.log(current_price / strike_price) + (risk_free_rate_percent / 100 +
                                                    (math.pow(volatility_percent / 100, 2)) / 2) *
          option_maturity_years) / (volatility_percent / 100 * math.pow(option_maturity_years, 0.5))
    d2 = d1 - volatility_percent / 100 * pow(option_maturity_years, 0.5)
    put_price = scipy.stats.norm.cdf(-d2)*strike_price*math.exp(-1*risk_free_rate_percent/100*option_maturity_years) \
        - scipy.stats.norm.cdf(-d1)*current_price

    return put_price
