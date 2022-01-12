"""
It is well known that if the square root of a natural number
is not an integer, then it is irrational. The decimal
expansion of such square roots is infinite without any
repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the
digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of
the digital sums of the first one hundred decimal digits for
all the irrational square roots.
"""

# Using square root by subtraction, by Frazer Jarvis


def squareRoot(n, digits):
    limit = 10 ** (digits + 1)
    a = 5 * n
    b = 5

    while (b < limit):
        if (a >= b):
            a -= b
            b += 10
        else:
            a *= 100
            b = (b//10) * 100 + 5

    return b//100


def digitSum(n):
    count = 0
    while n:
        count += (n % 10)
        n //= 10
    return count


squares = [k * k for k in range(1, 10 + 10)]

result = 0
for n in range(1, 100 + 1):
    if n in squares:
        continue
    result += digitSum(squareRoot(n, 100))

print(result)
