# =============================================================================
# Battleship AI generate shots
# =============================================================================

import matplotlib.pyplot as plt
import random as rand
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

def updateAIBoard(guess, value):
    AIBoard[guess[0]][guess[1]] = value

def checkValidShotLocation(guess):
    if str(guess[0]) in "0123456789" and str(guess[1]) in "0123456789":
        if AIBoard[guess[0]][guess[1]] == 'O' or AIBoard[guess[0]][guess[1]] == 'X' or AIBoard[guess[0]][guess[1]] == 'S':
            return False
        return True
    return False

def __printHeatMap__(ships, p2board, mode):
    if mode == "search":
        search(3, ships, p2board)
    else:
        target(3, ships)
    a = AIBoardHeatMap
    plt.imshow(a, cmap='binary')
    plt.show()

def search(diff, ships, p2board):
    global AIBoardHeatMap
    AIBoardHeatMap = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    guess = (0, 0)
    if diff == 1:
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            guess = (row, col)
            if checkValidShotLocation(guess) == True:
                return guess
    elif diff == 2:
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if (1+row)%2 == (1+col)%2:
                guess = (row, col)
                if checkValidShotLocation(guess) == True:
                    return guess
        
    elif diff == 3:
        #For each space
        for row in range(0, 10):
            for col in range(0, 10):
                
                #Destroyer Check
                if ships[4] == False and p2board[row][col] == ' ':
                    if col-1 >= 0:
                        if AIBoard[row][col-1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-1 >= 0:
                        if AIBoard[row-1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col+1 <= 9:
                        if AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row+1 <= 9:
                        if AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                
                #Sub Check
                if ships[3] == False and p2board[row][col] == ' ':
                    if col-1 >= 0 and col+1 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-1 >= 0 and row+1 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-2 >= 0:
                        if AIBoard[row][col-2] == ' ' and AIBoard[row][col-1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-2 >= 0:
                        if AIBoard[row-2][col] == ' ' and AIBoard[row-1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col+2 <= 9:
                        if AIBoard[row][col-2] == ' ' and AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row+2 <= 9:
                        if AIBoard[row-2][col] == ' ' and AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                
                #Cruiser Check
                if ships[2] == False and p2board[row][col] == ' ':
                    if col-1 >= 0 and col+1 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-1 >= 0 and row+1 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-2 >= 0:
                        if AIBoard[row][col-2] == ' ' and AIBoard[row][col-1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-2 >= 0:
                        if AIBoard[row-2][col] == ' ' and AIBoard[row-1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col+2 <= 9:
                        if AIBoard[row][col-2] == ' ' and AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row+2 <= 9:
                        if AIBoard[row-2][col] == ' ' and AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                            
                #Battleship Check
                if ships[1] == False and p2board[row][col] == ' ':
                    if col-3 >= 0:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col-2] == ' ' and AIBoard[row][col-3] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-2 >= 0 and col+1 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col-2] == ' ' and AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-1 >= 0 and col+2 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col+1] == ' ' and AIBoard[row][col+2] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col+3 <= 9:
                        if AIBoard[row][col+1] == ' ' and AIBoard[row][col+2] == ' ' and AIBoard[row][col+3] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-3 >= 0:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row-2][col] == ' ' and AIBoard[row-3][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-2 >= 0 and row+1 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row-2][col] == ' ' and AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-1 >= 0 and row+2 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row+1][col] == ' ' and AIBoard[row+2][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row+3 <= 9:
                        if AIBoard[row+1][col] == ' ' and AIBoard[row+2][col] == ' ' and AIBoard[row+3][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    
                #Carrier Check
                if ships[0] == False and p2board[row][col] == ' ':
                    if col-4 >= 0:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col-2] == ' ' and AIBoard[row][col-3] == ' ' and AIBoard[row][col-4] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-3 >= 0 and col+1 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col-2] == ' ' and AIBoard[row][col-3] == ' ' and AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-2 >= 0 and col+2 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col-2] == ' ' and AIBoard[row][col+1] == ' ' and AIBoard[row][col+2] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col-1 >= 0 and col+3 <= 9:
                        if AIBoard[row][col-1] == ' ' and AIBoard[row][col+1] == ' ' and AIBoard[row][col+2] == ' ' and AIBoard[row][col+3] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if col+4 <= 9:
                        if AIBoard[row][col+1] == ' ' and AIBoard[row][col+2] == ' ' and AIBoard[row][col+3] == ' ' and AIBoard[row][col+4] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    
                    if row-4 >= 0:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row-2][col] == ' ' and AIBoard[row-3][col] == ' ' and AIBoard[row-4][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-3 >= 0 and row+1 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row-2][col] == ' ' and AIBoard[row-3][col] == ' ' and AIBoard[row-1][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-2 >= 0 and row+2 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row-2][col] == ' ' and AIBoard[row+1][col] == ' ' and AIBoard[row+2][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row-1 >= 0 and row+3 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row+1][col] == ' ' and AIBoard[row+2][col] == ' ' and AIBoard[row+3][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    if row+4 <= 9:
                        if AIBoard[row-1][col] == ' ' and AIBoard[row+2][col] == ' ' and AIBoard[row+3][col] == ' ' and AIBoard[row+4][col] == ' ':
                            AIBoardHeatMap[row][col] += 1
                    
        maxVal = 0
        target = []
        for row in range(0, 10):
            for col in range(0, 10):
                if AIBoardHeatMap[row][col] > maxVal:
                    maxVal = AIBoardHeatMap[row][col]
        
        while True:
            target = (rand.randint(0, 9), rand.randint(0, 9))
            if AIBoardHeatMap[target[0]][target[1]] == maxVal:
                return target
        
        







def target(diff, ships):
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
        global AIBoardHeatMap
        AIBoardHeatMap = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        #For each space
        for row in range(0, 10):
            for col in range(0, 10):
                
                if AIBoard[row][col] == 'X':
                    if col-1 >= 0 and AIBoard[row][col-1] == ' ':
                        AIBoardHeatMap[row][col-1] += 1
                    if col+1 <= 9 and AIBoard[row][col+1] == ' ':
                        AIBoardHeatMap[row][col+1] += 1
                    if row-1 >= 0 and AIBoard[row-1][col] == ' ':
                        AIBoardHeatMap[row-1][col] += 1
                    if row+1 <= 9 and AIBoard[row+1][col] == ' ':
                        AIBoardHeatMap[row+1][col] += 1
                        
                    if col-1 >= 0 and col+1 <= 9:
                        if AIBoard[row][col+1] == ' ':
                            AIBoardHeatMap[row][col+1] += 1
                        if AIBoard[row][col-1] == 'X':
                            AIBoardHeatMap[row][col+1] += 1
                        if AIBoard[row][col+1] == 'O' or AIBoard[row][col+1] == 'X':
                            AIBoardHeatMap[row][col+1] = 0
                            
                    if row-1 >= 0 and row+1 <= 9:
                        if AIBoard[row+1][col] == ' ':
                            AIBoardHeatMap[row+1][col] += 1
                        if AIBoard[row-1][col] == 'X':
                            AIBoardHeatMap[row+1][col] += 1
                        if AIBoard[row+1][col] == 'O' or AIBoard[row+1][col] == 'X':
                            AIBoardHeatMap[row+1][col] = 0
                            
                    if col+1 <= 9 and col-1 >= 0:
                        if AIBoard[row][col-1] == ' ':
                            AIBoardHeatMap[row][col-1] += 1
                        if AIBoard[row][col+1] == 'X':
                            AIBoardHeatMap[row][col-1] += 1
                        if AIBoard[row][col-1] == 'O' or AIBoard[row][col-1] == 'X':
                            AIBoardHeatMap[row][col-1] = 0
                            
                    if row+1 <= 9 and row-1 >= 0:
                        if AIBoard[row-1][col] == ' ':
                            AIBoardHeatMap[row-1][col] += 1
                        if AIBoard[row+1][col] == 'X':
                            AIBoardHeatMap[row-1][col] += 1
                        if AIBoard[row-1][col] == 'O' or AIBoard[row-1][col] == 'X':
                            AIBoardHeatMap[row-1][col] = 0
                
        maxVal = 0
        for row in range(0, 10):
            for col in range(0, 10):
                if AIBoardHeatMap[row][col] > maxVal:
                    maxVal = AIBoardHeatMap[row][col]
        
        for row in range(0, 10):
            for col in range(0, 10):
                if AIBoardHeatMap[row][col] == maxVal:
                    return (row, col)
                    
        