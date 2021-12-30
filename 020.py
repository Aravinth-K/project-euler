"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def range_prod(lo, hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo, mid) * range_prod(mid+1, hi)
    if lo == hi:
        return lo
    return lo*hi


def factorial(n):
    if n < 2:
        return 1
    return range_prod(1, n)


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


x = factorial(100)

y = sum_digits(x)

print(y)
