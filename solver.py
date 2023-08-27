# This file will contain the solver for the sudoku board
# It will be using the backtracking algorithm to solve the board

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def check_valid(board, number, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True

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