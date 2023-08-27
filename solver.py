# This file will contain the solver for the sudoku board
# It will be using the backtracking algorithm to solve the board

def find_empty(board): # Find the next empty space
    for i in range(len(board)): # Iterate through the board
        for j in range(len(board[0])):
            if board[i][j] == 0: # If the space is empty,
                return (i, j) # Return the position
    return None # If there are no empty spaces, return None

def check_valid(board, number, position): # Check if the number is valid
    # Check row
    for i in range(len(board[0])): # Iterate through the row
        if board[position[0]][i] == number and position[1] != i: # If the number is already in the row, return False
            return False
    # Check column
    for i in range(len(board)): # Iterate through the column
        if board[i][position[1]] == number and position[0] != i: # If the number is already in the column, return False
            return False
    # Check box
    box_x = position[1] // 3 # Get the boxes x coordinate
    box_y = position[0] // 3 # Get the boxes y coordinate
    for i in range(box_y * 3, box_y * 3 + 3): # Iterate through the box
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position: # If the number is already in the box, return False
                return False
    return True # If the number is not in the row, column, or box, return True

def solve_board(board): # Backtracking algorithm
    find = find_empty(board)
    if not find: # If find is None, board is solved
        return True
    else: # If find is not None, board is not solved
        row, column = find
    for i in range(1, 10): 
        if check_valid(board, i, (row, column)): # If the number is valid, add it to the board
            board[row][column] = i
            if solve_board(board): # If the board is solved, return True
                return True
            else: # If the board is not solved, backtrack
                board[row][column] = 0
    return False 