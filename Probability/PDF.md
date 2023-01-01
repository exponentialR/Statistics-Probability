Question: Can values of PDF be greater than 1? if so, how do we interpret PDF?

Company: Google

**Answer**: The proabibility density function is a function
that describes the probability of a continous random variable taking on a particular value.
The value of the PDF can range from 0 to infinity, but the area under the PDF curve must always be equal to 1.
This is because the PDF represents the probability of a continuous random variable falling within a certain range of values, 
and the sum of the probabilities of all possible values of the random variable must be equal to 1.

The PDF can take on values greater than 1, but this does not mean that the probability of
the random variable taking on a particular value is greater than 1. Instead, it indicates that the probability 
of the random variable falling within a certain range of values is relatively high. 
For example, if the PDF of a random variable has a high peak at a particular value, 
this indicates that the probability of the random variable taking on a value near that peak is relatively high.

In general, the PDF can be though of as a way to represent the probability distribution of a continuous random variable. 
It can be used to calculate probabilities and to make prediction about the behaviour of the random varibale.

The probability density function (PDF) of a continuous random variable is defined as:

``
f(x) = (1/sigma * sqrt(2 * pi)) * exp(-0.5 * ((x - mu)/sigma)^2)
``

Where:

`f(x)` is the probability density at the value x
`mu` is the mean of the distribution
`sigma` is the standard deviation of the distribution
`pi` is the mathematical constant approximately equal to` 3.14159`

Here is a Python Implementation of PDF:

````
import numpy as np

# Define the probability density function
def pdf(x, mu, sigma):
  return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu)/sigma)**2)

# Define the mean and standard deviation of the distribution
mu = 0
sigma = 1

# Calculate the probability of the random variable taking on the value x
x = 0
probability = pdf(x, mu, sigma)
print(probability)

````