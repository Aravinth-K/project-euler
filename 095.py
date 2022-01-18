"""
The proper divisors of a number are all the divisors excluding
the number itself. For example, the proper divisors of 28 are
1, 2, 4, 7, and 14. As the sum of these divisors is equal to
28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and
the sum of the proper divisors of 284 is 220, forming a chain
of two numbers. For this reason, 220 and 284 are called an
amicable pair.

Perhaps less well known are longer chains. For example,
starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called
an amicable chain.

Find the smallest member of the longest amicable chain with no
element exceeding one million.
"""


def solution(L=1000000):
    d = [1] * L
    for i in range(2, L//2):
        for j in range(2*i, L, i):
            d[j] += i

    max_cl = 0
    for i in range(2, L):
        n, chain = i, []
        while d[n] < L:
            d[n], n = L+1, d[n]
            try:
                k = chain.index(n)
            except ValueError:
                chain.append(n)
            else:
                if len(chain[k:]) > max_cl:
                    max_cl, min_link = len(chain[k:]), min(chain[k:])
    return min_link


print(solution())
