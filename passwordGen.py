#####################################
#        Password Generator         #
#####################################

import random
import string
import os

from progress.bar import Bar

print('Password Generator!')

# store global variables
length = 0
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = ""
passNum = 1

# list where we keep passwords
passwords = []

# check if the input length is valid
lengthSatisfied = False

# for loop to ask for a valid length of a password
while not lengthSatisfied:        
    try:
        length = int(input('Enter the length of password: '))
    except ValueError: # when the user inputs anything not a number
        print("Invalid Input")
    else:
        if length < 5:
            print("Password must be more than 5 characters.")
        elif length > 24:
            print("Password must be less than 24 characters.")
        else:
            lengthSatisfied = True
    
# user wants uppercase letters
enableUpper = input("Enter 'y' or 'n' to enable uppercase letters (Default: Yes): ")

if enableUpper.upper() == 'N':    
    upper = ""

# user wants numbers
enableNum = input("Enter 'y' or 'n' to enable numbers (Default: Yes): ")

if enableNum.upper() == 'N':    
    num = ""
    
# user wants symbols
enableSym = input("Enter 'y' or 'n' to enable symbols (Default: No) : ")

# special case symbol list is empty by default 
if enableSym.upper() == 'Y':    
    symbols = string.punctuation

# check if the user input is valid, if not default to 1
try:    
    passNum = int(input("Enter the amount of passwords you would like to generate (Default: 1): "))
except ValueError:
    print("")

# combine the texts
all = lower + num + upper + symbols

# create a progress bar
bar = Bar('Generating', max=passNum, fill='#', suffix='%(percent)d%%')
for x in range(0, passNum):
    # create a randomly generated string from the all the characters available of length
    temp = random.sample(all, int(length))
    password = "".join(temp) # concatenate the string

    # progress bar
    bar.next()
    
    # add to the list
    passwords.append(password)
bar.finish()

# if the number of passwords the user wants to generate is less than 2, then we're done
if (passNum < 2):
    print("Generated Password: " + passwords.pop())
else: # else ask the user if they would like to save it to a file
    saveToFile = input("Enter 'y' or 'n' to save to a file (Default: No): ")

    # if so we save to the file
    if (saveToFile.upper() == 'Y'):
        bar = Bar('Saving', max=passNum, fill='#', suffix='%(percent)d%%')
        with open('passwords.txt', 'w') as f:
            for passw in passwords:
                f.write("%s\n" % passw)
                bar.next()
            bar.finish()
            print('Created password.txt with updated passwords.')

# system pause
os.system("PAUSE")