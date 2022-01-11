"""
Euler's Totient function, φ(n) [sometimes called the phi
function], is used to determine the number of positive numbers
less than or equal to n which are relatively prime to n. For
example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every
positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109
is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a
permutation of n and the ratio n/φ(n) produces a minimum.
"""


def prime_sieve(lower_bound, upper_bound):
    sieve = [True] * (upper_bound + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, upper_bound):
        if sieve[p]:
            for i in range(p * p, upper_bound + 1, p):
                sieve[i] = False
    primes = []
    for j in range(lower_bound, upper_bound + 1):
        if sieve[j]:
            primes.append(j)
    return primes


def is_perm(n, m):
    return sorted(list(map(int, str(n)))) == sorted(list(map(int, str(m))))


best = 1
phiBest = 1
bestRatio = float('inf')

limit = 10000000
lower_bound = 2000
upper_bound = 5000
primes = prime_sieve(lower_bound, upper_bound)

for i in range(0, len(primes)):
    for j in range(i + 1, len(primes)):
        n = primes[i] * primes[j]
        if (n > limit):
            break
        phi = (primes[i] - 1) * (primes[j] - 1)
        ratio = n / phi

        if (is_perm(n, phi) and (bestRatio > ratio)):
            best = n
            phiBest = phi
            bestRatio = ratio

print(best)
