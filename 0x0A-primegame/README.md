# Prime Game

This project implements the Prime Game where Maria and Ben take turns picking prime numbers from a set of consecutive integers. The rules of the game are as follows:

- Maria always goes first.
- Players take turns picking a prime number and removing that number and all of its multiples from the set.
- The player who cannot make a move loses the game.

## Function

### isWinner

The `isWinner` function determines the winner of the game after a specified number of rounds.

#### Parameters

- `x` (int): The number of rounds.
- `nums` (list of int): A list containing the `n` values for each round, where `n` is the maximum number in the set for that round.

#### Returns

- `str` or `None`: The name of the player that won the most rounds ("Maria" or "Ben"), or `None` if there is a tie.

## Usage

```python
#!/usr/bin/python3
from prime_game import isWinner

print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
