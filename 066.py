"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 –
13×1802 = 1.

It can be assumed that there are no solutions in positive
integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we
obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the
largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which
the largest value of x is obtained.
"""

from math import sqrt

result = 0
pmax = 0

for D in range(2, 1000 + 1):

    limit = int(sqrt(D))

    if (limit * limit == D):
        continue

    m = 0
    d = 1
    a = limit
    numm1 = 1
    num = a
    denm1 = 0
    den = 1

    while (num*num - D*den*den != 1):
        m = ((d * a) - m)
        d = (D - (m * m)) // d
        a = (limit + m) // d

        numm2 = numm1
        numm1 = num
        denm2 = denm1
        denm1 = den

        num = ((a*numm1) + numm2)
        den = ((a * denm1) + denm2)

    if (num > pmax):
        pmax = num
        result = D

print(result)
