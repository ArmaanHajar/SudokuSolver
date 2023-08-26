"""
Sudoku solver in Python using the console and the backtracking algorithm
You can either enter the sudoku manually or use a pre-generarted sudoku board
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
        rows = []
        for j in range(columns):
            print("Position", i+1, ",", j+1)
            userInput = int(input())
            if userInput < 0 or userInput > 9:
                print("Invalid input. Please try again.")
                print("Position", i+1, ",", j+1)
                userInput = int(input())
            rows.append(userInput)
        board.append(rows)
    print("Printing sudoku board:")
    print_board(board)

def pre_generated_board(rows, columns, board):
    print("Which difficulty would you like to play?")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    print("4: Expert")
    difficulty = int(input("Enter your choice: "))

    if difficulty == 1:
        file = open("easy.txt", "r")
        for i in range(rows):
            rows = []
            for j in range(columns):
                rows.append(int(file.read(1)))
            board.append(rows)
        file.close()
    elif difficulty == 2:
        file = open("medium.txt", "r")
        for i in range(rows):
            rows = []
            for j in range(columns):
                rows.append(int(file.read(1)))
            board.append(rows)
        file.close()
    elif difficulty == 3:
        file = open("hard.txt", "r")
        for i in range(rows):
            rows = []
            for j in range(columns):
                rows.append(int(file.read(1)))
            board.append(rows)
        file.close()
    elif difficulty == 4:
        file = open("expert.txt", "r")
        for i in range(rows):
            rows = []
            for j in range(columns):
                rows.append(int(file.read(1)))
            board.append(rows)
        file.close()
    else:
        print("Invalid choice. Please try again.")
        pre_generated_board(rows, columns, board)
    print("Printing sudoku board:")
    print_board(board)

def welcome():
    print("-------------------------------  Sudoku Solver  -----------------------------------")
    print("Welcome to the Sudoku Solver!")
    print("You can either enter the sudoku manually or use a pre-generarted sudoku board")
    print("1: Enter the sudoku manually")
    print("2: Use a pre-generarted sudoku board")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        manually_enter_board(rows, columns, board)
    elif choice == 2:
        pre_generated_board(rows, columns, board)
    else:
        print("Invalid choice. Please try again.")
        welcome()

if __name__ == "__main__":
    create_board(rows, columns, board)
    welcome()