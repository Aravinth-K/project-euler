"""
The arithmetic sequence, 1487, 4817, 8147, in which each of
the terms increases by 3330, is unusual in two ways: (i) each
of the three terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or
3-digit primes, exhibiting this property, but there is one
other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three
terms in this sequence?
"""


def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, n):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    primes = []
    for j in range(n + 1):
        if sieve[j]:
            primes.append(j)
    return sieve, primes


def same_digits(n, m):
    return sorted(list(map(int, str(n)))) == sorted(list(map(int, str(m))))


sieve, primes = sieve(10000 + 1)

search_range = [prime for prime in primes
                if ((prime <= 3340) and (prime > 1487))]

for a in search_range:
    b = a + 3330
    c = a + 6660
    if (sieve[b] and sieve[c]):
        if (same_digits(a, b) and same_digits(b, c)):
            print(str(a) + str(b) + str(c))
            break
