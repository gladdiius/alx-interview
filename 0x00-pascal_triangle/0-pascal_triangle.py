#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Args:
    - n: An integer representing the number of rows to generate.
    
    Returns:
    - A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Start the new row with 1

        # Calculate the values for the new row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)  # Add the new row to the triangle
    
    return triangle

def print_triangle(triangle):
    """
    Print the Pascal's Triangle.
    
    Args:
    - triangle: A list of lists representing Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)