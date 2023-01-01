Question: What is the difference between likelihood and probability

Company: Deloitte

**Answer**: Probability is a measure of the likelihood of an event occurring. it is expressed as a number between 0 and 1.
Where 0 indicates the event will not occur and 1 indicates that the event will certainly occur. For example, if we roll a die, the probability of rolling a 6 is 1/6, or approximatelt 0.17.
This means that if we roll the die many times, we would expect to roll a 6 approximately 1 out of every 6 rolls, on average.

Whereas Likelihood refers to the relative probability of one event occuring compared to another event. For example if we have a coin that we know is biased such that it has a probability of 0.8 of landing on head when flipped,
we can say that the likelihood of the coin landing on heads is higher than the likelihood of it landing on tails. In this case, the probability of the coin landing on heads is 0.8, and the probability of it landing on tails is 02, so the likelihood of the coin landing on heads is 4 times higher than the likelihood of it landing on tails.


Below is a Python Implementation

```
from fractions import Fraction

# Probability of event A occurring
prob_a = Fraction(4, 5)
print(f'Probability of A :{prob_a}')
# Probability of event B occurring
prob_b = Fraction(1, 5)
print(f'Probability of B: {prob_b}')
# Calculate the likelihood of event A occurring compared to event B
likelihood = prob_a / prob_b

print(f'Likelihood of Event A occuring compared to event B: {float(likelihood)}')

```