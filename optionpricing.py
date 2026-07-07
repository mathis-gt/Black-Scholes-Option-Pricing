#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def option_price(S, K, r, T, sd, c_p):
    """
    A model for option pricing based on various inputs.
    Changes based on whether it is a 'call' or 'put' option.

    Parameters:
    ∼ S ∼ current stock price.
    ∼ K ∼ strike price.
    ∼ r ∼ risk-free rate.
    ∼ T ∼ time to maturity.
    ∼ sd ∼ standard deviation (volatility).
    ∼ c_p ∼ standard normal CDF.
    
    Returns:
    Estimated price of the option based on the Black-Scholes model.
    """
    d1 = (math.log (S / K) + ((r + (0.5 * (sd ** 2))) * T)) / (sd * (T ** 0.5))
    
    d2 = d1 - (sd * (T ** 0.5))
    
    C = (S * norm.cdf(d1)) - (K * math.exp(-1 * r * T) * norm.cdf(d2))
    
    P = (K * math.exp(-1 * r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
    
    if c_p.lower() == "call":
        return float(C)
    
    elif c_p.lower() == "put":
        return float(P)
    
    else:
        raise ValueError("Last variable must be 'call or 'put'.")

