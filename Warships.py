#!/usr/bin/env python
#==============================================================================
# Title: Warships
# Author: Ryan Slater
# Date: 10/9/2017
# Changes: Improved Hard Difficulty and other minor tweaks
#==============================================================================

import numpy as np
import AIFleets, AIShots
import names
import matplotlib.pyplot as plt

class player():
    
    def __init__(self, name):
        self.name = name
        self.fleetBoard = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        self.guessBoard = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])

    def __setShip__(self, length, shipName, shipIndex, player):
        for row in range(0, 10):
            for col in range(0, 10):
                if self.fleetBoard[row][col] == shipIndex:
                    self.fleetBoard[row][col] = ' '
        print(500*"\n")
        print("Enter coordinates of the ship in the format \"startLetter, startNumber, direction\"")
        printBoard(self.name, self.fleetBoard, "Fleet", player)
        inpt = ""
        coords = ()
        while True:
            if player == "p1":
                print("\033[1;35;48m" + self.name + "\033[1;37;48m, set your " + shipName)
            else:
                print("\033[1;33;48m" + self.name + "\033[1;37;48m, set your " + shipName)
            inpt = __modInput__(input())
            if inpt != "THISISABADSTRINGSJKLA;FDSIAF380WADSF":
                coords = (__convertAlphaToNum__(inpt[0]), int(inpt[1]), inpt[2])
                if __checkValidShipPlacement__(length, coords, self.fleetBoard) == True:
                    break
                else:
                    print("Enter a valid ship location")
            else:
                print("Enter a valid ship location")
        if coords[2] == 'l':
            for i in range(length):
                self.fleetBoard[coords[0]][coords[1]-i] = shipIndex
        elif coords[2] == 'r':
            for i in range(length):
                self.fleetBoard[coords[0]][coords[1]+i] = shipIndex
        elif coords[2] == 'u':
            for i in range(length):
                self.fleetBoard[coords[0]-i][coords[1]] = shipIndex
        elif coords[2] == 'd':
            for i in range(length):
                self.fleetBoard[coords[0]+i][coords[1]] = shipIndex
        print(500*"\n")
        
        
    def setShips(self, player):
        if player == "p1":
            print("\033[1;35;48m" + self.name + "\033[1;37;48m, would you like a randomly generated fleet?")
        else:
            print("\033[1;33;48m" + self.name + "\033[1;37;48m, would you like a randomly generated fleet?")
        inpt = input().lower()
        if inpt in "yes" or "yes" in inpt:
            self.fleetBoard = AIFleets.getFleet()
            printBoard(self.name, self.fleetBoard, "Fleet", player)
            print("\033[1;37;48mPress Enter to continue")
            x = input()
            print(500*"\n")
        else:
            c, b, r, s, d, = False, False, False, False, False
            options = ["aircraft carrier", "battleship", "cruiser", "submarine", "destroyer"]
            while True:    
                while True:
                    printBoard(self.name, self.fleetBoard, "Fleet", player)
                    if player == "p1":
                        print("\033[1;35;48m" + self.name + "\033[1;37;48m, what ship would you like to place?")
                    else:
                        print("\033[1;33;48m" + self.name + "\033[1;37;48m, what ship would you like to place?")
                    print("       Ship       | Length")
                    print("------------------+-------")
                    for i in range(0, len(options)):
                        x = 18-len(options[i])
                        length = '  3'
                        if options[i] == "aircraft carrier":
                            length = '  5'
                        elif options[i] == "battleship":
                            length = '  4'
                        elif options[i] == "destroyer":
                            length = '  2'
                        print(options[i] + x*' ' + '| ' + length)
                    ship = input().lower()
                    if ship in "aircraftcarrier" or ship in "aircraft carrier":
                        self.__setShip__(5, "carrier", 'C', player)
                        c = True
                    elif ship in "battleship":
                        self.__setShip__(4, "battleship", 'B', player)
                        b = True
                    elif ship in "cruiser":
                        self.__setShip__(3, "cruiser", 'R', player)
                        r = True
                    elif ship in "submarine":
                        self.__setShip__(3, "submarine", 'S', player)
                        s = True
                    elif ship in "destroyer":
                        self.__setShip__(2, "destroyer", 'D', player)
                        d = True
                    else:
                        print("Please enter one of the options")
                    if c == True and b == True and r == True and s == True and d == True:
                        break
                printBoard(self.name, self.fleetBoard, "Fleet", player)
                print("\033[1;37;48mWould you like to edit your fleet?")
                edit = input().lower()
                if edit in "yes" or "yes" in edit:
                    continue
                else:
                    print(500*"\n")
                    break

