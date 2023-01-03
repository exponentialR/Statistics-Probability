Question: You randomlu draw a coin from 100 coins - 1 unfair coin(head-head), 99 fair coins (head-tail) and rollit 10 times . If the result is 10 heads, what is the probability that the coin is unfair?

Company: Meta

**Answer:**
The probability that the unfair coin will land on heads 10 times in a row is 1, because the unfair coin always lands on heads. The probability that a fair coin will land on heads 10 times in a row is very small, approximately 0.5^10, or about 0.098. Therefore, the probability that the unfair coin was chosen, given that it landed on heads 10 times in a row, is about 90.9%.

To be more precise, we can use Bayes' theorem to calculate the probability that the unfair coin was chosen, given that it landed on heads 10 times in a row. Bayes' theorem states that:

P(A|B) = (P(B|A) * P(A)) / P(B)

Where A is the event that the unfair coin was chosen, B is the event that the coin landed on heads 10 times in a row, P(A|B) is the probability of event A given that event B has occurred, P(B|A) is the probability of event B given that event A has occurred, P(A) is the probability of event A, and P(B) is the probability of event B.

Plugging in the values, we get:

`P(unfair coin was chosen | coin landed on heads 10 times in a row)` 

= `(1 * 1/100) / (1/100 + 0.098 * 99/100) = 90.9%`