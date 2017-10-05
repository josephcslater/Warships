# =============================================================================
# Battleship AI generate shots
# =============================================================================

import random
import numpy as np

AIBoard = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
AIBoardHeatMap = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])

def getNumUnsunkHits():
    for row in range(0, 9):
        for col in range(0, 9):
            if AIBoard[row][col] == 'X':
                return 1
    return 0

def __toString__():
    print("AIBoard")
    print(AIBoard)
#    print("AIBoardHeatMap")
#    print(AIBoardHeatMap)

def __updateHeatMap__():
    pass

def updateMode():
    for row in range(0, 10):
        for col in range(0, 10):
            if AIBoard[row][col] == 'X':
                return "target"
    return "search"

def updateAIBoardSinking(shipCoords):
    for i in range(0, len(shipCoords)):
        row = shipCoords[i][0]
        col = shipCoords[i][1]
        AIBoard[row][col] = 'S'

def updateAIBoardSunkShip(AIGuess, sunkShipLength):
    xup, xdown, xright, xleft = 0, 0, 0, 0
    for rowCount in range(0, 10):
        for colCount in range(0, 10):
            if AIBoard[rowCount][colCount] == 'X':
                row = rowCount
                col = colCount
                break

    #Check up
    for i in range(1, sunkShipLength):
        if AIBoard[row-i][col] == 'X':
            xup += 1

    #Check down
    for i in range(1, sunkShipLength):
        if AIBoard[row+i][col] == 'X':
            xdown += 1

    #Check left
    for i in range(1, sunkShipLength):
        if AIBoard[row][col-i] == 'X':
            xleft += 1

    #Check down
    for i in range(1, sunkShipLength):
        if AIBoard[row][col+i] == 'X':
            xright += 1

    if xup+xdown+1 == sunkShipLength:
        AIBoard[row][col] = 'S'
        for i in range(1, sunkShipLength):
            if AIBoard[row-i][col] == 'X':
                AIBoard[row-i][col] = 'S'
        for i in range(1, sunkShipLength):
            if AIBoard[row+i][col] == 'X':
                AIBoard[row+i][col] = 'S'
    if xleft+xright+1 == sunkShipLength:
        AIBoard[row][col] = 'S'
        for i in range(1, sunkShipLength):
            if AIBoard[row][col-i] == 'X':
                AIBoard[row][col-i] = 'S'
        for i in range(1, sunkShipLength):
            if AIBoard[row][col+i] == 'X':
                AIBoard[row][col+i] = 'S'

def updateAIBoard(guess, value):
    AIBoard[guess[0]][guess[1]] = value

def checkValidShotLocation(guess):
    if str(guess[0]) in "0123456789" and str(guess[1]) in "0123456789":
        if AIBoard[guess[0]][guess[1]] == 'O' or AIBoard[guess[0]][guess[1]] == 'X' or AIBoard[guess[0]][guess[1]] == 'S':
            return False
        return True
    return False

def search(diff):
    guess = (0, 0)
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if diff == 1:
            guess = (row, col)
            if checkValidShotLocation(guess) == True:
                return guess
        elif diff == 2:
            if (1+row)%2 == (1+col)%2:
                guess = (row, col)
                if checkValidShotLocation(guess) == True:
                    return guess

def __testSearch__(diff):
    board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    while True:
        guess = search(diff)
        board[guess[0]][guess[1]] = 'X'
        print(board)
        print("Added " + str(guess))
        inpt = input()

def target(diff):
    if diff == 1 or diff == 2:
        for row in range(0, 10):
            for col in range(0, 10):
                if AIBoard[row][col] == 'X':
                    if col > 0:
                        if AIBoard[row][col-1] == ' ':
                            return(row, col-1)
                    if row < 9:
                        if AIBoard[row+1][col] == ' ':
                            return(row+1, col)
                    if col < 9:
                        if AIBoard[row][col+1] == ' ':
                            return(row, col+1)
                    if row > 0:
                        if AIBoard[row-1][col] == ' ':
                            return(row-1, col)












    elif diff == 3:
        __updateHeatMap__()
        maxVal = (0, 0, 0)
        for row in range(0, 10):
            for col in range(0, 10):
                if AIBoardHeatMap[row][col] > maxVal[0]:
                    maxVal = (AIBoardHeatMap[row][col], row, col)
        return(maxVal[1], maxVal[2])