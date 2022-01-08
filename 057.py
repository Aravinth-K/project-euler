"""
It is possible to show that the square root of two can be
expressed as an infinite continued fraction.

By expanding this for the first four iterations, we get:

3/2 = 1.5
7/5 = 1.4
17/12 = 1.41666...
41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but
the eighth expansion, 1393/985, is the first example where the
number of digits in the numerator exceeds the number of digits
in the denominator.

In the first one-thousand expansions, how many fractions
contain a numerator with more digits than the denominator?
"""


def num_digits(n):
    result = 0
    while n:
        result += 1
        n //= 10
    return result


count = 0
n, d = 1, 1
for k in range(1000):
    n, d = (2 * d) + n, d + n
    if num_digits(n) > num_digits(d):
        count += 1
print(count)
