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
