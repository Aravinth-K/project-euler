"""
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators
2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring
cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""

LIMIT = 1000

max_len = 0   # The maximum length
max_d = 1     # The 'd' that has maximum length

for d in range(1, LIMIT):
    quotient = {0: 0}
    cur_value = 1
    len_recur = 0

    # Performing division as if by hand
    while cur_value not in quotient:
        len_recur += 1
        quotient[cur_value] = len_recur
        cur_value = (cur_value % d) * 10

    if not cur_value:
        continue

    # Remove number of values that do not recur
    len_recur -= quotient[cur_value]

    if len_recur > max_len:
        max_len = len_recur
        max_d = d

print(max_d)
