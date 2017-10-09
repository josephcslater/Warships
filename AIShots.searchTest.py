#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:57:19 2017

@author: rjslater
"""

import AIShots
import numpy as np
import random

# =============================================================================
# print(AIShots.search(3, [False, False, False, False, False]), "2")
# print(AIShots.search(3, [False, False, False, False, True]), "3")
# print(AIShots.search(3, [False, False, False, True, True]), "3")
# print(AIShots.search(3, [False, False, True, False, True]), "3")
# print(AIShots.search(3, [False, False, True, True, True]), "4")
# print(AIShots.search(3, [False, True, True, True, True]), "5")
# print(AIShots.search(3, [True, False, True, True, True]), "4")
# print(AIShots.search(3, [True, False, False, False, False]), "2")
# print(AIShots.search(3, [False, True, False, False, False]), "2")
# print(AIShots.search(3, [False, False, True, False, False]), "2")
# print(AIShots.search(3, [False, False, False, True, False]), "2")
# =============================================================================

# =============================================================================
# board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
# 
# for i in range(0, 1000):
#     guess = AIShots.search(3, [False, False, False, False, False])
#     board[guess[0]][guess[1]] = 'X'
# print("Smallest ship = 2:")
# print(board)
# 
# 
# print(5*"\n")
# board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
# 
# for i in range(0, 1000):
#     guess = AIShots.search(3, [False, False, False, False, True])
#     board[guess[0]][guess[1]] = 'X'
# print("Smallest ship = 3:")
# print(board)
# 
# print(5*"\n")
# board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
# 
# for i in range(0, 1000):
#     guess = AIShots.search(3, [False, False, True, True, True])
#     board[guess[0]][guess[1]] = 'X'
# print("Smallest ship = 4:")
# print(board)
# 
# print(5*"\n")
# board = np.array([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
# 
# for i in range(0, 1000):
#     guess = AIShots.search(3, [False, True, True, True, True])
#     board[guess[0]][guess[1]] = 'X'
# print("Smallest ship = 5:")
# print(board)
# =============================================================================



def search(diff, sunkShips):
    guess = (0, 0)
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if diff == 3:
            smallestShipSize = 2
            if sunkShips[4] == True:
                smallestShipSize = 3
            if sunkShips[4] == True and sunkShips[3] == True and sunkShips[2] == True:
                smallestShipSize = 4
            if sunkShips[4] == True and sunkShips[3] == True and sunkShips[2] == True and sunkShips[1] == True:
                smallestShipSize = 5
            if (1+row)%smallestShipSize == (1+col)%smallestShipSize:
                guess = (row, col)
                print(smallestShipSize)
                return guess
            
search(3, [False, False, False, False, True])