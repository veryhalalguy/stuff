# Dice Roll Simulator

# User inputs X sides
# Comp randomly picks a number between 1 to x.

from random import randint

# conduct a try/catch to make sure we get an integer value
try:
    sides = int(input("Enter the amount of sides the dice has (Default: 6): "))
except ValueError:
    sides = 6

# if a negative number is given default to 6
if sides <= 0:
    value = randint(1, 6)
else: # pick a random value from 1 to sides
    value = randint(1, sides)

# print the value
print("The Dice rolls: %d" % value)