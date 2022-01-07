"""
The first two consecutive numbers to have two distinct
prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct
prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four
distinct prime factors each. What is the first of these
numbers?
"""

# number of prime factors and successive integers
target = 4
# arbitrary upper-bound found by trial and error
limit = 150000
# the number of prime divisors of each integer considered
n_prime_divisors = [0] * limit
# length of the current run of valid integers
run_length = 0
for n in range(2, limit):
    if n_prime_divisors[n] == 0:
        # n is prime, sieve out multiples of n
        for m in range(2 * n, limit, n):
            # m is divisible by n (prime)
            n_prime_divisors[m] += 1
        # n is invalid, reset our run counter
        run_length = 0
    elif n_prime_divisors[n] == target:
        # n is valid, increment our run counter
        run_length += 1
    else:
        # n is invalid, reset our run counter
        run_length = 0

    if run_length == target:
        # we've found the smallest target run
        answer = n - target + 1
print(answer)
