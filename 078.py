"""
Let p(n) represent the number of different ways in which n
coins can be separated into piles. For example, five coins can
be separated into piles in exactly seven different ways, so p
(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one
million.
"""

# Using generating function for partitions

from itertools import accumulate, count, cycle


def pentagonal():
    """
    Generate the generalized pentagonal numbers starting at 1.
    """
    return accumulate(k if k % 2 else k // 2 for k in count(1))


def partitions_modulo(m):
    """Generate the partition numbers modulo m.
    """
    signs = 1, 1, -1, -1
    partitions = [1]          # Partition numbers up to p(n)
    pentagonals = []          # Generalized pentagonal numbers <= n
    pentagonal_it = pentagonal()
    next_pentagonal = next(pentagonal_it)

    yield 1
    for n in count(1):
        if next_pentagonal <= n:
            pentagonals.append(next_pentagonal)
            next_pentagonal = next(pentagonal_it)
        p = sum(sign * partitions[-pent]
                for sign, pent in zip(cycle(signs), pentagonals)) % m
        partitions.append(p)
        yield p


m = 10**6

result = next(i for i, p in enumerate(partitions_modulo(m)) if p % m == 0)

print(result)
