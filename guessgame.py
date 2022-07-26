# Guessing Number Game
#
# Three Levels: 
#   Easy (1 - 100)
#   Medium (1 - 1k)
#   Hard (1 - 100k)

from random import randint

running = True # game is running
winner = False # winner

# global variable
number = 0

# welcome message
print("Welcome to Guessing Number Game")

# while loop to keep the game running
while (running):
    # prompt the user for the highest possible number to pick from
    num = int(input("Enter the highest number possible: "))
    number = randint(1, num)

    # while the guess is not correct
    while (not winner):
        guess = int(input("Enter your guess: "))
        
        if guess < number: # guess is too low
            print("Too Low")
        elif guess > num: # guess doesn't fit the range
            print("What?")
        elif guess > number: # guess is too high
            print("Too High")
        else:
            print("Nice") # nice
            winner = True # break the inner loop
    
    # prompt if want to play again
    resp = input("Play Again (Y) or (N): ")
    if resp.lower() == 'y': # single letter
        winner = False
    elif resp.lower() == 'yes': # the word yes
        winner = False
    else: # any text will close the application
        running = False