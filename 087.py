"""
The smallest number expressible as the sum of a prime square,
prime cube, and prime fourth power is 28. In fact, there are
exactly four numbers below fifty that can be expressed in such
a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the
sum of a prime square, prime cube, and prime fourth power?
"""

from itertools import product, takewhile


def euler(n):
    # Create a candidate list within which non-primes will
    # marked as None, noting that only candidates below
    # sqrt(n) need be checked.
    candidates = list(range(n+1))
    fin = int(n**0.5)

    # Loop over the candidates, marking out each multiple.
    # If the current candidate is already checked off then
    # continue to the next iteration.
    for i in range(2, fin+1):
        if not candidates[i]:
            continue

        candidates[2*i::i] = [None] * (n//i - 1)

    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]


limit = 50000000
primes = euler(int(limit**0.5))
squares = takewhile(lambda x: x < limit, (prime**2 for prime in primes))
cubes = takewhile(lambda x: x < limit, (prime**3 for prime in primes))
tesseracts = takewhile(lambda x: x < limit, (prime**4 for prime in primes))
print((len(set(s + c + t for (s, c, t) in product(squares,
      cubes, tesseracts) if s + c + t < limit))))
