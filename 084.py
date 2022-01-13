"""
In the game, Monopoly, the standard board is set up in the
following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	                                C1
T2	 	                                U1
H1	 	                                C2
CH3	 	                                C3
R4	 	                                R2
G3	 	                                D1
CC3	 	                                CC2
G2	 	                                D2
G1	 	                                D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

A player starts on the GO square and adds the scores on two
6-sided dice to determine the number of squares they advance
in a clockwise direction. Without any further rules we would
expect to visit each square with equal probability: 2.5%.
However, landing on G2J (Go To Jail), CC (community chest),
and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that
orders the player to go directly to jail, if a player rolls
three consecutive doubles, they do not advance the result of
their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are
shuffled. When a player lands on CC or CH they take a card
from the top of the respective pile and, after following the
instructions, it is returned to the bottom of the pile. There
are sixteen cards in each pile, but for the purpose of this
problem we are only concerned with cards that order a
movement; any instruction not concerned with movement will be
ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting
a particular square. That is, the probability of finishing at
that square after a roll. For this reason it should be clear
that, with the exception of G2J for which the probability of
finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square,
and it is the final square that the player finishes at on each
roll that we are interested in. We shall make no distinction
between "Just Visiting" and being sent to JAIL, and we shall
also ignore the rule about requiring a double to "get out of
jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from
00 to 39 we can concatenate these two-digit numbers to produce
strings that correspond with sets of squares.

Statistically it can be shown that the three most popular
squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) =
Square 24, and GO (3.09%) = Square 00. So these three most
popular squares can be listed with the six-digit modal string:
102400.

If, instead of using two 6-sided dice, two 4-sided dice are
used, find the six-digit modal string.
"""

from random import randint, shuffle
from collections import deque, Counter

squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2",
           "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
square_numbers = {square: i for i, square in enumerate(squares)}
num_squares = len(squares)


def build_deck(choices):
    numbers = [square_numbers[square] for square in choices]
    shuffle(numbers)
    return deque(numbers)


transitions = {
    "G2J": build_deck(["JAIL"]),
    "CH1": build_deck(["CH1", "CH1", "CH1", "CH1", "CH1", "CH1", "GO", "JAIL", "C1", "E3", "H2", "R1", "R2", "R2", "U1", "T1"]),
    "CH2": build_deck(["CH2", "CH2", "CH2", "CH2", "CH2", "CH2", "GO", "JAIL", "C1", "E3", "H2", "R1", "R2", "R3", "U2", "D3"]),
    "CH3": build_deck(["CH3", "CH3", "CH3", "CH3", "CH3", "CH3", "GO", "JAIL", "C1", "E3", "H2", "R1", "R1", "R1", "U1", "CC3"]),
    "CC1": build_deck(["CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "GO", "JAIL"]),
    "CC2": build_deck(["CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "GO", "JAIL"]),
    "CC3": build_deck(["CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "GO", "JAIL"])
}
transitions = {square_numbers[square]               : deck for square, deck in list(transitions.items())}


def transition(square_number):
    while square_number in transitions:
        deck = transitions[square_number]
        new_square_number = deck.pop()
        deck.appendleft(new_square_number)
        if square_number == new_square_number:
            break
        square_number = new_square_number
    return square_number


def move(square_number, die_size=6):
    roll = randint(1, die_size) + randint(1, die_size)
    square_number += roll
    square_number %= num_squares
    return transition(square_number)


def simulate(iterations=2000000, die_size=6):
    result = Counter()
    square_number = 0
    for i in range(iterations):
        square_number = move(square_number, die_size)
        result[square_number] += 1
    return result


simulation = simulate(die_size=4)
print(("".join("{:02}".format(square_number)
      for square_number, count in simulation.most_common(3))))
