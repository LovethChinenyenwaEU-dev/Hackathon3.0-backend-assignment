# exercise 9.13
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        # Returns a random integer between 1 and the total number of sides
        return randint(1, self.sides)

# Function to handle rolling any die 10 times cleanly
def test_die(sides):
    die = Die(sides)
    results = []
    for _ in range(10):
        results.append(die.roll_die())
    print(f"Rolling a {sides}-sided die 10 times: {results}")

# 1. Make a 6-sided die and roll it 10 times
test_die(6)

# 2. Make a 10-sided die and roll it 10 times
test_die(10)

# 3. Make a 20-sided die and roll it 10 times
test_die(20)


# exercise 9.14
import random

# 1. Pool containing a series of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 2. Randomly select 4 items without duplication using random.sample()
winning_ticket = random.sample(lottery_pool, 4)

# 3. Print the message
print("--- LOTTERY DRAW ---")
print(f"Any ticket matching these 4 numbers/letters wins a prize: {winning_ticket}")

# exercise 9.15
import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# My specific chosen ticket
my_ticket = [3, 7, 'A', 'E']

# Track the number of loops required to win
attempts = 0
won = False

print("Simulating lottery draws... Please wait...")

while not won:
    attempts += 1
    # Sample 4 random items from the pool
    current_draw = random.sample(lottery_pool, 4)
    
    # Check if our ticket elements match the current draw exactly
    # We sort both to ensure order doesn't stop a match if the items are identical
    if sorted(map(str, my_ticket)) == sorted(map(str, current_draw)):
        won = True

print(f"\nVictory!")
print(f"Your ticket: {my_ticket}")
print(f"Winning draw: {current_draw}")
print(f"The loop had to run {attempts:,} times to give you a winning ticket!")


