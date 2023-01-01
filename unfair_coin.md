Question: How do you make an unfair coin fair?
Company: Google
Answer: 
1. Flip the coin multiple times; say for 20 times.  Since the coin is unfair, it is guaranteed that the results will come up unequal.  So, flipping 20 times could generate the following results:

```
H H T T T H T T H T T H T T T T H T H T H T T 

```

13 tails and 7 Tails are generated as outcome. 

Hence probability of Heads in 20 flips of the unfair coin:

```
pr(H) = 7/20
          = 0.35
```

and probability of Tails :

```
Pr(T) = 13/20
         = 0.65
```

2. Now using the probabilities of the unfair coins you can generate new set of flips which are guaranteed to be fair. One way to do this is to use a random number generator to simulate the flips of the unfair coin, and using the calculated probabilities as the weights. For example, you might generate a random number between 0 and 1. If the number is less than 0.65, you would consider that a "tails" flip. If the number is greater than or equal to 0.65, you would consider it a "tails" flip. You can repeat this process as many times as you like to generate as many fair flips as you need.

Below is a Python Code to do this:


````
import random

def reweighting(flips):
    """
    Reweights an unfair coin based on a list of flips
    
    Args:
        flips: List A list of flips, where each element is either Head or Tail.
        
    Returns:
            List [str] a list of flips that is guaranteed to be fair
    """
    
    heads = flips.couunt('H')
    tails = flips.count('T')
    
    probability_heads = heads / (heads + tail)
    probability_tails = tails / (heads + tail)
    
    new_flips = []
    
    for i in range(heads + tails):
        if random.random() < probability_heads:
            new_flips.append('H')
        else:
            new_flips.append('T')
    
    return new_flips
    

````