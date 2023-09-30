#!/usr/bin/python3
# BEGIN: xy7z89abcde1
"""This program solves the N-queens puzzle by determining all possible solutions to placing N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def is_safe(board, row, col, n):
    """
    Check if a given position is safe for a queen.
    """
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    """
    Recursive function to place queens on the board.
    """
    # Base case: all queens have been placed
    if col == n:
        # Print the board as a solution
        for row in board:
            print(str(row).replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))
        return True

    # Recursive case: try to place a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            # Place the queen on the board
            board[row][col] = 1

            # Recursively place queens on the remaining columns
            solve_n_queens(board, col + 1, n)

            # Backtrack: remove the queen from the board
            board[row][col] = 0

    return False

if __name__ == '__main__':
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the argument provided is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty board
    board = [[0 for x in range(n)] for y in range(n)]

    # Solve the N queens problem
    solve_n_queens(board, 0, n)