def __modInput__(string):
    if len(string) > 2:
        stringCoords = []
        letCoordIndex, numCoordIndex = 0, 0
        for i in range(0, len(string)):
            if string[i].lower() in "abcdefghij":
                letCoordIndex = i
                stringCoords.append(string[i].lower())
                break
        for i in range(letCoordIndex+1, len(string)):
            if string[i] in "1234567890":
                numCoordIndex = i
                stringCoords.append(string[i])
                break
        for i in range(numCoordIndex+1, len(string)):
            if string[i].lower() in "udlr":
                stringCoords.append(string[i])
                break
        if len(stringCoords) == 3:
            if stringCoords[0] in "abcdefghij" and stringCoords[1] in "1234567890" and stringCoords[2] in "udlr":
                newString = stringCoords[0] + stringCoords[1] + stringCoords[2]
                return(newString)
        return("THISISABADSTRINGSJKLA;FDSIAF380WADSF")
    else:
        return("THISISABADSTRINGSJKLA;FDSIAF380WADSF")
        
def __convertAlphaToNum__(a):
    if a == 'a' or a == 'A':
        a = 0
    elif a == 'b' or a == 'B':
        a = 1
    elif a == 'c' or a == 'C':
        a = 2
    elif a == 'd' or a == 'D':
        a = 3
    elif a == 'e' or a == 'E':
        a = 4
    elif a == 'f' or a == 'F':
        a = 5
    elif a == 'g' or a == 'G':
        a = 6
    elif a == 'h' or a == 'H':
        a = 7
    elif a == 'i' or a == 'I':
        a = 8
    else:
        a = 9
    return(a)

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

def checkValidShotLocation(guess, player):
    if player == "p1":
        if p1.guessBoard[guess[0]][guess[1]] == 'O' or p1.guessBoard[guess[0]][guess[1]] == 'X':
            return(False)
        return(True)
    elif player == "p2":
        if p2.guessBoard[guess[0]][guess[1]] == 'O' or p2.guessBoard[guess[0]][guess[1]] == 'X':
            return(False)
        return(True)

def printBoard(name, board, boardType, player):
    letters = "ABCDEFGHIJ"
    if player == "p1":
        print("\033[1;35;48m   " + name + "\'s " + boardType)
    else:
        print("\033[1;33;48m   " + name + "\'s " + boardType)
    print("\n\033[1;34;48m  ", end="")
    for i in range(10):
        print("  " + str(i) + " ", end="")
    print("\n  " + 10*"+---", end="+\n")
    for y in range(10):
        print(letters[y] + " ", end="")
        for x in range(10):
            print("|\033[1;30;48m " + board[y][x] + "\033[1;34;48m", end=" ")
        print("| " + letters[y])
        print("  " + 10*"+---", end="+\n")
    print("  ", end="")
    for i in range(10):
        print("  " + str(i) + " ", end="")
    print("\n")

