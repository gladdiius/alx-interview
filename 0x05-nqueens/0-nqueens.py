#!/usr/bin/python3
""" n-queens """
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    """
    Utility function to solve the N-Queens problem recursively.
    """
    # If all queens are placed, add the solution to the list of solutions
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0  # Backtrack if placement leads to failure
    return res


def solve_n_queens(n):
    """
    Main function to solve the N-Queens problem.
    """
    # Check if N is a valid integer
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard as an empty grid
    board = [[0] * n for _ in range(n)]

    # List to store all solutions
    solutions = []

    # Solve the N-Queens problem
    solve_n_queens_util(board, 0, n, solutions)

    # Print all solutions in reverse order
    for sol in reversed(solutions):
        print(sol)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Solve the N-Queens problem with the given N
    solve_n_queens(sys.argv[1])
