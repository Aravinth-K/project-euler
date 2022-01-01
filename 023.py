"""
A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper
divisorsis less than n and it is called abundant if this
sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant
numbers is 24. By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of
two abundant numbers. However, this upper limit cannot be
reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two
abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.
"""


def prime_sieve(n):
    sieve = [True for i in range(n) if (i * i < n)]
    upper_bound = len(sieve)
    i = 2
    while i*i <= n:
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


def div_count(n):
    original_number = n
    count = 1
    if n < 4:
        return 1
    for i in range(len(primes)):
        p = primes[i]
        if n % p == 0:
            t = p*p
            n //= p
            while n % p == 0:
                t *= p
                n //= p
            count *= (t - 1)//(p - 1)
        if p * p > n:
            break
    if n > 1:
        count *= (n + 1)
    return count - original_number


primes = prime_sieve(28123)
abundant_subspace = set()
answer = 0
for n in range(1, 28123 + 1):
    if div_count(n) > n:
        abundant_subspace.add(n)
    if not any((n - a in abundant_subspace) for a in abundant_subspace):
        # The any operator provides lazy evaluation, terminating on
        # the first satisfied condition
        answer += n
print(answer)
