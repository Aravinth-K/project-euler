"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
20, 22, 44, 55 and 110; therefore d(220) = 284. The proper
divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def div_count(n):
    original_number = n
    count = 1
    if n < 4:
        return 1
    for i in range(len(primes)):
        p = primes[i]
        if n % p == 0:
            t = p*p
            n //= p
            while n % p == 0:
                t *= p
                n //= p
            count *= (t - 1)//(p - 1)
        if p * p > n:
            break
    if n > 1:
        count *= (n + 1)
    return count - original_number


# amicable numbers involutive under div, i.e. div(div(a)) = a
total = 0
for i in range(2, 10000):
    if div_count(div_count(i)) == i and div_count(i) != i:
        total += i
    else:
        continue

print(total)