def printBoard2(p1name, p1board, p1boardType, p2name, p2board, p2boardType):
    letters, numbers = "ABCDEFGHIJ", "0123456789"
    spacesBetweenNames = 36 - len(p1name)
    if spacesBetweenNames > 0:
        print("\033[1;35;48m   " + p1name + "\'s " + p1boardType + spacesBetweenNames*" " + "\033[1;33;48m" + p2name + "\'s " + p2boardType)
    else:
        print("\033[1;35;48m   " + p1name + "\'s " + p1boardType + 5*" " + p2name + "\'s " + p2boardType)
    print("\n\033[1;34;48m    " + "   ".join(str(p) for p in numbers) + "       " + "   ".join(str(p) for p in numbers))
    for row in range(0, 10):
        if row == 0:
            print("  " + 10*"+---", end="+")
            print("   " + 10*"+---", end="+ \n")
        else:
            print("\n  " + 10*"+---", end="+")
            print("   " + 10*"+---", end="+ \n")
        print(letters[row], end = " ")
        for col in range(0, 10):
            if p1board[row][col] == 'X':
                print("| " + "\033[1;31;48m" + p1board[row][col] + "\033[1;34;48m ", end="")
            elif p1board[row][col] == 'O' or p1board[row][col] in "01234":
                print("| " + "\033[1;37;48m" + p1board[row][col] + "\033[1;34;48m ", end="")
            elif p1board[row][col] in "CBSRD":
                print("| " + "\033[1;30;48m" + p1board[row][col] + "\033[1;34;48m ", end="")
            else:
                print("| " + p1board[row][col] + "\033[1;34;48m ", end="")
        print("| " + letters[row], end="")
        print(" ", end = "")
        for col in range(0, 10):
            if p2board[row][col] == 'X':
                print("| " + "\033[1;31;48m" + p2board[row][col] + "\033[1;34;48m ", end="")
            elif p2board[row][col] == 'O' or p2board[row][col] in "01234":
                print("| " + "\033[1;37;48m" + p2board[row][col] + "\033[1;34;48m ", end="")
            elif p2board[row][col] in "CBSRD":
                print("| " + "\033[1;30;48m" + p2board[row][col] + "\033[1;34;48m ", end="")
            else:
                print("| " + p2board[row][col] + "\033[1;34;48m ", end="")
        print("| " + letters[row], end="")
    print("\n" + "  " + 10*"+---" + "+   " + 10*"+---", end="+\n")
    print("    " + "   ".join(str(p) for p in numbers) + "       " + "   ".join(str(p) for p in numbers))

def checkHitOrMiss(player, guess):
    if player == "p1":
        if p2.fleetBoard[guess[0]][guess[1]] != ' ':
            return("hit")
        return("miss")
    elif player == "p2":
        if p1.fleetBoard[guess[0]][guess[1]] != ' ':
            return("hit")
        return("miss")

def checkShotSyntax(guess):
    if len(guess) == 2:
        if guess[0] in "ABCDEFGHIJabcdefghij" and guess[1] in "0123456789":
            return(True)
        return(False)

def fire(player, guess, minesweeper):
    if player == 'p1':
        if checkHitOrMiss(player, guess) == 'miss':
            if minesweeper == True:
                p1.guessBoard[guess[0]][guess[1]] = __minesweeperMiss__(p2.fleetBoard, guess)
            else:
                p1.guessBoard[guess[0]][guess[1]] = 'O'
        elif checkHitOrMiss(player, guess) == 'hit':
            p1.guessBoard[guess[0]][guess[1]] = 'X'
    elif player == 'p2':
        if checkHitOrMiss(player, guess) == 'miss':
            if minesweeper == True:
                p2.guessBoard[guess[0]][guess[1]] = __minesweeperMiss__(p1.fleetBoard, guess)
            else:
                p2.guessBoard[guess[0]][guess[1]] = 'O'
        elif checkHitOrMiss(player, guess) == 'hit':
            p2.guessBoard[guess[0]][guess[1]] = 'X'

def __minesweeperMiss__(fleetBoard, guess):
    marker = 0
    if guess[0] > 0:
        if fleetBoard[guess[0]-1][guess[1]] != ' ':
            marker += 1
    if guess[0] < 9:
        if fleetBoard[guess[0]+1][guess[1]] != ' ':
            marker += 1
    if guess[1] > 0:
        if fleetBoard[guess[0]][guess[1]-1] != ' ':
            marker += 1
    if guess[1] < 9:
        if fleetBoard[guess[0]][guess[1]+1] != ' ':
            marker += 1
    return(str(marker))

