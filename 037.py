"""
The number 3797 has an interesting property. Being prime
itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797,
97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable
primes.
"""


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


def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    i = 5
    while i * i < n:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6
    return True


# prime numbers less than 1 million
primes = prime_sieve(1000000)

result = 0
count = 0

searchList = [3, 7]

left_append = [1, 2, 3, 5, 7, 9]

while (count < 11):
    primeCandidate = searchList[0]
    searchList.pop(0)
    if (isPrime(primeCandidate)):
        isTruncablePrime = True
        n = primeCandidate
        multiplier = 1
        # check right trunacatable
        while n:
            isTruncablePrime = (isPrime(n) and isTruncablePrime)
            n //= 10
            multiplier *= 10
        if (isTruncablePrime and (primeCandidate > 10)):
            result += primeCandidate
            count += 1
        # generate new candidates
        for i in left_append:
            searchList.append(multiplier * i + primeCandidate)

print(result)
