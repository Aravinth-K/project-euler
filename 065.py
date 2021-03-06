"""
The square root of 2 can be written as an infinite continued
fraction.

\sqrt{2} = 1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 +
\dfrac{1}{2 + ...}}}}

The infinite continued fraction can be written, \sqrt{2} =
[1; (2)] indicates that 2 repeats ad infinitum. In a similar
way, \sqrt{23} = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued
fractions for square roots provide the best rational
approximations. Let us consider the convergents for \sqrt{2}.

\begin{align}
&1 + \dfrac{1}{2} = \dfrac{3}{2} \\
&1 + \dfrac{1}{2 + \dfrac{1}{2}} = \dfrac{7}{5}\\
&1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2}}} = \dfrac{17}{12}\\
&1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2}}}} = \dfrac{41}{29}
\end{align}

Hence the sequence of the first ten convergents for \sqrt{2}
are:

1, \dfrac{3}{2}, \dfrac{7}{5}, \dfrac{17}{12}, \dfrac{41}{29},
\dfrac{99}{70}, \dfrac{239}{169}, \dfrac{577}{408},
\dfrac{1393}{985}, \dfrac{3363}{2378}, ...

What is most surprising is that the important mathematical
constant,

e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...]

The first ten terms in the sequence of convergents for e are:

2, 3, \dfrac{8}{3}, \dfrac{11}{4}, \dfrac{19}{7},
\dfrac{87}{32}, \dfrac{106}{39}, \dfrac{193}{71},
\dfrac{1264}{465}, \dfrac{1457}{536}, ...

The sum of digits in the numerator of the 10th convergent is
1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th
convergent of the continued fraction for e.
"""

from itertools import islice


def take(iterable, n):
    return list(islice(iterable, n))


def e():
    yield 2
    k = 1
    while True:
        yield 1
        yield 2*k
        yield 1
        k += 1


def rationalize(frac):
    if len(frac) == 0:
        return (1, 0)
    elif len(frac) == 1:
        return (frac[0], 1)
    else:
        remainder = frac[1:len(frac)]
        (num, denom) = rationalize(remainder)
        return (frac[0] * num + denom, num)


numerator = rationalize(take(e(), 100))[0]
print(sum(int(d) for d in str(numerator)))
