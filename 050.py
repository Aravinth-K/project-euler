"""
The prime 41, can be written as the sum of six consecutive
primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a
prime below one-hundred.

The longest sum of consecutive primes below one-thousand that
adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of
the most consecutive primes?
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
    return sieve, primes


LIMIT = 1000000

sieve, primes = prime_sieve(LIMIT)

max_sum = 0
max_run = -1
for i in range(len(primes)):
    total_sum = 0
    for j in range(i, len(primes)):
        total_sum += primes[j]
        if (total_sum > LIMIT):
            break
        if (sieve[total_sum] and (total_sum > max_sum)
                and j - i > max_run):
            max_run = j - i
            max_sum = total_sum
print(max_sum)
