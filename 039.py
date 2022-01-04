"""
If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions
maximised?
"""

max = 0
maxp = 0
for p in range(2, 1000 + 1, 2):
    c = 0
    for a in range(2, p//3):
        if (p * (p - 2 * a) % (2 * (p - a)) == 0):
            c += 1
    if (c > max):
        max = c
        maxp = p

print(maxp)
