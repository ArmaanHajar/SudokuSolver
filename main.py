# This file is the main file that runs the program, it is the file that the user runs and interacts with
# The solver.py file contains the backtracking algorithm that solves the sudoku board

from solver import solve_board
import time

rowCount = 9
columnCount = 9
board = []

def print_board(board): # Print the sudoku board
    print("-----------------------")
    for i in range(len(board)): # Iterate through the board
        if i % 3 == 0 and i != 0: # Print a line every 3 rows
            print("-----------------------")
        for j in range(len(board[0])): # Iterate through the row
            if j % 3 == 0 and j != 0: # Print a line every 3 columns
                print(" | ", end = "")
            if j == 8: # Print the last number in the row
                print(board[i][j])
            else: # Print the number in the row
                print(str(board[i][j]) + " ", end = "")
    print("-----------------------")

def manually_enter_board(rowCount, columnCount, board): # Manually enter the sudoku board
    print("Enter the sudoku board row by row")
    print("Enter the number you want then press enter, use 0 for empty spaces.")
    for i in range(rowCount): # Iterate through the board
        rowCount = []
        for j in range(columnCount): # Iterate through the row
            print("Position", i+1, ",", j+1)
            userInput = int(input())
            if userInput < 0 or userInput > 9: # Check if the input is valid
                print("Invalid input. Please try again.")
                print("Position", i+1, ",", j+1)
                userInput = int(input())
            rowCount.append(userInput) # Add the input to the row
        board.append(rowCount) # Add the row to the board
    print("Printing sudoku board:")
    print_board(board)

def pre_generated_board(rowCount, columnCount, board): # Use a pre-generated sudoku board
    print("Which difficulty would you like to play?")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
    print("4: Expert")
    difficulty = int(input("Enter your choice: "))

    if difficulty == 1: # User chose easy difficulty
        file = open("easy.txt", "r")
        for i in range(rowCount): # Iterate through the board
            rowCount = []
            for j in range(columnCount): # Iterate through the row
                rowCount.append(int(file.read(1))) # Add the number to the row
            board.append(rowCount) # Add the row to the board
        file.close()
    elif difficulty == 2: # User chose medium difficulty
        file = open("medium.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    elif difficulty == 3: # User chose hard difficulty
        file = open("hard.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    elif difficulty == 4: # User chose expert difficulty
        file = open("expert.txt", "r")
        for i in range(rowCount):
            rowCount = []
            for j in range(columnCount):
                rowCount.append(int(file.read(1)))
            board.append(rowCount)
        file.close()
    else: # User chose an invalid difficulty
        print("Invalid choice. Please try again.")
        pre_generated_board(rowCount, columnCount, board)
    print("Printing sudoku board:")
    print_board(board)

def save_solution(board): # Save the solution in a text file
    file = open("solution.txt", "w")
    for i in range(len(board)): # Iterate through the board
        for j in range(len(board[0])): # Iterate through the row
            file.write(str(board[i][j])) # Write the number to the file
        file.write("\n")
    file.close()

def welcome(): # Welcome the user and ask them if they want to enter the sudoku manually or use a pre-generated sudoku board
    print("-------------------------------  Sudoku Solver  -----------------------------------")
    print("Welcome to the Sudoku Solver!")
    print("You can either enter the sudoku manually or use a pre-generarted sudoku board")
    print("1: Enter the sudoku manually")
    print("2: Use a pre-generarted sudoku board")

    choice = int(input("Enter your choice: "))
    if choice == 1: # User chose to enter the sudoku manually
        manually_enter_board(rowCount, columnCount, board)
    elif choice == 2: # User chose to use a pre-generated sudoku board
        pre_generated_board(rowCount, columnCount, board)
    else:
        print("Invalid choice. Please try again.")
        welcome()

def solve(board): # Solve the sudoku board
    print("Solving sudoku board...")
    start = time.time() # Start the timer
    solve_board(board) # Solve the board
    end = time.time() # End the timer
    print("Printing solution:")
    print_board(board)
    save_solution(board)
    print("Solution saved in solution.txt")
    print("Time taken to solve:", round(1000*(end - start)), "milliseconds")

def main():
    welcome()
    solve(board)

if __name__ == "__main__":
    main()