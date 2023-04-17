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
        # do this later

        # with open(self.fileLocation, "r") as file:
        #     for line in file.readlines():
        #         if name in line.split(",")[0]:
        #             print("You're already on the scoreboard. Do you want to replace your score or submit another one? (replace/submit)")
        #             response = input("... ")
        #             if "rep" in response:
                        
        #                 pass
        #             else:
        #                 #print
        #                 pass
        #             pass
        #         pass
        #     pass

        
        return

    def writeScoreboard(self, name, score, word, time):
        # if person alrady has score ask if they wanna override it
        with open(self.fileLocation, "a") as file:
            file.write(f'{name},{score},{word},{time}')
            file.write("\n")
            pass
        return
