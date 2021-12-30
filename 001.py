"""
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

max_num = 1000

multiples = []

for i in range(max_num):
    i % 3 == 0 and multiples.append(i)

for i in range(max_num):
    (i % 3 != 0) & (i % 5 == 0) and multiples.append(i)

print(sum(multiples))
