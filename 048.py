"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... +
10001000.
"""
n = 0
for i in range(1, 1000 + 1):
    n += (i ** i)
digits = []
for i in range(10):
    digits.append(n % 10)
    n //= 10
print(''.join(str(digit) for digit in digits[::-1]))
