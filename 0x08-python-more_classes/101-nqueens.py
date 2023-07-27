#!/usr/bin/python3
import sys

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        # Check if any queens are in the same row or diagonal
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            # Found a valid solution, append the board to the solutions list
            solutions.append(list(enumerate(board)))
        else:
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(board, row+1)

    # Start the backtrack search with an empty board and an empty solutions list
    board = [-1] * n
    solutions = []
    backtrack(board, 0)

    # Print the solutions
    for solution in solutions:
        print(solution)

# Parse command line arguments and call nqueens
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
nqueens(n)
