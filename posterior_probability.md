Question: Define posterior probability

Company: Deloitte

Answer:
In probability theory and statistical inference, 
the posterior probability is the probability of an event occurring, 
given that some evidence has already been observed. 
It is calculated using Bayes' theorem, which states 
that the posterior probability of an event is equal to the 
product of the prior probability of the event and the likelihood of the evidence, 
divided by the marginal probability of the evidence. 
The posterior probability is a type of conditional probability, 
since it is the probability of an event occurring given the occurrence of some other event.

For example, suppose you are trying to determine the probability that a patient has a certain disease, 
given that they have tested positive for a certain biomarker. 
The prior probability is the probability of the patient having the disease before the test results are known. 
The likelihood is the probability of the patient testing positive for the biomarker given that they have the disease. 
The marginal probability is the overall probability of the patient testing positive for the biomarker, 
regardless of whether they have the disease. The posterior probability is the 
revised probability of the patient having the disease after taking into account the test results.

Below is a sample code:

````

def posterior_probability(prior, likelihood, marginal):
  return (prior * likelihood) / marginal

# Example:
prior = 0.1 # probability of disease before test
likelihood = 0.8 # probability of positive test given disease
marginal = 0.2 # overall probability of positive test

posterior = posterior_probability(prior, likelihood, marginal)
print(posterior) # 0.4

````

This code calculates the posterior probability of a patient having a certain disease, 
given that they have tested positive for a certain biomarker. 
The prior probability is the probability of the patient having the disease before the test results are known, 
the likelihood is the probability of the patient testing positive for the biomarker given that they have the disease, 
and the marginal probability is the overall probability of the patient testing positive for the biomarker, 
regardless of whether they have the disease. 
The posterior probability is then calculated by multiplying the prior probability by the likelihood, 
and dividing the result by the marginal probability.