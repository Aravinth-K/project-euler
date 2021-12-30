"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five
hundred divisors?
"""


def divisors(n, start=2):
    if n == 1:
        return 1
    i = start
    while i * i <= n:
        if n % i == 0:
            cnt = 1
            while n % i == 0:
                n //= i
                cnt += 1
            return divisors(n, i+1)*cnt
        i += 1
    return 2


for n in range(1, 1000000):
    Tn = (n*(n+1))//2
    if n % 2 == 0:
        cnt = divisors(n/2)*divisors(n+1)
    else:
        cnt = divisors(n)*divisors((n+1)/2)
    if cnt >= 500:
        print(Tn)
        break