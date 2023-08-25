"""
Sudoku solver in Python using the console and the backtracking algorithm
You can either enter the sudoku manually or use a randomly generarted sudoku board
The sudoku board is printed in the console and the solution is printed in the console
The solution is also saved in a text file called "solution.txt"
The sudoku board is saved in a text file called "sudoku.txt"

Author: Armaan Hajar
Date Started: August 24th, 2023
Date Finished: 
"""

rows = 9
columns = 9
boxes = 9
board = []

def create_board(rows, columns, board):
    for i in range(rows):
        rows = []
        for j in range(columns):
            rows.append(0)
        board.append(rows)

def print_board(board):
    print("-----------------------")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")
    print("-----------------------")

def manually_enter_board(rows, columns, board):
    print("Enter the sudoku board row by row")
    print("Enter the number you want then press enter, use 0 for empty spaces.")
    for i in range(rows):
        userInput = int(input())
        rows = []
        for j in range(columns):
            rows.append(userInput)
        board.append(rows)

def randomly_generate_board(board):
    print("Printing randomly generated sudoku board:")
    print_board(board)

def welcome():
    print("-------------------------------  Sudoku Solver  -----------------------------------")
    print("Welcome to the Sudoku Solver!")
    print("You can either enter the sudoku manually or use a randomly generarted sudoku board")
    print("1: Enter the sudoku manually")
    print("2: Use a randomly generarted sudoku board")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        manually_enter_board(rows, columns, board)
    elif choice == 2:
        randomly_generate_board(board)
    else:
        print("Invalid choice. Please try again.")
        welcome()

if __name__ == "__main__":
    welcome()
    manually_enter_board(rows, columns, board)
    randomly_generate_board(board)
    create_board(rows, columns, board)
    print_board(board)
