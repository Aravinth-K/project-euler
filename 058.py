"""

"""


def isPrime(n):
    if (n <= 3):
        return n > 1
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


p = 0
m = 3
not_found = True
while not_found:
    p += isPrime((m - 1) * m + 1)
    p += isPrime((m - 2) * m + 2)
    p += isPrime((m - 3) * m + 3)
    if (10 * p < 2 * m - 1):
        not_found = False
        break
    m += 2
print(m)
