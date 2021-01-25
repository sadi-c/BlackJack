"""
    Card class
        Definition for each card

"""


class Card:
    def __init__(self, value, suit, code):
        self.value = value
        self.suit = suit
        self.code = code

    def __str__(self):
        return f"{self.suit} {self.value}"