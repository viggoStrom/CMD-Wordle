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

    def printRow(self, row):
        sys.stdout.write("              ")  # to center the board
        for i in range(len(row)):
            if row != "":
                if row[i] == self.chosenWord[i]:
                    sys.stdout.write(
                        f'| {self.correctPlace(row[i].upper())} ')
                    pass
                elif row[i] in self.chosenWord:
                    sys.stdout.write(
                        f'| {self.correctLetter(row[i].upper())} ')
                    pass
                else:
                    sys.stdout.write(
                        f'| {self.wrongLetter(row[i].upper())} ')
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
        return colored(string, "red")

    def defineNewWord(self):
        # do stuff with textHandler
        # except old words so you dont get duplicates, thats no fun
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
                sliceWord(self.chosenWord[i], i)
                pass
            elif response[i] in self.chosenWord:
                sliceWord(response[i], i)
                pass
            else:
                sliceWord(response[i], i)
                pass
            pass

        # self.printRow(self.board[self.activeRow])

        if response == self.chosenWord:
            print("You guessed the word.")
            raise SystemExit

        if self.activeRow < len(self.board) - 1:
            self.activeRow += 1
        else:
            print("game over")
            raise SystemExit

    def run(self):
        # this loops

        # clear terminal
        def clear():
            os.system("cls")
            sys.stdout.write("\n")

        clear()

        self.welcome()
        self.printBoard()
        self.checkInputWord()

        self.run()


mainClass = main()

mainClass.run()
