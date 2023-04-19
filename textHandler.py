import random


class text:
    def __init__(self):
        self.scoreBoardLocation = "saves/scoreboard.csv"
        self.wordsLocation = "words.csv"

        try:
            open(self.scoreBoardLocation, "x")
        except:
            pass
        pass

    def readScoreboard(self):
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

        listOfObjects = []

        with open(self.scoreBoardLocation, "r") as file:
            for line in file.readlines():
                line = line.split(",")
                line[3] = line[3][:-2]
                listOfObjects.append({
                    "name": line[0],
                    "score": line[1],
                    "word": line[2],
                    "time": line[3],
                })
                pass
            pass
        return listOfObjects

    def writeScoreboard(self, name, score, word, time):
        # if person alrady has score ask if they wanna override it
        with open(self.scoreBoardLocation, "a") as file:
            file.write(f'{name},{score},{word},{time}')
            file.write("\n")
            pass
        return

    def getWord(self):
        word = "horse"
        with open(self.wordsLocation, "r") as file:
            word = random.choice(file.readline().split(","))
            pass
        return word

    def checkWord(self, input):
        boolean = True

        with open(self.wordsLocation, "r") as file:
            words = file.readline().split(",")
            if input in words:
                return True
            else:
                return False