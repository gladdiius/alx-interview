#!/usr/bin/python3
"""0-makingchange"""


#!/usr/bin/python3
"""0-makingchange"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Parameters:
    coins (list): A list of the values of the coins in possession.
    total (int): The total amount to be met.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0 or less, returns 0.
         If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)
    
    num_coins = 0
    for coin in coins:
        if total >= coin:
            count = total // coin
            num_coins += count
            total -= count * coin
    
    if total != 0:
        return -1  # If total cannot be met by any combination of coins
    return num_coins