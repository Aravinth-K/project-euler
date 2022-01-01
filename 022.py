"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

open_file = open('p022_names.txt', 'r')


def find_replace(string, dictionary):
    for item in string:
        if item in dictionary.keys():
            string = string.replace(item, "+" + str(dictionary[item]))
    return string


data = open_file.read()

names = data.split(",")

for i in range(len(names)):
    names[i] = names[i].replace("\"", "")

names.sort()

# define a dictionary scoring each letter with a number
l_score = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
           'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
           'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
           'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
           'Y': 25, 'Z': 26}

# list strings with the sum of each scored name
numbers = [find_replace(names[i], l_score) for i in range(len(names))]

for i in range(len(numbers)):
    numbers[i] = numbers[i].split("+")
    numbers[i].remove('')
    numbers[i] = list(map(int, numbers[i]))

# score of the name times its position in the list.
scores = [sum(numbers[i])*(i+1) for i in range(len(numbers))]

print(sum(scores))

open_file.close()
