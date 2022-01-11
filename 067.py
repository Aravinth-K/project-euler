"""
By starting at the top of the triangle below and moving to
adjacent numbers on the row below, the maximum total from top
to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'), a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It
is not possible to try every route to solve this problem, as
there are 299 altogether! If you could check one trillion
(1012) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to
solve it. ;o)
"""


def get_triangle(triangle_filename):
    """Return a list of lists containing rows of the triangle."""
    triangle = open(triangle_filename).read().strip().split('\n')
    triangle = [[int(number) for number in row.split()] for row in triangle]
    return triangle


triangle = get_triangle('p067_triangle.txt')

n = len(triangle)

path = [[] for i in range(n)]

for j in range(n):

    path[j] = [[triangle[j][i]] for i in range(j+1)]

for j in range(2, n+1):
    for i in range(n+1-j):
        triangle[n-j][i] = max((triangle[n-j][i] + triangle[n-j+1][i]),
                               (triangle[n-j][i] + triangle[n-j+1][i+1]))

# largest sum
print(triangle[0][0])

for j in range(2, n + 1):
    for i in range(n + 1 - j):
        if (triangle[n-j][i] + triangle[n-j+1][i]) > \
                (triangle[n-j][i] + triangle[n-j+1][i+1]):
            path[n-j][i] += path[n-j+1][i]
        else:
            path[n-j][i] += path[n-j+1][i+1]

# corresponding path
print(path[0][0])
