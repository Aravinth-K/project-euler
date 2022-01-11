"""
The number 145 is well known for the property that the sum of
the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the
longest chain of numbers that link back to 169; it turns out
that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will
eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms,
but the longest non-repeating chain with a starting number
below one million is sixty terms.

How many chains, with a starting number below one million,
contain exactly sixty non-repeating terms?
"""

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def FacSum(n):
    temp = n
    facsum = 0
    while (temp > 0):
        facsum += f[temp % 10]
        temp //= 10
    return facsum


limit = 1000000
result = 0
seqlengths = [0] * (limit + 1)
seqlengths[169] = 3
seqlengths[363601] = 3
seqlengths[1454] = 3
seqlengths[871] = 2
seqlengths[45361] = 2
seqlengths[872] = 2
seqlengths[45362] = 2

for i in range(1, limit + 1):
    n = i
    count = 0
    seq = []
    seq.append(0)

    while (seq[-1] != n):
        seq.append(n)
        n = FacSum(n)
        count += 1

        if (n <= limit and seqlengths[n] > 0):
            count += seqlengths[n]
            break

    if (count == 60):
        result += 1

    for j in range(1, len(seq)):
        if (seq[j] <= limit):
            seqlengths[seq[j]] = count
        count -= 1

print(result)
