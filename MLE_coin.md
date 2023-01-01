Question: Suppose you flip a (biased) coin N times and it lands heads K times. Can you derive the Maximum Likelihood estimator of the coin’s probability of landing heads?

Company: Amazon

**Answer :**

the Maximum Likelihood estimator (MLE) of the coin's probability of landing heads can be derived as follows:

Let's assume that the probability of the coin landing heads is p. Then the probability of the coin landing tails is 1 - p.

If the coin is flipped N times and lands heads K times, the probability of this occurring is given by the binomial distribution:

P(K heads in N flips) = `(N choose K) * p^K * (1-p)^(N-K)`

The MLE is the value of p that maximizes this probability. To find this maximum, we can take the derivative of the equation with respect to p and set it equal to 0:

`d/dp [(N choose K) * p^K * (1-p)^(N-K)] = 0`

Solving this equation for p gives us:

`p = K/N`

Therefore, the MLE for the probability of the coin landing heads is K/N, where K is the number of times the coin landed heads in N flips.
