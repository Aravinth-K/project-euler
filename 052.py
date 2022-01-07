"""
It can be seen that the number, 125874, and its double,
251748, contain exactly the same digits, but in a different
order.

Find the smallest positive integer, x, such that 2x, 3x, 4x,
5x, and 6x, contain the same digits.
"""


def same_digits(n):
    multiples = [2, 3, 4, 5, 6]
    digits = list(map(int, str(n)))
    check = True
    for m in multiples:
        tmp = list(map(int, str(m * n)))
        check = check and (sorted(digits) == sorted(tmp))
    return check


not_found = True
n = 0
while not_found:
    n += 1
    if same_digits(n):
        not_found = False
print(n)
