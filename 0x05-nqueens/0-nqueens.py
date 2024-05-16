#!/usr/bin/python3
"""
This module solves the N-Queens problem, determining all possible arrangements of N queens on an NxN chessboard without attacking each other.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at position (row, col) on the board.

    Parameters:
    - board: The current state of the chessboard.
    - row: The row to check for placing the queen.
    - col: The column to check for placing the queen.
    - n: The size of the board.

    Returns:
    - True if it's safe to place a queen at the given position; otherwise, False.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    """
    Utility function to solve the N-Queens problem recursively.

    Parameters:
    - board: Current state of the chessboard.
    - col: Current column being processed.
    - n: Size of the board.
    - solutions: List to store valid solutions.

    Modifies the board to find all valid solutions.

    Returns:
    - True when a solution is found.
    """
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0
    return res

def solve_n_queens(n):
    """
    Main function to solve the N-Queens problem.

    Parameters:
    - n: Size of the board.

    Validates input, creates the initial board, and calls the utility function to find solutions.
    Prints out all valid solutions found.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens_util(board, 0, n, solutions)

    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_n_queens(sys.argv[1])
