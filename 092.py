"""
A number chain is created by continuously adding the square of
the digits in a number to form a new number until it has been
seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck
in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


def square_sum_digits(n):
    s = 0
    while n:
        s, n = s + (n % 10)**2, n // 10
    return s


def unhappy(n):
    while n > 1 and n != 89 and n != 4:
        n = square_sum_digits(n)
    return n > 1


L = 7  # Limit is expressed as 10^L

Lc = 9**2 * L + 1  # maximum sum of digits square for L digits (plus 1)

t = [0] * Lc

solutions = [0] * Lc

for i in range(10):
    solutions[i*i] = 1

for i in range(2, L+1):
    for j in range(Lc):
        t[j] = sum(solutions[j - k*k] for k in range(10) if k*k <= j)
    solutions = list(t)

print(sum(solutions[i] for i in range(1, Lc) if unhappy(i)))
