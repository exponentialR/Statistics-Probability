Question: How to draw a uniform random sample from a circle in polar coordinates?

Company: Lyft

**Answer:**
To draw a uniform random sample from a circle with radius r in polar coordinates, you can follow these steps:

Generate two random numbers `x` and `y` from a uniform distribution between `0` and `1`.
Convert `x` and `y` to polar coordinates `(r, theta)`, where r is the radius of the circle and theta is the angle in radians.
Set r equal to the radius of the circle and theta equal to `2 * pi * y`.
Here is some example Python code that demonstrates this process:

```
import random
import math

def sample_from_circle(r):
  x = random.uniform(0, 1)
  y = random.uniform(0, 1)
  theta = 2 * math.pi * y
  return (r, theta)

r = 1  # radius of the circle
sample = sample_from_circle(r)
print(sample)  # prints a random point on the circle with radius r```
