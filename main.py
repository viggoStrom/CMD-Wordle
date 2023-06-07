# 
# This is a Wordle copy made in Python.
# The code choses a word at random from
# a list of approved words which you're
# supposed to guess. There's logic which
# handles whether the guessed word is 
# correct and which letters are correct
# so that they can be colored an appropriate
# color for if the letter is even present
# in the correct word or is in the correct  
# place. After each guess the entire board
# (terminal) gets cleared so the board can 
# be redrawn so it looks cleaner. If you 
# correctly guess the word or if you fail
# the leaderboard will be displayed and 
# if you won, your score will be shown 
# and you'll se your position.
# 

import os
import re
import sys
import time
from termcolor import colored
import math

from textHandler import text
textHandler = text()


class wordle:
    def __init__(self):
        self.chosenWord = textHandler.getWord()
        self.board = [
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
        ]
        self.activeRow = 0
        pass

    def welcome(self):
        print("Welcome to Wordle\n")
        print("██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗")
        print("██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝")
        print("██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  ")
        print("██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  ")
        print("╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗")
        print(" ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
        print("\n")

    def printRow(self, word):
        sys.stdout.write("              ")  # to center the board

        for letter in word:
            if word == "":
                sys.stdout.write("|\n\n")

            if letter == self.chosenWord:
                sys.stdout.write(f'| {self.correctPlace(letter.upper())} ')
                pass

            elif letter in self.chosenWord:
                sys.stdout.write(f'| {self.correctLetter(letter.upper())} ')
                pass

            else:
                sys.stdout.write(f'| {self.wrongLetter(letter.upper())} ')
                pass

        sys.stdout.write("|\n\n")
        pass

    def printBoard(self):
        for row in self.board:
            self.printRow(row)
            pass

        sys.stdout.write("\n")
        pass

    def correctPlace(self, string):
        return colored(string, "green")

    def correctLetter(self, string):
        return colored(string, "yellow")

    def wrongLetter(self, string):
        return colored(string, "dark_grey")

    def printScoreBoard(self):
        entries = textHandler.readScoreboard()
        latest = entries[len(entries)-1]

        # sort entries
        # !!! i.e.the sorting algorithm is located here !!!
        # !!! Can't miss it !!!
        entries = sorted(entries, key=lambda entry: (int(entry["score"]), float(entry["time"])))

        print("\nScoreboard:")
        i = 1
        for entry in entries:
            guess = "guesses"
            if entry["score"] == "1":
                guess = "guess"

            if entry == latest:
                print(
                    f'\t{i}. {entry["name"]}: {entry["score"]} {guess} at {entry["word"].upper()} \t ({math.floor(float(entry["time"])*100)/100} s) (Most recent)')
                pass
            else:
                print(
                    f'\t{i}. {entry["name"]}: {entry["score"]} {guess} at {entry["word"].upper()} \t ({math.floor(float(entry["time"])*100)/100} s)')
                pass
            pass

            if i >= 10:
                suffix = ""
                print(entry)
                if entry == latest:
                    suffix = " (Most recent)"
                print(
                    f'\n\t{len(entries)}. {latest["name"]}: {latest["score"]} {guess} at {latest["word"].upper()}.{suffix}')
                break

            i = i + 1
        print("")
        pass

    def checkInputWord(self):
        def sliceWord(reasign, i):
            slicedRow = []
            for letter in self.board[self.activeRow]:
                slicedRow.append(letter)

            slicedRow[i] = reasign
            self.board[self.activeRow] = "".join(slicedRow)

        response = input("... ").lower()
        response = re.sub(r'[^a-z]', "", response)

        # first check if it's actually five letters or not
        if len(response) != 5:
            print("Only five letter words please.\n")
            time.sleep(.8)
            return
        elif not textHandler.checkWord(response):
            print("Not in word list.")
            time.sleep(.8)
            return

        # secondly for each letter in the guess we'll check if they match with the chosen word's letter
        for i in range(len(response)):
            if response[i] == self.chosenWord[i]:
                sliceWord(self.chosenWord[i], i)
                pass
            elif response[i] in self.chosenWord:
                sliceWord(response[i], i)
                pass
            else:
                sliceWord(response[i], i)
                pass
            pass

        self.finish()

        self.clear()
        self.welcome()
        self.printBoard()

        if response == self.chosenWord:
            print(
                f'Congrats! You guessed the word {self.chosenWord.upper()}.\n')
            time.sleep(.9)
            name = input("What's your name? For the scoreboard... ")[
                0:16].title()
            if name == "":
                name = "Im Lazy"
            textHandler.writeScoreboard(
                name, self.activeRow + 1, self.chosenWord, self.time)

            self.printScoreBoard()
            raise SystemExit

        if self.activeRow < len(self.board) - 1:
            self.activeRow += 1
        else:
            print(f'Game over. The word was {self.chosenWord.upper()}.')
            self.printScoreBoard()
            raise SystemExit

    # clear terminal
    def clear(self):
        os.system("cls")
        sys.stdout.write("\n")

    def run(self):
        # this loops

        self.clear()

        # DEBUG only
        print(self.chosenWord)

        self.welcome()
        self.printBoard()
        self.checkInputWord()

        self.run()

    def initiate(self):
        self.startTime = time.time()
        self.run()

    def finish(self):
        self.endTime = time.time()
        self.time = self.endTime - self.startTime


game = wordle()
game.initiate()
