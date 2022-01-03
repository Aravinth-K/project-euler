"""
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11,
13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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


def rotation(number):
    str_number = str(number)
    return {
        int(str_number[i:] + str_number[:i])
        for i in range(len(str_number))
    }


primes = prime_sieve(1000000)

total = 0

for prime in primes:
    for n in rotation(prime):
        if isPrime(n) is False:
            break
    else:
        total += 1

print(total)
