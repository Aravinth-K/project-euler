"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n!/(r!(n - r)!), where r <= n, n! = n x (n-1)
x ... x 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million:
23C10 = 11440066.

How many, not necessarily distinct, values of nCr for
1 <= n <= 100, are greater than one-million?
"""

num_rows = 100
pascal = [[1]*(i+1) for i in range(num_rows + 1)]
for i in range(num_rows + 1):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
count = 0
for sub_list in pascal:
    for element in sub_list:
        if element > 1000000:
            count += 1
print(count)