def checkForSunkShips(player, p1c, p1b, p1d, p1s, p1r, p2c, p2b, p2d, p2s, p2r):
    carrierCount, battleshipCount, cruiserCount, subCount,  destroyerCount = 0, 0, 0, 0, 0
    if player == "p1":
        for y in range(10):
            for x in range(10):
                if p1.guessBoard[y][x] == 'X':
                    if p2.fleetBoard[y][x] == 'C':
                        carrierCount += 1
                    elif p2.fleetBoard[y][x] == 'B':
                        battleshipCount += 1
                    elif p2.fleetBoard[y][x] == 'R':
                        cruiserCount += 1
                    elif p2.fleetBoard[y][x] == 'S':
                        subCount += 1
                    elif p2.fleetBoard[y][x] == 'D':
                         destroyerCount += 1
        if carrierCount == 5 and p2c == False:
            return("aircraft carrier")
        elif battleshipCount == 4 and p2b == False:
            return("battleship")
        elif cruiserCount == 3 and p2r == False:
            return("cruiser")
        elif subCount == 3 and p2s == False:
            return("submarine")
        elif destroyerCount == 2 and p2d == False:
            return("destroyer")
        else:
            return("no")

    elif player == "p2":
        for y in range(10):
            for x in range(10):
                if p2.guessBoard[y][x] == 'X':
                    if p1.fleetBoard[y][x] == 'C':
                        carrierCount += 1
                    elif p1.fleetBoard[y][x] == 'B':
                        battleshipCount += 1
                    elif p1.fleetBoard[y][x] == 'R':
                        cruiserCount += 1
                    elif p1.fleetBoard[y][x] == 'S':
                        subCount += 1
                    elif p1.fleetBoard[y][x] == 'D':
                         destroyerCount += 1
        if carrierCount == 5 and p1c == False:
            return("aircraft carrier")
        elif battleshipCount == 4 and p1b == False:
            return("battleship")
        elif cruiserCount == 3 and p1r == False:
            return("cruiser")
        elif subCount == 3 and p1s == False:
            return("submarine")
        elif destroyerCount == 2 and p1d == False:
            return("destroyer")
        else:
            return("no")

def makeAIPrintBoard():
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
    for row in range(0, 10):
        for col in range(0, 10):
            board[row][col] = p1.fleetBoard[row][col]
            if p2.guessBoard[row][col] != ' ':
                board[row][col] = p2.guessBoard[row][col]
    return(board)

def makeFinalBoard(player):
    if player == "p1":
        finalBoard = p1.fleetBoard
        for x in range(0, 10):
            for y in range(0, 10):
                if p2.guessBoard[x][y] != ' ':
                    finalBoard[x][y] = p2.guessBoard[x][y]
    else:
        finalBoard = p2.fleetBoard
        for x in range(0, 10):
            for y in range(0, 10):
                if p1.guessBoard[x][y] != ' ':
                    finalBoard[x][y] = p1.guessBoard[x][y]
    return(finalBoard)





p1c, p1b, p1d, p1s, p1r, p2c, p2b, p2d, p2s, p2r = False, False, False, False, False, False, False, False, False, False
winner = ""

print("How many players?")
while True:
    numPlayers = input()
    if numPlayers == '1':
        break
    elif numPlayers == '2':
        break
    else:
        print("Please enter \'1\' or \'2\'")

#============================== 1 Player ==============================================================
if numPlayers == '1':
    AIMode = "search"
    AIDiff = 0;
    print("What\'s your name?")
    name = input()
    p1 = player("Admiral " + name)
    p2 = player("Admiral " + names.get_last_name())
    while True:
        print("Select AI Difficulty:\nEasy     Medium     Hard")
        inpt = input()
        if inpt.lower() == "easy" or inpt.lower() == 'e':
            AIDiff = 1
            break
        elif inpt.lower() == "medium" or inpt.lower() == 'm':
            AIDiff = 2
            break
        elif inpt.lower() == "hard" or inpt.lower() == 'h':
            AIDiff = 3
            break
    p1.setShips("p1")
    p2.fleetBoard = AIFleets.getFleet()
    p2.guessBoard = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
    AITargetBoard = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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

        #Player 1
        print(500*"\n")
        p2AIBoard = makeAIPrintBoard()
        printBoard2(p1.name, p1.guessBoard, "Radar", p2.name, p2AIBoard, "Radar")
        print("\033[1;37;48m")
        #AIShots.__printHeatMap__([p1c, p1b, p1r, p1s, p1d], p2.guessBoard, AIMode)
        #-----------------------------------------------------
        AIGuess = AIShots.search(3, [p1c, p1b, p1r, p1s, p1d], p2.guessBoard)
