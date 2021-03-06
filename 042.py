"""
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form
a word value. For example, the word value for SKY is 19 + 11 +
25 = 55 = t10. If the word value is a triangle number then we
shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English
words, how many are triangle words?
"""

from math import sqrt

f = open('p042_words.txt')
words = f.read()
f.close()
words = words.strip().split(',')


def convert(character):
    """function to convert the
    words to alphabetical position"""
    return ord(character)-64


counter = 0

for word in words:
    x = sum(map(convert, word[1:-1]))
    if sqrt(8*x+1) == int(sqrt(8*x+1)):
        counter += 1

print(counter)
