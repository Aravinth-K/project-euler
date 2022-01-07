"""
By replacing the 1st digit of the 2-digit number *3, it turns
out that six of the nine possible values: 13, 23, 43, 53, 73,
and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same
digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is
the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part
of an eight prime value family.
"""

from itertools import combinations


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


limit = 1000000

sieve, primes = prime_sieve(limit)

found = False

for prime in primes:
    str_digit = list(str(prime))
    length = len(str_digit)
    for i in range(1, length + 1):
        if found:
            break
        for combination in combinations(range(length), i):
            test = True
            for k in combination:
                test = (test and (str_digit[k] ==
                                  str_digit[combination[0]]))
            if not test:
                continue
            count = 1
            for j in range(1, 9 + 1):
                value = str_digit.copy()
                for k in combination:
                    value[k] = str(j)
                num = int(''.join(value))
                if sieve[num] and num != prime:
                    count += 1
            if count == 8:
                found = True
                result = prime
                break

print(result)
