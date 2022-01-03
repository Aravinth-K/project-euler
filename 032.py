"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186
= 7254, containing multiplicand, multiplier, and product
is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/
product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
"""

import itertools
products = set()


def makeint(n):
    return int(''.join(map(str, n)))


target = range(1, 10)
d = itertools.permutations(target, 5)
for a in d:
    product = makeint(a[:2])*makeint(a[2:])
    if sorted(list(a)+list(map(int, str(product)))) == sorted(list(target)):
        products.add(product)
    product = makeint(a[:1])*makeint(a[1:])
    if sorted(list(a)+list(map(int, str(product)))) == sorted(list(target)):
        products.add(product)

ans = sum(list(products))
print(ans)
