#!/usr/bin/python3
"""
Prime Game Module

This module contains the function isWinner which determines the winner
of the prime game played between Maria and Ben.

Maria always goes first, and both players play optimally. The function
returns the name of the player who won the most rounds or None if there
is a tie.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game played between Maria and Ben.
    
    Parameters:
    x (int): Number of rounds.
    nums (list of int): List of n values for each round.
    
    Returns:
    str or None: Name of the player that won the most rounds, or None if it's a tie.
    """
    if x <= 0 or not nums:
        return None
    
    # Precompute primes up to the maximum number in nums using the Sieve of Eratosthenes
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    
    # Count number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    
    # Initialize wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # Number of primes in the set {1, 2, ..., n}
        primes_in_game = prime_count[n]
        
        if primes_in_game % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
