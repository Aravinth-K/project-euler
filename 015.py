"""
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# Edge length of n x n grid.
n = 20

# f(m) = binom(2m)(m) = \frac{4m-2}{m}f(m - 1), with f(1) = 2.


def f(m):
    x = 1
    for i in range(m):
        x = int(((4*i + 2)*x)/(i + 1))

    return x


print(f(n))
