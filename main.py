"""
Sudoku solver in Python using the console and the backtracking algorithm
You can either enter the sudoku manually or use a pre-generarted sudoku board
The sudoku board is printed in the console and the solution is printed in the console
The solution is also saved in a text file called solution.txt

Author: Armaan Hajar
Date Started: August 24th, 2023
Date Finished: 
"""

# This file is the main file that runs the program, it is the file that the user runs and interacts with
# The solver.py file contains the backtracking algorithm that solves the sudoku board

from solver import solve_board

rowCount = 9
columnCount = 9
board = []

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

def manually_enter_board(rowCount, columnCount, board):
    print("Enter the sudoku board row by row")
    print("Enter the number you want then press enter, use 0 for empty spaces.")
    for i in range(rowCount):
        rowCount = []
        for j in range(columnCount):
            print("Position", i+1, ",", j+1)
            userInput = int(input())
            if userInput < 0 or userInput > 9:
                print("Invalid input. Please try again.")
                print("Position", i+1, ",", j+1)
                userInput = int(input())
            rowCount.append(userInput)
        board.append(rowCount)
    print("Printing sudoku board:")
    print_board(board)

def pre_generated_board(rowCount, columnCount, board):
    print("Which difficulty would you like to play?")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    print("4: Expert")
    difficulty = int(input("Enter your choice: "))

    if difficulty == 1:
        file = open("easy.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    elif difficulty == 2:
        file = open("medium.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    elif difficulty == 3:
        file = open("hard.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    elif difficulty == 4:
        file = open("expert.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    else:
        print("Invalid choice. Please try again.")
        pre_generated_board(rowCount, columnCount, board)
    print("Printing sudoku board:")
    print_board(board)

def save_solution(board):
    file = open("solution.txt", "w")
    for i in range(len(board)):
        for j in range(len(board[0])):
            file.write(str(board[i][j]))
        file.write("\n")
    file.close()

def welcome():
    print("-------------------------------  Sudoku Solver  -----------------------------------")
    print("Welcome to the Sudoku Solver!")
    print("You can either enter the sudoku manually or use a pre-generarted sudoku board")
    print("1: Enter the sudoku manually")
    print("2: Use a pre-generarted sudoku board")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        manually_enter_board(rowCount, columnCount, board)
    elif choice == 2:
        pre_generated_board(rowCount, columnCount, board)
    else:
        print("Invalid choice. Please try again.")
        welcome()
    print("Solving sudoku board...")
    solve_board(board)
    print("Printing solution:")
    print_board(board)
    save_solution(board)

if __name__ == "__main__":
    welcome()