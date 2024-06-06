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
    
    # Initialize the dp array with infinity values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: zero coins to make total of 0
    
    # Populate the dp array
    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    
    # Check if we found a solution or not
    return dp[total] if dp[total] != float('inf') else -1