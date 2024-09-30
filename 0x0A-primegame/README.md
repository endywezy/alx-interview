Prime Game - README

Project Overview
Maria and Ben are engaged in a game involving prime numbers. The game starts with a set of consecutive integers from 1 up to a given value n. On each player's turn, they select a prime number from the set and remove that prime number and all of its multiples from the set. The player who cannot make a valid move loses the game.

This project implements a function to determine the winner of each game after multiple rounds, assuming both Maria and Ben play optimally and Maria always goes first.

Game Rules
The game is played in rounds, where each round has a different set size n.
Players alternate picking prime numbers from the set.
When a player picks a prime number, they must remove that prime and all of its multiples from the set.
The player who cannot make a move (because there are no primes left in the set) loses the game.

Function Prototype
python
Copy code
def isWinner(x, nums)

x: The number of rounds.
nums: An array of integers where each value represents the set size n for that round.

Return Value:
The function returns the name of the player ("Maria" or "Ben") who won the most rounds.
If the winner cannot be determined (both players won the same number of rounds), the function returns None.

Constraints:
x and each n in nums will not be larger than 10,000.
You cannot import any external packages for this task.

Example
python
Copy code
x = 3
nums = [4, 5, 1]

Round 1: n = 4
Maria picks 2, removing 2 and 4. Remaining set: {1, 3}
Ben picks 3, removing 3. Remaining set: {1}
Ben wins because there are no prime numbers left for Maria to choose.

Round 2: n = 5
Maria picks 2, removing 2 and 4. Remaining set: {1, 3, 5}
Ben picks 3, removing 3. Remaining set: {1, 5}
Maria picks 5, removing 5. Remaining set: {1}
Maria wins because there are no prime numbers left for Ben to choose.

Round 3: n = 1
Ben wins because there are no prime numbers for Maria to choose from.

Result:
Ben wins 2 rounds, Maria wins 1 round.
The function returns "Ben".

Usage
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/alx-interview.git

Navigate to the project directory:
bash
Copy code
cd alx-interview/0x0A-primegame

Run the 0-prime_game.py script with the required inputs.

Author

Endurance Ossai - GitHub