import os
import re
import sys
import time
from termcolor import colored


class main:
    def __init__(self):
        self.chosenWord = "horse"
        self.board = [
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

    def printBoard(self):
        for row in self.board:
            sys.stdout.write("              ")  # to center the board
            for letter in row:
                if row != "":
                    sys.stdout.write(f'| {letter.upper()} ')

            sys.stdout.write("|\n\n")
            pass

        sys.stdout.write("\n")
        pass

    def correctPlace(self, string):
        return colored(string, "green")

    def correctLetter(self, string):
        return colored(string, "yellow")

    def wrongLetter(self, string):
        return colored(string, "red")

    def defineNewWord(self):
        # do stuff with textHandler
        # except old words so you dont get duplicates
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
        pass

        # secondly for each letter in the guess we'll check if they match with the chosen word's letter
        for i in range(len(response)):
            if response[i] == self.chosenWord[i]:
                sliceWord((self.chosenWord[i]), i)
                pass
            elif response[i] in self.chosenWord:
                sliceWord((response[i]), i)
                pass
            else:
                sliceWord((response[i]), i)
                pass
            pass

        self.activeRow += 1

    def run(self):
        # this loops

        # clear terminal
        def clear():
            os.system("cls")
            sys.stdout.write("\n")

        clear()

        self.welcome()
        self.printBoard()
        sys.stdout.write(self.correctPlace("a") + "\n")
        self.checkInputWord()

        self.run()


mainClass = main()

mainClass.run()
