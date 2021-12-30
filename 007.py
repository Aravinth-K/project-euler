"""
By listing the first six prime numbers: 2, 3, 5, 7, 11,
and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import log, ceil


def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def find_n_prime(n):
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]


print(find_n_prime(10001))
