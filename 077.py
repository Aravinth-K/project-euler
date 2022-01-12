"""
It is possible to write ten as the sum of primes in exactly
five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of
primes in over five thousand different ways?
"""


def prime_sieve(n):
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
    return primes


upper_bound = 100000

primes = prime_sieve(upper_bound)

ways = [0]

target = 10

while ways[len(ways) - 1] < 5000:
    ways = [0] * (target + 1)
    ways[0] = 1
    prime_set = [n for n in primes if (n <= target)]
    for i in range(len(prime_set)):
        j = prime_set[i]
        while j <= target:
            ways[j] += ways[j - prime_set[i]]
            j += 1
    target += 1

print(target - 1)
