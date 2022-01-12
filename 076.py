"""
It is possible to write five as a sum in exactly six different
ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of
at least two positive integers?
"""

target = 100
ways = [0] * (target + 1)
ways[0] = 1

for i in range(1, target):
    for j in range(i, target + 1):
        ways[j] += ways[j - i]

print(ways[target])
