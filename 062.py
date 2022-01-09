"""
The cube, 41063625 (345^3), can be permuted to produce two
other cubes: 56623104 (384^3) and 66430125 (405^3). In fact,
41063625 is the smallest cube which has exactly three
permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of
its digits are cube.
"""

from collections import defaultdict
def cube(x): return x**3


cubes = defaultdict(list)
for i in range(10000):
    c = cube(i)
    digits = ''.join(sorted([d for d in str(c)]))
    cubes[digits].append(c)
print(min([min(v) for k, v in list(cubes.items()) if len(v) == 5]))
