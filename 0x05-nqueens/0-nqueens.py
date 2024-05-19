#!/usr/bin/python3
""" n-queens """
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    
    Args:
        board (list): The chessboard configuration.
        row (int): The row to check.
        col (int): The column to check.
    
    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col, solutions):
    """
    Utilize backtracking to find all solutions.
    
    Args:
        board (list): The chessboard configuration.
        col (int): The current column.
        solutions (list): List to store all solutions found.
    
    Returns:
        bool: True if a solution was found, False otherwise.
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, solutions) or res
            board[i][col] = 0
    return res

def solve_nqueens(n):
    """
    Solve the N Queens problem and return all solutions.
    
    Args:
        n (int): The number of queens to place.
    
    Returns:
        list: List of all solutions found.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions

def main():
    """
    Main function to handle input and output.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(n)
    solutions.reverse()
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
