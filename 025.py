"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci
sequence to contain 1000 digits?
"""

fibonacci_cache = {}


def fibonacci_memo(input_value):
    if input_value in fibonacci_cache:
        return fibonacci_cache[input_value]
    if input_value == 1:
        value = 1
    elif input_value == 2:
        value = 1
    elif input_value > 2:
        value = fibonacci_memo(input_value - 1) + \
            fibonacci_memo(input_value - 2)
    fibonacci_cache[input_value] = value
    return value


i = 0
num_digits = 0

while num_digits < 1000:
    i += 1
    num_digits = 0
    x = fibonacci_memo(i)
    while x:
        num_digits += 1
        x //= 10

print(i)
