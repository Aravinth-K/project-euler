"""
We shall say that an n-digit number is pandigital if it makes
use of all the digits 1 to n exactly once. For example, 2143
is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# 7 & 4 digit give prime pandigitals


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


def is_pandigital(n):
    num = str(n)
    digits = len(num)
    target = range(1, digits + 1)
    return sorted(list(map(int, num))) == sorted(list(target))


primes = prime_sieve(7654321 + 1)
max_value = 0
for i in range(len(primes)):
    if is_pandigital(primes[len(primes) - i - 1]):
        max_value = primes[len(primes) - i - 1]
        break

print(max_value)
