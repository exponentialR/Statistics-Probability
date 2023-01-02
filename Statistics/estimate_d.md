Question: Given n samples from a uniform distribution `[0, d]`, how to estimate d?

Company: Spotify 

**Answer:**
Estimating d means finding the upper bound of a uniform distribution. This can be achieved in 2 different ways.

(1) Using the maximum of the n samples as an estimate of d:
This method is based on the idea that the maximum value of the samples is the highest possible value that can be drawn from the distribution, and therefore it is an upper bound on the range of the distribution. To use this method, you would simply find the maximum value among the n sample and use that as your estimate for d.

(2) Using the sample mean and sample standard deviation to calculate an estimate value for d:
This method is based on the fact that the sample mean and sample standard deviation can be used to provide a "central tendency" and "spread" for the sample data, respectively. By combining these two quantities and adjusting the level of confidence you want in your estimate, you can calculate an estimated value for d.

To calculate the sample mean, you would take the sum of all the samples and divide by n. For example, if you have `5` samples with the following values: `2, 4, 6, 8, 10`, the sample mean would be `(2+4+6+8+10)/5 = 6`.

To calculate the sample standard deviation, you would first calculate the difference between each sample and the sample mean, square those differences, and sum them up. Then, you would divide that sum by `(n-1)` and take the square root of the result. Using the same example as above, the sample standard deviation would be calculated as follows:

`( ( (2-6)^2 + (4-6)^2 + (6-6)^2 + (8-6)^2 + (10-6)^2 ) / (5-1) )^(1/2) = 4
`

Once you have calculated the sample mean and sample standard deviation you can use the following formula to estimate `d`:

`d = sample mean + (k * sample standard deviation) `

Where k is a constant that determines the level of confidence you want in your estimate. For example, if you want to be 95% confident in your estimate of d, you can use `k=2`. This is because, for a normal distribution (which the sample mean and standard deviation are often used to approximate), approximately `95%` of the data lies within 2 standard deviations of the mean.
