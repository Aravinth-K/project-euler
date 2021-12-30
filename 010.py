"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def prime_sieve(n):
    # Using sieve of Eratosthenes, this function computes the
    # set of prime numbers up to an input number n.
    # Parameters:
    # -----------
    # n: int
    #   Upper limit.
    # Returns:
    # -----------
    # prime: list
    #   The list of prime numbers is returned.
    sieve = [True for i in range(n)]
    i = 2
    while i*i <= n:
        if sieve[i]:
            for j in range(2*i, n, i):
                sieve[j] = False
        i += 1
    sieve[0] = False
    sieve[1] = False
    prime = []
    for p in range(n):
        if sieve[p]:
            prime.append(p)
    return(prime)


n = 2000000

print(sum(prime_sieve(n)))