#        AIShots.__printHeatMap__([p1c, p1b, p1r, p1s, p1d], p2.guessBoard)
        #-----------------------------------------------------
        p1Sunk = []
        if p1c == True:
            p1Sunk.append("aircraft carrier")
        if p1b == True:
            p1Sunk.append("battleship")
        if p1s == True:
            p1Sunk.append("submarine")
        if p1r == True:
            p1Sunk.append("cruiser")
        if p1d == True:
            p1Sunk.append("destroyer")
        p2Sunk = []
        if p2c == True:
            p2Sunk.append("aircraft carrier")
        if p2b == True:
            p2Sunk.append("battleship")
        if p2s == True:
            p2Sunk.append("submarine")
        if p2r == True:
            p2Sunk.append("cruiser")
        if p2d == True:
            p2Sunk.append("destroyer")
        if len(p2Sunk) > 0:
            print("\033[1;35;48m" + p1.name + "\033[1;37;48m has sunk the enemy's " + ", ".join(str(p) for p in p2Sunk))
        else:
            print("\033[1;35;48m" + p1.name + "\033[1;37;48m has sunk \033[1;31;48mnone\033[1;37;48m of the enemy's ships")
        if len(p1Sunk) > 0:
            print("\033[1;33;48m" + p2.name + "\033[1;37;48m has sunk the enemy's " + ", ".join(str(p) for p in p1Sunk))
        else:
            print("\033[1;33;48m" + p2.name + "\033[1;37;48m has sunk \033[1;31;48mnone\033[1;37;48m of the enemy's ships")
        print("\033[1;35;48m" + p1.name + "\033[1;37;48m, enter coordinates:")
        inpt = input()
        while True:
            if checkShotSyntax(inpt) == True:
                guess = (__convertAlphaToNum__(inpt[0]), int(inpt[1]))
                if checkValidShotLocation(guess, "p1") == True:
                    break
                else:
                    print("Illegal shot")
            else:
                print("Enter coordinates in correct format")
            inpt = input()
        fire("p1", guess, False)
        print(500*"\n")
        sunk = checkForSunkShips("p1", p1c, p1b, p1d, p1s, p1r, p2c, p2b, p2d, p2s, p2r)
        if p2c == False and sunk == "aircraft carrier":
            p2c = True
        elif p2b == False and sunk == "battleship":
            p2b = True
        elif p2r == False and sunk == "cruiser":
            p2r = True
        elif p2s == False and sunk == "submarine":
            p2s = True
        elif p2d == False and sunk == "destroyer":
            p2d = True
        if p2c == True and p2b == True and p2d == True and p2s == True and p2r == True:
            winner = "p1"
            gameOver = True
            break


#=====================AI====================================

#==================================Perfet Game Code================================================
#        for row in range(0, 10):
#            for col in range(0, 10):
#                if p2.guessBoard[row][col] == ' ' and p1.fleetBoard[row][col] != ' ':
#                    AIGuess = (row, col)
#==================================================================================================


        AIGuess = (0, 0)
        #Easy AI
        if AIDiff == 1:
            AIMode = AIShots.updateMode()
            if AIMode == "search":
                AIGuess = AIShots.search(1, [], p2.guessBoard)
            elif AIMode == "target":
                AIGuess = AIShots.target(1, [])

        #Medium AI
        elif AIDiff == 2:
            AIMode = AIShots.updateMode()
            if AIMode == "search":
                AIGuess = AIShots.search(2, [], p2.guessBoard)
            elif AIMode == "target":
                AIGuess = AIShots.target(2, [])
                
        #Hard AI
        elif AIDiff == 3:
            AIMode = AIShots.updateMode()
            if AIMode == "search":
                AIGuess = AIShots.search(3, [p1c, p1b, p1r, p1s, p1d], p2.guessBoard)
            elif AIMode == "target":
                AIGuess = AIShots.target(3, [p1c, p1b, p1r, p1s, p1d])



