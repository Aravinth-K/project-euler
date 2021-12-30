"""
By starting at the top of the triangle below and moving
to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve
      this problem by trying every route. However, Problem 67,
      is the same challenge with a triangle containing one-hundred
      rows; it cannot be solved by brute force, and requires a
      clever method! ;o)
"""

# number of rows
n = 15

# triangle as a list of lists
l = [[] for i in range(n)]

l[0] = [75]
l[1] = [95, 64]
l[2] = [17, 47, 82]
l[3] = [18, 35, 87, 10]
l[4] = [20, 4, 82, 47, 65]
l[5] = [19, 1, 23, 75, 3, 34]
l[6] = [88, 2, 77, 73, 7, 63, 67]
l[7] = [99, 65, 4, 28, 6, 16, 70, 92]
l[8] = [41, 41, 26, 56, 83, 40, 80, 70, 33]
l[9] = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
l[10] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
l[11] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
l[12] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
l[13] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
l[14] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

path = [[] for i in range(n)]

for j in range(n):

    path[j] = [[l[j][i]] for i in range(j+1)]

# sarting at bottom row, find which path maximises the sum going
# to the next row up

for j in range(2, n+1):
    for i in range(n+1-j):
        l[n-j][i] = max((l[n-j][i] + l[n-j+1][i]), (l[n-j][i] + l[n-j+1][i+1]))

# largest sum
print(l[0][0])

for j in range(2, n + 1):
    for i in range(n + 1 - j):
        if (l[n-j][i] + l[n-j+1][i]) > (l[n-j][i] + l[n-j+1][i+1]):
            path[n-j][i] += path[n-j+1][i]
        else:
            path[n-j][i] += path[n-j+1][i+1]

# corresponding path
print(path[0][0])
