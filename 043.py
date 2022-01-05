"""
The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in
some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with
this property.
"""

# problem can be solved by hand, the following is a
# programmatic solution

factors = [1, 2, 3, 5, 7, 11, 13, 17]
valid_len = len(factors)
valid_sequences = []
total = 0

# Checks for a 3-digit number with 3 unique digits


def not_unique(digits):
    return ((digits[0] == digits[1])
            or (digits[1] == digits[2])
            or (digits[0] == digits[2]))


# generate all valid triples that have unique digits
# for each factor
for i in range(0, len(factors)):
    current_map = {}
    for j in range(factors[i], 1000, factors[i]):
        digits = str(j).zfill(3)

        # prune numbers without non-unique digits
        if not_unique(digits):
            continue

        # current_map is of the form
        # {'d1d2':[list of all possible valid d3s], ...}
        if digits[:2] not in current_map:
            current_map[digits[:2]] = [digits[2]]
        else:
            current_map[digits[:2]].append(digits[2])

    valid_sequences.append(current_map)


# check each triple starting with the 3 most
# significant digits
# get the last two digits, and find all the valid
# values for the next one digit
# perform recursively
def get_matches_starting_with(sequence, index):
    global total
    if index == valid_len:
        total += int(sequence)
    else:
        pair = sequence[-2:]
        if pair in valid_sequences[index]:
            for digit in valid_sequences[index][pair]:
                if digit not in sequence:
                    get_matches_starting_with(sequence + digit, index + 1)


all_matches = []
for pair in valid_sequences[0]:
    if pair[0] == '0':
        continue
    for digit in valid_sequences[0][pair]:
        triple = pair + digit
        all_matches.append(get_matches_starting_with(triple, 1))

print(total)
