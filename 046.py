"""
It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as
the sum of a prime and twice a square?
"""

from math import sqrt


def is_twice_square(n):
    square_test = sqrt(n/2)
    return square_test.is_integer()


def prime_sieve(n):
    sieve = [True for i in range(n)]
    upper_bound = len(sieve)
    i = 2
    while i < n:
        if sieve[i]:
            for j in range(2*i, upper_bound, i):
                sieve[j] = False
        i += 1
    sieve[0] = False
    sieve[1] = False
    prime = []
    for p in range(upper_bound):
        if sieve[p]:
            prime.append(p)
    return(prime)


primes = prime_sieve(10000)
result = 1
not_found = True
while not_found:
    result += 2
    j = 0
    not_found = False
    while (result >= primes[j]):
        if (is_twice_square(result - primes[j])):
            not_found = True
            break
        j += 1

print(result)
