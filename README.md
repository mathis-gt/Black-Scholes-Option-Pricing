# Black-Scholes Option Pricing

The algorithm to asign prices to options based on environment parameters.

## Tutorial

In this tutorial, we will demonstrate the use of `Black-Scholes` to price options accurately. For further information on particular methods we recommend reading the various articles on the topic released by investopedia.

Given the parameters:

100, 100, 0.05, 1, 0.2, "call"

We begin by importing the necessary files so we can use the algorithm to find a price of the option depending on which method is chosen to append them. Through this example we will work with a 'call' option.

```python
import math
from scipy.stats import norm
import optionprice as op

    S = 100
    K = 100
    r = 0.05
    T = 1
    sd = 0.2
   c_p = "call" 
```
Where 'S' is the current stock price, 'K' is the strike price, 'r' is the risk-free rate, 'T' is the time to maturity, 'sd' is the satandard deviation (volatility) and c_p is the option type.
```
parameters = [100, 100, 0.05, 1, 0.2, "call"]
op.option_price(parameters)
```

Output:

```
10.450583572185565
```

The algorithm returns the estimated theoretical price of the option based on the Black-Scholes model.

## How to guides

### How to price a call option

A call option gives the holder the right, but not the obligation, to buy an asset at a predetermined strike price.

The pricing method is as follows:

```python
import optionprice as op

op.option_price(100, 100, 0.05, 1, 0.2, "call")
```

This has an output of:

```
10.450583572185565
```

### How to price a put option

A put option gives the holder the right, but not the obligation, to sell an asset at a predetermined strike price.

The same function can be used by changing the final parameter:

```python
import optionprice as op

op.option_price(100, 100, 0.05, 1, 0.2, "put")
```

This would return:

```
5.573526022256971
```

### How to adjust model parameters

The option price can be recalculated under different market conditions by changing the input parameters.

For example:

```python
import optionprice as op

parameters = [120, 100, 0.05, 2, 0.25, "call"]

op.option_price(parameters)
```

This calculates the theoretical price of a call option where:

The stock price is 120.
The strike price is 100.
The risk-free rate is 5%.
The maturity period is 2 years.
The volatility is 25%.

## Explanation

### Reason for Black-Scholes pricing

The Black-Scholes model is a mathematical model used to estimate the theoretical value of European-style options. It is widely used in financial markets because it provides a consistent method of valuing options based on measurable market factors.

The model considers several key variables:

Current stock price.
Strike price.
Time until expiration.
Risk-free interest rate.
Volatility of the underlying asset.

This library uses these inputs to calculate both call and put option prices.

### How its calculated

The Black-Scholes model first calculates two intermediate values, d1 and d2, which are used to estimate the probability of the option finishing in-the-money.

These values are then used with the cumulative distribution function of the standard normal distribution to calculate the final option price.

The call option formula is:

C = S*N(d1) - K*e^(-rT)*N(d2)

The put option formula is:

P = K*e^(-rT)*N(-d2) - S*N(-d1)

Where:

N(x) is the cumulative distribution function of the standard normal distribution.
e represents Euler's number.
The other variables represent the user-defined model inputs.

### Limitations

The Black-Scholes model has several assumptions which can reduce accuracy in real-world situations.

These include:

The model assumes volatility remains constant over the lifetime of the option.
Stock prices are assumed to follow a continuous log-normal distribution.
Transaction costs and taxes are ignored.
The model assumes European-style options which can only be exercised at maturity.
Dividends are not considered without additional adjustments.

Due to these assumptions, the output should be considered a theoretical estimate rather than a guaranteed market price.

## Reference

### List of functions

The following functions are written in `optionprice`:

- `option_price`

### Bibliography

The following resource provides further information on the Black-Scholes model:

Investopedia - Black-Scholes Model
https://www.investopedia.com/terms/b/blackscholes.asp
