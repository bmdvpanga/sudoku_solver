import numpy as np

board =  [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]

        # [
        #     [8,7,6,2,5,4,3,1,0],
        #     [3,0,0,0,5,9,0,0,0],
        #     [0,9,6,0,0,7,0,1,0],
        #     [1,0,0,8,0,0,9,0,0],
        #     [0,0,2,4,0,6,8,0,0],
        #     [0,0,9,0,0,1,0,0,3],
        #     [0,5,0,6,0,0,7,2,0],
        #     [0,0,0,7,3,0,0,0,6],
        #     [0,0,0,0,0,5,0,0,8]
        # ]

def check_board(coordinates, value):
    global board
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

def solve_board():
    ''' Recursive function to individually fill out squares marked 0 (empty)
        Backtracks if the solution is not correct
     '''
    for row in range(0,9):
        for col in range(0,9):
            #If the current location is empty, then we start brute forcing the guess value
            if(board[row][col] == 0):
                for guess in range(1,10):
                    if( check_board((row,col), guess) ):
                        board[row][col] = guess
                        #Call the function with the updated board
                        solve_board()
                        #if we are unable to solve this using the cur value, then we backrack and change position back to 0
                        board[row][col] = 0
                return
    print(np.matrix(board))

if __name__ == "__main__":
    print(np.matrix(board))
    print("====================================================================================")
    solve_board()
