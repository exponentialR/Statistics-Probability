Question: Assume the distribution of children per family is as given in the table below:

| n_children | 0     | 1      |  2     | 3      |	4    | \>=5 |
|------------|-------| -------| -------| -------| -------|------|
|p	       | 0.3 | 0.25 |0.2| 0.15 | 0.1 | 	0   |

Company: Google

Consider a random girl in the population of children. What is the probability that she has a sister?

**Answer:**

To find the probability that a random girl has a sister, we need to consider the probability of each family size and the probability that the girl is one of the children in that family.

For a family with 0 children, the probability of having exactly two girls is `0`, since it is impossible to have exactly two girls if there are no children.

For a family with 1 child, the probability of having exactly two girls is also `0`, since it is again impossible to have exactly two girls if there is only 1 child.

For a family with 2 children, the probability of having exactly two girls is `1/4`, 
since there is only 1 way for the family to have exactly two girls (both children must be girls) 
out of a total of 4 possible outcomes `GG, GB, BG, BB`.

For a family with 3 children, the probability of having exactly two girls is `4/8`, 
since there are 4 ways for the family to have exactly two girls 
`GGG, GBG, BGG, GGB `out of a total of 8 possible outcomes 

`GGG, GBG, BGG, GGB, GBB, BGB, BBG, BBB`.

For a family with 4 children, the probability of having exactly two girls is `8/16`, since 
there is only 1 way for the family to have exactly two girls out of a total of 16 possible outcomes 

``GGGG, GBGG, BGGG, GGBG, GBBG, BGBG, GGBB, GBBB, BGBB, BBGG, BBBG, BBBG, BBGB, BBBB, BBGB, BBBB.``

For a family with 5 children, the probability of having exactly two girls is 0, since it is impossible to have a family with 5 children.

Pr(girl has a sister) = 

``pr(2) * (1/4) + pr(3) * (1/2) + pr(4) * (1/2) + pr(5 or more) * (4/5)``

``= 0.2 * (1/4) + 0.15 * (1/2) + 0.1 * (1/2)``

`= 0.05 + 0.1 + 0.05`

`= 0.2`

Therefore, the probability that a random girl has a sister is approximately 20%.