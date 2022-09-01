import game as game

'''
    Game Engine File - main.py
'''

def main():
    dice = int(input("How many dice in this game? "))
    g = game.Game(dice)
    status = 1
    while status:
        status = g.game()
    # g.gameStatus()

if __name__ == "__main__":
    main()