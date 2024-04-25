#!/usr/bin/python3
"""define min opratinos"""


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
    operations = 0
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    return operations