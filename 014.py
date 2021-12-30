"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def iteration(n):
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = 3*n + 1
    return n


limit = 1000000

seq = {}

for i in range(limit):
    num = i + 1
    count = 1
    while num != 1:
        if seq.get(num, 0) != 0:
            count += seq[num] - 1
            break
        else:
            count += 1
            num = iteration(num)
    seq[i+1] = count

max_value = max(seq.values())

max_keys = [k for k, v in seq.items() if v == max_value]

print(f"Longest chain starts from {max_keys[0]} of length {max_value}")
