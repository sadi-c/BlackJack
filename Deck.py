"""
    Deck class
        Definition for creating a deck of card.

        When instantiated, makes GET request to api to receive a new deck of cards.
        Saves a unique deck id to 'self.deckID'.

"""


import requests


class Deck:
    def __init__(self):
        self.URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        self.init()
        
    def init(self):
      try:
        req = requests.get(self.URL)
        res = req.json()
        self.deckID = res['deck_id']
      except:
        print("Network error")
