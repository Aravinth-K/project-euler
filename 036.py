"""
The decimal number, 585 = 10010010012 (binary), is
palindromic in both bases.

Find the sum of all numbers, less than one million, which
are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""

solution = 0

for i in range(1, 1000000, 2):
    if str(i) == str(i)[::-1]:
        if bin(i)[2:] == bin(i)[2:][::-1]:
            solution += i

print(solution)
