# =============================================================================
# Battleship AI preset fleet positions
# =============================================================================

import random
import numpy as np

def __checkValidShipPlacement__(length, coords, board):
    if coords[2] == 'l':
        if coords[1] < length-1:
            return(False)
        for i in range(length):
            if board[coords[0]][coords[1]-i] != ' ':
                return(False)
    elif coords[2] == 'r':
        if coords[1] > 10-length:
            return(False)
        for i in range(length):
            if board[coords[0]][coords[1]+i] != ' ':
                return(False)
    elif coords[2] == 'u':
        if coords[0] < length-1:
            return(False)
        for i in range(length):
            if board[coords[0]-i][coords[1]] != ' ':
                return(False)
    elif coords[2] == 'd':
        if coords[0] > 10-length:
            return(False)
        for i in range(length):
            if board[coords[0]+i][coords[1]] != ' ':
                return(False)
    return(True)

def __getStartCoords__():
    coords = (0, 0, 'l')
    direction = random.randint(0, 3)
    if direction == 0:
        coords = (random.randint(0, 9), random.randint(0, 9), 'l')
    if direction == 1:
        coords = (random.randint(0, 9), random.randint(0, 9), 'u')
    if direction == 2:
        coords = (random.randint(0, 9), random.randint(0, 9), 'r')
    if direction == 3:
        coords = (random.randint(0, 9), random.randint(0, 9), 'd')
    return coords
    
def getFleet():
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
    
    #Carrier
    coords = __getStartCoords__()
    while __checkValidShipPlacement__(5, coords, board) == False:
        coords = __getStartCoords__()
    if coords[2] == 'l':
        for i in range(5):
            board[coords[0]][coords[1]-i] = 'C'
    elif coords[2] == 'r':
        for i in range(5):
            board[coords[0]][coords[1]+i] = 'C'
    elif coords[2] == 'u':
        for i in range(5):
            board[coords[0]-i][coords[1]] = 'C'
    elif coords[2] == 'd':
        for i in range(5):
            board[coords[0]+i][coords[1]] = 'C'
            
    #Battleship
    coords = __getStartCoords__()
    while __checkValidShipPlacement__(4, coords, board) == False:
        coords = __getStartCoords__()
    if coords[2] == 'l':
        for i in range(4):
            board[coords[0]][coords[1]-i] = 'B'
    elif coords[2] == 'r':
        for i in range(4):
            board[coords[0]][coords[1]+i] = 'B'
    elif coords[2] == 'u':
        for i in range(4):
            board[coords[0]-i][coords[1]] = 'B'
    elif coords[2] == 'd':
        for i in range(4):
            board[coords[0]+i][coords[1]] = 'B'
            
    #Cruiser
    coords = __getStartCoords__()
    while __checkValidShipPlacement__(3, coords, board) == False:
        coords = __getStartCoords__()
    if coords[2] == 'l':
        for i in range(3):
            board[coords[0]][coords[1]-i] = 'R'
    elif coords[2] == 'r':
        for i in range(3):
            board[coords[0]][coords[1]+i] = 'R'
    elif coords[2] == 'u':
        for i in range(3):
            board[coords[0]-i][coords[1]] = 'R'
    elif coords[2] == 'd':
        for i in range(3):
            board[coords[0]+i][coords[1]] = 'R'
            
    #Submarine
    coords = __getStartCoords__()
    while __checkValidShipPlacement__(3, coords, board) == False:
        coords = __getStartCoords__()
    if coords[2] == 'l':
        for i in range(3):
            board[coords[0]][coords[1]-i] = 'S'
    elif coords[2] == 'r':
        for i in range(3):
            board[coords[0]][coords[1]+i] = 'S'
    elif coords[2] == 'u':
        for i in range(3):
            board[coords[0]-i][coords[1]] = 'S'
    elif coords[2] == 'd':
        for i in range(3):
            board[coords[0]+i][coords[1]] = 'S'
            
    #Destroyer
    coords = __getStartCoords__()
    while __checkValidShipPlacement__(2, coords, board) == False:
        coords = __getStartCoords__()
    if coords[2] == 'l':
        for i in range(2):
            board[coords[0]][coords[1]-i] = 'D'
    elif coords[2] == 'r':
        for i in range(2):
            board[coords[0]][coords[1]+i] = 'D'
    elif coords[2] == 'u':
        for i in range(2):
            board[coords[0]-i][coords[1]] = 'D'
    elif coords[2] == 'd':
        for i in range(2):
            board[coords[0]+i][coords[1]] = 'D'
    return(board)