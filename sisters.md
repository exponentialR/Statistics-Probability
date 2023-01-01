Question:Assume that in large city; the distribution of the number of children per family is as follows: Number of children Proportion families with n children 0.15 0.20 0.25 0.25 0.10 0.05 Assume that each child in family is a boy or a girl with probability 1/2, independently: If a family is picked at random; what is the chance that this family has exactly two girls? 

Company: Anonymous

**Answer**: 
To find the probability that a family picked at random has exactly two girls, we need to consider the probability that a family has two girls given that it has 0, 1, 2, 3, 4, or 5 children.

For a family with 0 children, the probability of having exactly two girls is `0`, since it is impossible to have exactly two girls if there are no children.

For a family with 1 child, the probability of having exactly two girls is also `0`, since it is again impossible to have exactly two girls if there is only 1 child.

For a family with 2 children, the probability of having exactly two girls is `1/4` since there is only 1 way for the family to have exactly two girls (both children must be girls) 
out of a total of 4 possible outcomes (`GG, GB, BG, BB`).

For a family with 3 children, the probability of having exactly two girls is `3/8`, since there are 3 ways for the family to have exactly two girls 
(`GBG, BGG, GBB`) out of a total of 8 possible outcomes (`GGG, GBG, BGG, GGB, GBB, BGB, BBG, BBB`).

For a family with 4 children, the probability of having exactly two girls is `1/4`, since there is only 1 way for the family to have exactly two girls (GBBB) out of a total of 16 possible outcomes 
(`GGGG, GBGG, BGGG, GGBG, GBBG, BGBG, GGBB, GBBB, BGBB, BBGG, BBBG, BBBG, BBGB, BBBB, BBGB, BBBB`).

For a family with 5 children, the probability of having exactly two girls is 0, since it is impossible to have exactly two girls if there are 5 children.

To find the overall probability that a family picked at random has exactly two girls, we need to weight the probability for each number of children by the proportion of families with that number of children and add them up. This gives us:

`(0.15 * 0) + (0.20 * 0) + (0.25 * 1/4) + (0.25 * 3/8) + (0.10 * 1/4) + (0.05 * 0) = 0.0625`

So the probability that a family picked at random has exactly two girls is approximately 0.0625.

`(b)` If a child is picked at random from the children of this population, what is the chance that the child comes from family with exactly two girls?

**Answer (b) :**
To find the probability that a child picked at random comes from a family with exactly two girls, we can use the following formula:

P(Child comes from family with exactly two girls) = P(Child comes from family with exactly two girls | Family has 2 children) * P(Family has 2 children) + P(Child comes from family with exactly two girls | Family has 3 children) * P(Family has 3 children) + P(Child comes from family with exactly two girls | Family has 4 children) * P(Family has 4 children)

Plugging in the values that we calculated earlier, we get:

P(Child comes from family with exactly two girls) = `(1/2) * (0.25) + (1/3) * (0.25) + (1/4) * (0.10) = 0.0708`

This means that the probability that a child picked at random comes from a family with exactly two girls is approximately 0.0708.

`(c)` If a girl is picked at random from the girl children of this population, what is the chance that the girl comes from family with exactly two girls, i.e , she has exactly one sister?

**Answer (b) :**
To find the probability that a girl picked at random comes from a family with exactly one sister, we can use the following formula:

P(Girl comes from family with exactly one sister) = P(Girl comes from family with exactly one sister | Family has 2 children) * P(Family has 2 children) + P(Girl comes from family with exactly one sister | Family has 3 children) * P(Family has 3 children) + P(Girl comes from family with exactly one sister | Family has 4 children) * P(Family has 4 children)

Since a girl picked at random must come from a family with at least one girl, we know that the probability that she comes from a family with exactly one sister is equal to the probability that she comes from a family with 2 children (where she is the only girl) plus the probability that she comes from a family with 3 children (where she is one of two girls) plus the probability that she comes from a family with 4 children (where she is one of three girls).

Plugging in the values that we calculated earlier, we get:

P(Girl comes from family with exactly one sister) = (1/2) * (0.25) + (2/3) * (0.25) + (3/4) * (0.10) = 0.1701

This means that the probability that a girl picked at random comes from a family with exactly one sister is approximately 0.1701.