"""
In the card game poker, a hand consists of five cards and are
ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made
up of the highest value wins; for example, a pair of eights
beats a pair of fives (see example 1 below). But if two ranks
tie, for example, both players have a pair of queens, then
highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	    Player 2	 	    Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD   	    Player 2
        Pair of Fives       Pair of Eights

2	 	5D 8C 9S JS AC 	    2C 5C 7D 8S QH          Player 1
        Highest card Ace    Highest card Queen

3	 	2D 9C AS AH AC      3D 6D 7D TD QD          Player 2
        Three Aces          Flush with Diamonds

4	 	4D 6S 9H QH QC      3D 6D 7H QD QS          Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D          Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt
to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's
cards and the last five are Player 2's cards. You can assume
that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in
each hand there is a clear winner.

How many hands does Player 1 win?
"""

import collections


class Card:
    """Card object (value and suit)."""
    CARD_VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @classmethod
    def from_string(cls, card):
        value, suit = card
        return cls(value, suit)

    def __str__(self):
        return str(self.value) + self.suit

    def __repr__(self):
        return self.__class__.__name__ + \
            "(" + self.value + ", " + self.suit + ")"

    def evaluate(self):
        return Card.CARD_VALUES[self.value]


class Hand:
    """Hand object (iterable of NB_CARDS cards)."""
    NB_CARDS = 5

    def __init__(self, cards):
        assert len(cards) == Hand.NB_CARDS
        self.cards = cards

    @classmethod
    def from_string(cls, string):
        cards = [Card.from_string(chunk) for chunk in string.split()]
        return cls(cards[:Hand.NB_CARDS]), cls(cards[Hand.NB_CARDS:])

    def __str__(self):
        return "-".join(str(c) for c in self.cards)

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.cards) + ")"

    def evaluate(self):
        """Return an arbitrarly formed tuple that can be used
        to sort hands using lexicographic order. First element
        is an integer describing the type of hand. Other
        values are added to be able to differentiate hands.
        Integers used:
        1 High Card: Highest value card.
        2 One Pair: Two cards of the same value.
        3 Two Pairs: Two different pairs.
        4 Three of a Kind: Three cards of the same value.
        5 Straight: All cards are consecutive values.
        6 Flush: All cards of the same suit.
        7 Full House: Three of a kind and a pair.
        8 Four of a Kind: Four cards of the same value.
        9 Straight Flush: All cards are consecutive values of
                          same suit.
        9 Royal Flush: Ten, Jack, Queen, King, Ace, in same
                       suit.
        """
        values = sorted((c.evaluate() for c in self.cards), reverse=True)
        count = collections.Counter(values)
        mc, mc2 = count.most_common(2)
        mc_val, mc_nb = mc
        mc2_val, mc2_nb = mc2
        if mc_nb == 4:
            return (8, mc_val, values)
        elif mc_nb == 3:
            if mc2_nb == 2:
                return (7, mc_val, mc2_val, values)
            else:
                return (4, mc_val, values)
        elif mc_nb == 2:
            if mc2_nb == 2:
                return (3, sorted((mc_val, mc2_val)), values)
            else:
                return (2, mc_val, values)
        else:
            assert mc_nb == 1
            is_flush = len(set(c.suit for c in self.cards)) == 1
            delta = values[0] - values[-1]
            is_straight = delta == Hand.NB_CARDS - 1
            if is_straight:
                return (9 if is_flush else 5, values)
            else:
                return (6 if is_flush else 1, values)

    # Note: other magic methods should be defined as well
    def __gt__(self, other):
        return self.evaluate() > other.evaluate()


ret = 0
with open('p054_poker.txt') as file_:
    for line in file_:
        hand1, hand2 = Hand.from_string(line)
        ret += hand1 > hand2
print(ret)
