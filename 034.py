"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of
the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def factorial_sum(n):
    total = 0
    while n:
        total += FACTORIAL[n % 10]
        n //= 10
    return total


answer = 0
for n in range(10, 1500000):
    if n == factorial_sum(n):
        answer += n
print(answer)
