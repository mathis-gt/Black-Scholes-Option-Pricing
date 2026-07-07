#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import optionprice as op

def test_op():
    """
    This tests if the option pricing model gives a valid result.
    For both a 'call' and 'put' option.
    
    Parameters:
    S = 100
    K = 100
    r = 0.05
    T = 1
    sd = 0.2

    Expected results (Black-Scholes):
    Call ≈ 10.4506
    Put ≈ 5.5735
    """
    S = 100
    K = 100
    r = 0.05
    T = 1
    sd = 0.2

    call_output = round(option_price(S, K, r, T, sd, "call"), 4)
    put_output = round(option_price(S, K, r, T, sd, "put"), 4)

    expected_call = 10.4506
    expected_put = 5.5735

    if call_output == expected_call and put_output == expected_put:
        return "Verified Result"

    if call_output != expected_call or put_output != expected_put:
        return "Mismatch detected"

test_op()

