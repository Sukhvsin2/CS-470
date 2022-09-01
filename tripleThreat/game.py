from urllib import response


import random

class Game:
    dices = list()
    score = 0
    gameOver = 1

    # game constructor
    def __init__(self, dice):
        self.dices = [0] * dice
        self.score = 0

    def game(self):
        response = input("Roll the dice (Y/N)? ")
        status = 1
        if not self.gameOver:
            self.printScoreBoard()
            print("=> YOU LOSE!")
            return 0
            
        if(response.capitalize() == "Y"):
            for i in range(len(self.dices)):
                if self.dices[i] == "STUCK":
                    continue
                self.dices[i] = random.randint(1, 6)

            self.printScoreBoard()
            self.gameOver = self.scoreCalculate()
            print(self.score)
            status = 1
        else:
            status = 0
        return status

    def printScoreBoard(self):
        for i in range(len(self.dices)):
            print(f"Die #{i+1}", ("").ljust(1), end="")
        print("Sum")
        for i in self.dices:
            print(i, ("").ljust(5), end=" ")

    def scoreCalculate(self):
        res = 0
        for i in range(len(self.dices)):
            if self.dices[i] == 3 or self.dices[i] == "STUCK":
                self.dices[i] = "STUCK"
            else:
                self.score += self.dices[i]
                res += self.dices[i]
        return res

    def gameStatus(self):
        print("Current Score: ", self.score)
        print("Dices: ", self.dices)