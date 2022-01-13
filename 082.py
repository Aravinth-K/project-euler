"""
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting
in any cell in the left column and finishing in any cell in
the right column, and only moving up, down, and right, is
indicated in red and bold; the sum is equal to 994.

\begin{pmatrix}
131 & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & 746 & 422 & 111\\
537 & 699 & 497 & 121 & 956\\
805 & 732 & 524 & 37 & 331
\end{pmatrix}

Find the minimal path sum from the left column to the right
column in matrix.txt (right click and "Save Link/Target As...")
, a 31K text file containing an 80 by 80 matrix.
"""

matrix = []
with open("p081_matrix.txt") as matfile:
    for row in matfile:
        matrix.append([int(n) for n in row.split(',')])

gridSize = len(matrix)
sol = [0] * gridSize

# initialise solution
for i in range(gridSize):
    sol[i] = matrix[i][gridSize - 1]


for i in range(gridSize - 2, 0 - 1, -1):
    # Traverse down
    sol[0] += matrix[0][i]
    for j in range(1, gridSize):
        sol[j] = min(sol[j - 1] + matrix[j][i], sol[j] + matrix[j][i])

    # Traverse up
    for j in range(gridSize - 2, 0 - 1, -1):
        sol[j] = min(sol[j], sol[j + 1] + matrix[j][i])

print(min(sol))
