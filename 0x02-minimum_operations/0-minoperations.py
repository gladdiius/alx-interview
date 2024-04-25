#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations needed to obtain 'n' H characters 
    in the text file using the operations 'Copy All' and 'Paste'.
    
    Args:
    - n (int): The desired number of H characters.
    
    Returns:
    - int: Minimum number of operations to achieve 'n' H characters.
           Returns 0 if 'n' is impossible to achieve.
    """
    
    # Initialize operations count
    operations = 0
    
    # Start with the smallest divisor
    divisor = 2
    
    # Continue until 'n' is reduced to 1
    while n > 1:
        # Check if 'n' is divisible by the current divisor
        if n % divisor == 0:
            # Reduce 'n' by the divisor
            n //= divisor
            # Increase operations by the divisor (Copy operation)
            operations += divisor
        else:
            # If not divisible, try the next divisor
            divisor += 1
    
    return operations