#----------------------------------------------------------------------------------------------------------------
        fire("p2", AIGuess, False)
        if checkHitOrMiss("p2", AIGuess) == "hit":
            AIMode = "target"
            AIShots.updateAIBoard(AIGuess, 'X')
        else:
            AIShots.updateAIBoard(AIGuess, 'O')
        sunk = checkForSunkShips("p2", p1c, p1b, p1d, p1s, p1r, p2c, p2b, p2d, p2s, p2r)
        if p1c == False and sunk == "aircraft carrier":
            p1c = True
            AIMode = AIShots.updateMode()
            carrierCoords = []
            for row in range(0, 10):
                for col in range(0, 10):
                    if p1.fleetBoard[row][col] == 'C':
                        carrierCoords.append((row, col))
            AIShots.updateAIBoardSinking(carrierCoords)
        elif p1b == False and sunk == "battleship":
            p1b = True
            battleshipCoords = []
            for row in range(0, 10):
                for col in range(0, 10):
                    if p1.fleetBoard[row][col] == 'B':
                        battleshipCoords.append((row, col))
            AIShots.updateAIBoardSinking(battleshipCoords)
        elif p1r == False and sunk == "cruiser":
            p1r = True
            cruiserCoords = []
            for row in range(0, 10):
                for col in range(0, 10):
                    if p1.fleetBoard[row][col] == 'R':
                        cruiserCoords.append((row, col))
            AIShots.updateAIBoardSinking(cruiserCoords)
        elif p1s == False and sunk == "submarine":
            p1s = True
            subCoords = []
            for row in range(0, 10):
                for col in range(0, 10):
                    if p1.fleetBoard[row][col] == 'S':
                        subCoords.append((row, col))
            AIShots.updateAIBoardSinking(subCoords)
        elif p1d == False and sunk == "destroyer":
            p1d = True
            destroyerCoords = []
            for row in range(0, 10):
                for col in range(0, 10):
                    if p1.fleetBoard[row][col] == 'D':
                        destroyerCoords.append((row, col))
            AIShots.updateAIBoardSinking(destroyerCoords)
        if p1c == True and p1b == True and p1d == True and p1s == True and p1r == True:
            winner = "p2"
            gameOver = True
            break



#======================================================================================================

#============================== 2 Player ==============================================================
if numPlayers == "2":
    moreShotsVersion = False
    minesweeper = False
    gameOver = False

    print("Play the realistic version? (type 'info' for details)")
    inpt = input().lower()
    if inpt in "info" or "info" in inpt:
        print("In this version of Battleship, you get as many shots per turn as you have operational ships.\
              \nAs the game goes on, players get less and less shots as their ships get sunk!")
        print("Would you like to play the realistic version?")
        inpt = input().lower()
        if inpt in "yes" or "yes" in inpt:
            moreShotsVersion = True
    elif inpt in "yes" or "yes" in inpt:
        moreShotsVersion = True

    print("Enable Minesweeper-style miss icons? (type 'info' for details)")
    inpt = input().lower()
    if inpt in "info" or "info" in inpt:
        print("Miss icons become numer of ships adjacent to missed shot")
        print("Enable Minesweeper-style miss icons?")
        inpt = input().lower()
        if inpt in "yes" or "yes" in inpt:
            minesweeper = True
    elif inpt in "yes" or "yes" in inpt:
        minesweeper = True


    print("Player 1, what\'s your name?")
    p1 = player("Admiral " + input())
    print("Player 2, what\'s your name?")
    p2 = player("Admiral " + input())
    p1.setShips("p1")
    p2.setShips("p2")
    printBoard(p1.name, p1.fleetBoard, "Fleet", "p1")
    printBoard(p2.name, p2.fleetBoard, "Fleet", "p2")
    
    
    while gameOver == False:
        
