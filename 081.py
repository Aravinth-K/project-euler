"""
In the 5 by 5 matrix below, the minimal path sum from the top
left to the bottom right, by only moving to the right and
down, is indicated in bold red and is equal to 2427.

\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & \color{red}{746} & \color{red}{422} & 111\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}

Find the minimal path sum from the top left to the bottom
right by only moving right and down in matrix.txt (right click
and "Save Link/Target As..."), a 31K text file containing an
80 by 80 matrix.
"""


matrix = []
with open("p081_matrix.txt") as matfile:
    for row in matfile:
        matrix.append([int(n) for n in row.split(',')])

m = len(matrix)

for i in range(1, m):
    matrix[0][i] += matrix[0][i - 1]
    matrix[i][0] += matrix[i - 1][0]

for i in range(1, m):
    for j in range(1, m):
        matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[m - 1][m - 1])
