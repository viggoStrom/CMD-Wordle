class text:
    def __init__(self):
        self.fileLocation = "saves/scoreboard.csv"
        # create file if it doesnt exist
        # else
        # open existing file

        # create structure of file (csv)
        # name, nr. of tries, word

        # sort by time, frequency of use.

        try:
            open(self.fileLocation, "x")
        except:
            pass
        pass

    def readScoreboard(self, name):

        return

    def writeScoreboard(self, name, score, word):
        # if person alrady has score ask if they wanna override it
        with open(self.fileLocation, "a") as file:
            file.write(f'{name},{score},{word}')
            file.write("\n")
            pass
        return
