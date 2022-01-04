"""
An irrational decimal fraction is created by concatenating
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find
the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""


cache = [9]
for i in range(2, 8):
    cache.append((10**i - 10**(i-1))*i + cache[i-2])
digits = 1
target = 10
while target <= 1000000:
    for i in range(6):
        if target < cache[i + 1] and target > cache[i]:
            marker = (target - cache[i])/(i + 2) + (10**(i + 1) - 1)
            integer_part = int(marker)
            fractional_part = marker - int(marker)
            movement = int(fractional_part * (i + 2) - 1)
            digits *= (int(str(integer_part + 1)[movement]))
    target *= 10


print(digits)
