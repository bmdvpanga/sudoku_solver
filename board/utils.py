import numpy as np
from django.shortcuts import render


class SudokuSolver:
    def __init__(self, request):
        self.board = np.empty([9,9], dtype=int)
        for i in range(9):
            for j in range(9):
                key = str(i+1)+str(j+1)
                self.board[i][j] = request.POST.get(key,'')
    def check_board(self,board, coordinates, value):
        ''' Function takes the column and the row of the board that is validated 
            Parameters:
                board
                coordinates -> tuple,  (Y, X)
                value to be checked
            Returns True if value being checked does not exist
        '''
        y = coordinates[0]
        x = coordinates[1]

        # check y
        for i in range (0, 9):
            if ( board[i][x] == value and i != y):
                return False

        #check x
        for i in range (0, 9):
            if ( board[y][i] == value and i != x):
                return False

        #check the box
        box_x = ( x // 3) * 3
        box_y = ( y // 3) * 3

        for i in range(box_y, box_y + 3):
            for j in range(box_x, box_x + 3):
                if(board[i][j] == value and (i, j) != coordinates):
                    return False

        return True

    def solve_board(self,board):
        ''' Recursive function to individually fill out squares marked 0 (empty)
            Backtracks if the solution is not correct
        '''
        for row in range(0,9):
            for col in range(0,9):
                #If the current location is empty, then we start brute forcing the guess value
                if(board[row][col] == 0):
                    for guess in range(1,10):
                        if( self.check_board(board, (row,col), guess) ):
                            board[row][col] = guess
                            #Call the function with the updated board
                            self.solve_board(board)
                            #if we are unable to solve this using the cur value, then we backrack and change position back to 0
                            board[row][col] = 0
                    return
        print(np.matrix(board))