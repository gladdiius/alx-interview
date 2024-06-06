#!/usr/bin/python3
"""0-makingchange"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): List of coin values in possession.
    total (int): The target total amount to reach.

    Returns:
    int: Fewest number of coins needed to meet the total.
         Return 0 if total is 0 or less.
         Return -1 if total cannot be met by any number of coins.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1