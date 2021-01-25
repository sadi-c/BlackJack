"""
    Menu class
        Definition for menu

        Displays the menu and controls of the game (start or quit).

"""


import sys
from Game import Game


class Menu:
    def __init__(self):
        self.game = Game()
        self.choices = {

            "1": self.game.start_game,

            "2": self.game.show_leaderboard,

            "3": self.game.clear_leaderboard,

            "Q": self.quit
        }

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def display_menu(self):
        print(""" 
            **************************
             Welcome to G2 Casino: Blackjack Table!
             What would you like to do?  


             1. Start A New Game

             2. Show Leaderboard

             3. Clear Leaderboard

             Q. Quit Game

             """)

    def quit(self):
        print("***  Game over! ****")
        sys.exit()
