Question: What is the Probability Density Function of  Z = max(X,Y) where X, Y ∼ U(0, 1)?

Company: Goldman Sachs

**Answer:**
The probability density function (PDF) of the maximum of two random variables is given by:

`f_Z(z) = f_X(z) + f_Y(z) - f_{X,Y}(z,z)
`
where f_X(z) and f_Y(z) are the PDFs of X and Y, respectively, and `f_{X,Y}(z,z)` is the joint PDF of `X` and `Y` evaluated at `(z,z)`.

In this case, X and Y are uniformly distributed over the interval `(0, 1)`, so their PDFs are both equal to 1. The joint PDF of X and Y is also equal to 1 over the region `(0,1) x (0,1)`, so we can plug these values into the formula above to find the PDF of Z:

`f_Z(z) = 1 + 1 - 1 = 1`

This means that the `PDF` of `Z` is always equal to `1`, regardless of the value of `z`. This means that Z is also uniformly distributed over the interval `(0,1)`.