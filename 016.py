"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""


def exp_by_squaring(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_squaring(x*x, int(n/2))
    else:
        return x*exp_by_squaring(x*x, int((n-1)/2))


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


print(sum_digits(exp_by_squaring(2, 1000)))