#===========PLAYER 1==============================================
        if moreShotsVersion == True:
            p1Turns = 0
            if p1c == False:
                p1Turns += 1
            if p1b == False:
                p1Turns += 1
            if p1d == False:
                p1Turns += 1
            if p1s == False:
                p1Turns += 1
            if p1r == False:
                p1Turns += 1
        else:
            p1Turns = 1
        for i in range(0, p1Turns):
            print(500*"\n")
            printBoard2(p1.name, p1.guessBoard, "Radar", p2.name, p2.guessBoard, "Radar")
            print("\033[1;37;48m")
            p1Sunk = []
            if p1c == True:
                p1Sunk.append("aircraft carrier")
            if p1b == True:
                p1Sunk.append("battleship")
            if p1s == True:
                p1Sunk.append("submarine")
            if p1r == True:
                p1Sunk.append("cruiser")
            if p1d == True:
                p1Sunk.append("destroyer")
            p2Sunk = []
            if p2c == True:
                p2Sunk.append("aircraft carrier")
            if p2b == True:
                p2Sunk.append("battleship")
            if p2s == True:
                p2Sunk.append("submarine")
            if p2r == True:
                p2Sunk.append("cruiser")
            if p2d == True:
                p2Sunk.append("destroyer")
            if len(p2Sunk) > 0:
                print("\033[1;35;48m" + p1.name + "\033[1;37;48m has sunk the enemy's " + ", ".join(str(p) for p in p2Sunk))
            else:
                print("\033[1;35;48m" + p1.name + "\033[1;37;48m has sunk \033[1;31;48mnone\033[1;37;48m of the enemy's ships")
            if len(p1Sunk) > 0:
                print("\033[1;33;48m" + p2.name + "\033[1;37;48m has sunk the enemy's " + ", ".join(str(p) for p in p1Sunk))
            else:
                print("\033[1;33;48m" + p2.name + "\033[1;37;48m has sunk \033[1;31;48mnone\033[1;37;48m of the enemy's ships")
            print("\033[1;35;48m" + p1.name + "\033[1;37;48m, enter coordinates:")
            inpt = input()
            while True:
                if checkShotSyntax(inpt) == True:
                    guess = (__convertAlphaToNum__(inpt[0]), int(inpt[1]))
                    if checkValidShotLocation(guess, "p1") == True:
                        break
                    else:
                        print("Illegal shot")
                else:
                    print("Enter coordinates in correct format")
                inpt = input()
            fire("p1", guess, minesweeper)
            print(500*"\n")
            sunk = checkForSunkShips("p1", p1c, p1b, p1d, p1s, p1r, p2c, p2b, p2d, p2s, p2r)
            if p2c == False and sunk == "aircraft carrier":
                p2c = True
            elif p2b == False and sunk == "battleship":
                p2b = True
            elif p2r == False and sunk == "cruiser":
                p2r = True
            elif p2s == False and sunk == "submarine":
                p2s = True
            elif p2d == False and sunk == "destroyer":
                p2d = True
            if p2c == True and p2b == True and p2d == True and p2s == True and p2r == True:
                winner = "p1"
                gameOver = True
                break
            
        if gameOver == True:
            break
        
