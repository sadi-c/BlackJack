"""
    Game class
        Definition of the game

    1. prepare()
        Will be called by start_game() to prepare a new deck of cards and initialize numbers of players.
    2. start_game()
        Starts the game and checks to see if the player wins or loses.
    3. readJson
        Reads leaderboard.json if it exists and load to 'self.leaderboard' variable to show the leader board.
    4. writeJson
        Writes results to leaderboard.json after each round.
    5. show_leaderboard()
        Displays the leader board by printing out the 'self.leaderboard' variable.
    6. clear_leaderbard()
        Delete the leaderboard.json file and also clear the 'self.leaderboard' variable.


"""


import json
import os

from Deck import Deck
from Player import Player


class Game:
    def __init__(self):
        self.players = []
        self.leaderboard = {}

    def prepare(self):
        # prepare each players before the game starts

        self.players.clear()
        self.readJson()

        while True:
            try:
                players = int(input("Input how many players: "))

                while (players < 2):
                    players = int(input("Minimum of 2 players to play. Input how many players: "))
            except:
                print("Not a valid input, try again")
                continue
            else:
                break


        deck = Deck()

        for _ in range(players):
            name = input("Please enter your name: ")
            player = Player(deck, name)
            self.players.append(player)
            if name not in self.leaderboard:
                self.leaderboard[name] = 0

    def start_game(self):
        self.prepare()

        while len(self.players) > 0:
            for player in self.players:
                if len(self.players) == 1:
                    print("!!!!!!!!!!!Player " + str(player.name) + " WINS!!!!!!!!!!!")
                    self.leaderboard[player.name] += 1
                    self.writeJson()
                    return

                print("===Player " + str(player.name) + "'s turn===")

                while True:
                    try:
                        choice = int(input("Enter 1 to draw card, 0 to skip: "))
                    except:
                        print("Not a valid input")
                        continue
                    else:
                        if choice != 0 and choice != 1:
                            print("Not a valid input")
                            continue
                        break

                if choice == 1:
                    player.drawCard()
                    if player.status == "LOSE":
                        print("Sorry you lose.")
                        print("==================================")
                        self.players.remove(player)

                    elif player.status == "WIN":
                        print("!!!!!!!!!!!Player " + str(player.name) + " WINS!!!!!!!!!!!")
                        self.leaderboard[player.name] += 1
                        self.writeJson()
                        return
                else:
                    continue

    def readJson(self):
        try:
            with open("leaderboard.json", "r") as read_file:
                self.leaderboard = json.load(read_file)
        except Exception as e:
            pass

    def writeJson(self):

        try:
            with open("leaderboard.json", "w") as write_file:
                json.dump(self.leaderboard, write_file, indent=4)
        except Exception as e:
            pass

    def show_leaderboard(self):
        self.readJson()
        print("""
    ***************************
    Here is your G2 Casino: Blackjack Table Leaderboard:
    """)

        sortedBoard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

        for i in range(len(sortedBoard)):
            print(str(i + 1) + " " + sortedBoard[i][0] + " WINS " + str(sortedBoard[i][1]))
    
    def clear_leaderboard(self):
        self.leaderboard.clear()
        if os.path.exists("leaderboard.json"):
            os.remove("leaderboard.json")
        else:
            pass


