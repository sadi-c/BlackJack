"""
    Player class
        Defines the actions that each player instance can do.

    1. drawCard()
        draws one card or skip when take turn
    2. check()
        checks whether the sum reaches, under, or over 21
    3. showCurrent()
        displays the current cards the player has


"""


import requests
from Card import Card


class Player:
    def __init__(self, deck, name):
        self.hand = []
        self.sum = 0
        self.convert = {
            "ACE": 1,
            "JACK": 10,
            "QUEEN": 10,
            "KING": 10
        }
        self.deck = deck
        self.name = name
        self.status = ""

    def drawCard(self):
        deckID = self.deck.deckID
        req = requests.get("https://deckofcardsapi.com/api/deck/" + deckID + "/draw/?count=1")
        res = req.json()

        card = Card(res['cards'][0]['value'], res['cards'][0]['suit'], res['cards'][0]['code'])
        num = card.value
        if card.value in self.convert:
            # choice for ACE
            num = self.convert[card.value]
            if num == 1:
                while True:
                    try:
                        num = int(input("You got an Ace, would you like 1 or 11?: "))
                    except:
                        print("Not a valid input, try again: ")
                        continue
                    else:
                        if num == 1 or num == 11:
                            break
                        print("Not a valid input, try again: ")

        self.sum += int(num)
        result = self.check()
        if result == 0:
            self.hand.append(card)
            self.showCurrent()
        elif result == -1:
            self.status = "LOSE"
            self.hand.append(card)
            self.showCurrent()
        else:
            self.status = "WIN"
            self.hand.append(card)
            self.showCurrent()

    def check(self):
        # check win/lose
        if self.sum > 21:
            return -1
            # LOSE
        elif self.sum < 21:
            # continue
            return 0
        else:
            # win
            return 1

    def showCurrent(self):
        print("==========NOW YOU HAVE==========")
        if self.hand:
            for card in self.hand:
                print(card)
        else:
            print("No cards in your hand, start drawing.")

        print("===============" + str(self.sum) + "===============\n\n")