#===========PLAYER 2==============================================   
        if moreShotsVersion == True:
            p2Turns = 0
            if p2c == False:
                p2Turns += 1
            if p2b == False:
                p2Turns += 1
            if p2d == False:
                p2Turns += 1
            if p2s == False:
                p2Turns += 1
            if p2r == False:
                p2Turns += 1
        else:
            p2Turns = 1
        for i in range(0, p2Turns):
            print(500*"\n")
            printBoard2(p1.name, p1.guessBoard, "Radar", p2.name, p2.guessBoard, "Radar")
            print("\033[1;37;48m")
            p1Sunk = []
            if p1c == True:
                p1Sunk.append("aircraft carrier")
            if p1b == True:
                p1Sunk.append("battleship")
            if p1s == True:
                p1Sunk.append("submarine")
            if p1r == True:
                p1Sunk.append("cruiser")
            if p1d == True:
                p1Sunk.append("destroyer")
            p2Sunk = []
            if p2c == True:
                p2Sunk.append("aircraft carrier")
            if p2b == True:
                p2Sunk.append("battleship")
            if p2s == True:
                p2Sunk.append("submarine")
            if p2r == True:
                p2Sunk.append("cruiser")
            if p2d == True:
                p2Sunk.append("destroyer")
            if len(p2Sunk) > 0:
                print("\033[1;35;48m" + p1.name + "\033[1;37;48m has sunk the enemy's " + ", ".join(str(p) for p in p2Sunk))
            else:
                print("\033[1;35;48m" + p1.name + "\033[1;37;48m has sunk \033[1;31;48mnone\033[1;37;48m of the enemy's ships")
            if len(p1Sunk) > 0:
                print("\033[1;33;48m" + p2.name + "\033[1;37;48m has sunk the enemy's " + ", ".join(str(p) for p in p1Sunk))
            else:
                print("\033[1;33;48m" + p2.name + "\033[1;37;48m has sunk \033[1;31;48mnone\033[1;37;48m of the enemy's ships")
            print("\033[1;33;48m" + p2.name + "\033[1;37;48m, enter coordinates:")
            inpt = input()
            while True:
                if checkShotSyntax(inpt) == True:
                    guess = (__convertAlphaToNum__(inpt[0]), int(inpt[1]))
                    if checkValidShotLocation(guess, "p2") == True:
                        break
                    else:
                        print("Illegal shot")
                else:
                    print("Enter coordinates in correct format")
                inpt = input()
            fire("p2", guess, minesweeper)
            print(500*"\n")
            sunk = checkForSunkShips("p2", p1c, p1b, p1d, p1s, p1r, p2c, p2b, p2d, p2s, p2r)
            if p1c == False and sunk == "aircraft carrier":
                p1c = True
            elif p1b == False and sunk == "battleship":
                p1b = True
            elif p1r == False and sunk == "cruiser":
                p1r = True
            elif p1s == False and sunk == "submarine":
                p1s = True
            elif p1d == False and sunk == "destroyer":
                p1d = True
            if p1c == True and p1b == True and p1d == True and p1s == True and p1r == True:
                winner = "p2"
                gameOver = True
                break
            
            
            

#============================================================================================

print(500*"\n")
p1FinalBoard = makeFinalBoard("p1")
p2FinalBoard = makeFinalBoard("p2")


if winner == "p1":
    print("\033[1;35;48m" + p1.name + "\033[1;37;48m wins!\n")
    p1Sunk = []
    if p1c == True:
        p1Sunk.append("aircraft carrier")
    if p1b == True:
        p1Sunk.append("battleship")
    if p1r == True:
        p1Sunk.append("cruiser")
    if p1s == True:
        p1Sunk.append("submarine")
    if p1d == True:
        p1Sunk.append("destroyer")
    if len(p1Sunk) == 0:
        print("\033[1;33;48m" + p2.name + "\033[1;37;48m sunk none of \033[1;35;48m" + p1.name + "\033[1;37;48m\'s ships!")
    else:
        print("\033[1;33;48m" + p2.name + "\033[1;37;48m sunk \033[1;35;48m" + p1.name + "'s\033[1;37;48m ", end="")
        print(", ".join(str(p) for p in p1Sunk))
elif winner == "p2":
    print("\033[1;33;48m" + p2.name + "\033[1;37;48m wins!\n")
    p2Sunk = []
    if p2c == True:
        p2Sunk.append("aircraft carrier")
    if p2b == True:
        p2Sunk.append("battleship")
    if p2r == True:
        p2Sunk.append("cruiser")
    if p2s == True:
        p2Sunk.append("submarine")
    if p2d == True:
        p2Sunk.append("destroyer")
    if len(p2Sunk) == 0:
        print("\033[1;35;48m" + p1.name + "\033[1;37;48m sunk none of \033[1;33;48m" + p2.name + "\033[1;37;48m\'s ships!")
    else:
        print("\033[1;35;48m" + p1.name + "\033[1;37;48m sunk \033[1;33;48m" + p2.name + "'s\033[1;37;48m ", end="")
        print(", ".join(str(p) for p in p2Sunk))

print("")
printBoard2(p1.name, p1FinalBoard, "Fleet", p2.name, p2FinalBoard, "Fleet")
