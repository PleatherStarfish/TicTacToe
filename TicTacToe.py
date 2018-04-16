import random
from random import randint
import time
import sys

board = [None] * 9 # Create an empty list with 9 values

gameInPlay = True  # The gameInPlay variable will be used to control the main gameplay "while" loop

printSpeed = 0.1   # How fast to print each row of the game board (0.2 seconds by default)

humansTurn = True  # Human plays first


def whoGoesFirst():
    global humansTurn
    letterChoice = ""
    while True:
        letterChoice = str(input("Who goes first? Type \"h\" (human), \"c\" (computer), or \"r\" (random): "))
        if (letterChoice == "h") or (letterChoice == "c") or (letterChoice == "r"):
            break

    if (letterChoice == "h"):
        humansTurn = True
    elif (letterChoice == "c"):
        humansTurn = False
    elif (letterChoice == "r"):
        humansTurn = random.choice([True, False])
    else:
        print("ERROR")


def robotIsThinking():
    time.sleep(2)
    robotTalk = ["Shhh... I'm thinking!",
                 "Don't wake a sleeping giant...",
                 "Daisy, Daisy, give me your answer do...",
                 "Elementary, my dear Watson!",
                 "It's not exactly three-dimensional chess is it?",
                 "Sometimes I've believed as many as six impossible things before breakfast!",
                 "You just keep on trying till you run out of cake."]
    returnedRobotTalk = random.sample(robotTalk, 1)
    print(returnedRobotTalk[0]) ## [0] because we want this returned as a string
    time.sleep(2)


# Print instructions for the game.
def printInstructions():
    print("Welcome to Tic-Tac-Toe")
    print("by Daniel Miller - April 2018")
    print("Released for use under CC BY-SA 2.0")
    print("\n")
    print("Please choose your move by entering a number.")
    print("\n")
    print ("      |       |    ")
    print ("  0  ", "|", "  1  ", "|", "  2  ")
    print ("      |       |    ")
    print ("----------------------")
    print ("      |       |    ")
    print ("  3  ", "|", "  4  ", "|", "  5  ")
    print ("      |       |    ")
    print ("----------------------")
    print ("      |       |    ")
    print ("  6  ", "|", "  7  ", "|", "  8  ")
    print ("      |       |    ")
    print("\n")


def printBoard():
    if humansTurn:
        print("COMPUTER PLAYED %i" % randomMove)
    else:
        print("HUMAN PlAYED %i" % int(move))
    time.sleep(printSpeed)
    print ("      |       |    ")
    time.sleep(printSpeed)
    print ("     " if board[0] == None else "  " + board[0] + "  ", "|", "     " if board[1] == None else "  " + board[1] + "  ", "|", "     " if board[2] == None else "  " + board[2] + "  ")
    time.sleep(printSpeed)
    print ("      |       |    ")
    time.sleep(printSpeed)
    print ("----------------------")
    time.sleep(printSpeed)
    print ("      |       |    ")
    time.sleep(printSpeed)
    print ("     " if board[3] == None else "  " + board[3] + "  ", "|", "     " if board[4] == None else "  " + board[4] + "  ", "|", "     " if board[5] == None else "  " + board[5] + "  ")
    time.sleep(printSpeed)
    print ("      |       |    ")
    time.sleep(printSpeed)
    print ("----------------------")
    time.sleep(printSpeed)
    print ("      |       |    ")
    time.sleep(printSpeed)
    print ("     " if board[6] == None else "  " + board[6] + "  ", "|", "     " if board[7] == None else "  " + board[7] + "  ", "|", "     " if board[8] == None else "  " + board[8] + "  ")
    time.sleep(printSpeed)
    print ("      |       |    ")


def replay(userInput):
    global humansTurn
    if (userInput == "y"):

        for i in range(0,9):          # go through every element in the list
            board[i] = None           # set each element to None

        humansTurn = not humansTurn   # Reverse order of play (i.e. if human went first before, computer goes first)
    else:
        print("\n")
        print("Goodbye")
        sys.exit()


printInstructions()

whoGoesFirst()

while True:

    if humansTurn:                                 # is it the humans turn to move?
        isInvalidMove = True                       # this sets the "while" loop to repeat until it gats a valid answer
        while isInvalidMove:                       # isInvalidMove fals True until a valid answer is given
            move = input("Enter your move: ")      # get user input in the form of a number
            if not board[int(move)]:               # iff the chosen index is falsy, proceed into the "if" statement
                board[int(move)] = "X"             # set the user-selected index to have string value "X"
                isInvalidMove = not isInvalidMove  # end the "while" loop
                humansTurn = not humansTurn        # end the human's turn
            else:
                print("Invalid move.")             # Iff the selected index is a value (not None) return error
                print("\n")
    else:                                          # "else" is entered in humanTurn is False
        compInvalidMove = True                     # his sets the "while" loop to repeat until it gats a valid answer
        while compInvalidMove:
            randomMove = int(randint(0,8))         # in the basic case, the program plays a random move
            if not board[randomMove]:              # iff the chosen index is falsy, proceed into the "if" statement
                board[randomMove] = "O"            # change the value at that index from None to "O"
                compInvalidMove = not compInvalidMove  # reverse the compInvalidMove boolean
                humansTurn = not humansTurn        # reverse the humansTurn boolean
                robotIsThinking()                  # wait some amount of time to "think"
            else:
                compInvalidMove = True             # unnecessary to repeat this, but helpful as a reminder

    if ((board[0] == "X" and board[1] == "X" and board[2] == "X") or    # Check if any wining move has been made
       (board[3] == "X" and board[4] == "X" and board[5] == "X") or
       (board[6] == "X" and board[7] == "X" and board[8] == "X") or
       (board[0] == "X" and board[4] == "X" and board[8] == "X") or
       (board[2] == "X" and board[4] == "X" and board[6] == "X") or
       (board[0] == "X" and board[3] == "X" and board[6] == "X") or
       (board[1] == "X" and board[4] == "X" and board[7] == "X") or
       (board[2] == "X" and board[5] == "X" and board[8] == "X")):
            printBoard()
            print("\n")
            print("Savor your moment of triumph Superman, but remember, victory has its price.")

            time.sleep(2)
            playAgain = input("Play again? (y/n): ")
            replay(playAgain)

    elif ((board[0] == "O" and board[1] == "O" and board[2] == "O") or   # Check if any wining move has been made
       (board[3] == "O" and board[4] == "O" and board[5] == "O") or
       (board[6] == "O" and board[7] == "O" and board[8] == "O") or
       (board[0] == "O" and board[4] == "O" and board[8] == "O") or
       (board[2] == "O" and board[4] == "O" and board[6] == "O") or
       (board[0] == "O" and board[3] == "O" and board[6] == "O") or
       (board[1] == "O" and board[4] == "O" and board[7] == "O") or
       (board[2] == "O" and board[5] == "O" and board[8] == "O")):
            printBoard()
            print("\n")
            print("You lose. Haha! I mean, I was literally just picking random moves. Not exactly Deep Blue")
            print("here. Maybe you should try Rock Paper Scissors. That might be more your speed.")

            time.sleep(2)
            playAgain = input("Play again? (y/n): ")    # user chooses whether to play again
            replay(playAgain)

    elif all(board):
            printBoard()
            print("\n")
            print("A tie! At best a Pyrrhic victory.")

            time.sleep(2)
            playAgain = input("Play again? (y/n): ")
            replay(playAgain)

    else:
            printBoard()

    print("\n")
