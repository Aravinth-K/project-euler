"""
If the numbers 1 to 5 are written out in words: one, two,
three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342
      (three hundred and forty-two) contains 23 letters and
      115 (one hundred and fifteen) contains 20 letters.
      The use of "and" when writing out numbers is in compliance
      with British usage.
"""

dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'}


def tens(word, n):
    # Add the numbers 20 to 99 to dict.
    dict[n] = word
    for i in range(n + 1, n + 10):
        dict[i] = word + dict[i-n]


tenList = ['twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']

for i in range(0, 8):
    tens(tenList[i]+'ty', (i+2)*10)


def hundreds(n):
    # Add numbers 100 to 999.
    i = 100 * n
    dict[i] = dict[n] + 'hundred'
    for j in range(i+1, i+100):
        dict[j] = dict[i] + 'and' + dict[j - i]


for i in range(1, 10):
    hundreds(i)

# Manually add 1000 to dict.
dict[1000] = dict[1] + 'thousand'

# List all of the words associated to each number from 1 to 1000.
words = list(dict.values())

count = 0

# Add up the number of letters in all the words.
for x in words:
    s = 0
    for i in x:
        s += 1
    count += s

print(count)
