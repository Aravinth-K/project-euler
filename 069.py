"""
Euler's Totient function, φ(n) [sometimes called the phi
function], is used to determine the number of numbers less
than n which are relatively prime to n. For example, as 1, 2,
4, 5, 7, and 8, are all less than nine and relatively prime to
nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1	    2
3	1, 2	            2	    1.5
4	1, 3	            2	    2
5	1, 2, 3, 4	        4	    1.25
6	1, 5	            2	    3
7	1, 2, 3, 4, 5, 6	6     	1.1666...
8	1, 3, 5, 7	        4	    2
9	1, 2, 4, 5, 7, 8	6	    1.5
10	1, 3, 7, 9	        4	    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
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


result = 1
primes = prime_sieve(200)
i = 0
limit = 1000000

while (result * primes[i] < limit):
    result *= primes[i]
    i += 1

print(result)
