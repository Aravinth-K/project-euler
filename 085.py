"""
By counting carefully it can be seen that a rectangular grid
measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains
exactly two million rectangles, find the area of the grid with
the nearest solution.
"""

error = float('inf')
closestArea = 0
target = 2000000

n = 2000
m = 1

while (n >= m):
    rects = n * (n + 1) * m * (m + 1) / 4

    if (error > abs(rects - target)):
        closestArea = n * m
        error = abs(rects - target)

    if (rects > target):
        n -= 1
    else:
        m += 1

print(closestArea)
