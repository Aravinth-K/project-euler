"""
A googol (10^100) is a massive number: one followed by
one-hundred zeros; 100^100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of
the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100,
what is the maximum digital sum?
"""


def digit_sum(n):
    result = 0
    while n:
        result += (n % 10)
        n //= 10
    return result


max_sum = 1
for power in range(100):
    for number in range(2, 100):
        max_sum = max(max_sum, digit_sum(number ** power))
print(max_sum)
