"""
    Welcome to *Guessing the number with Le Chat*
    A simple program to guess a number from 0 to 20
    
    What does it do?:

    **It iterate until you guess the correct value**
    **Only accepts an integer between 0 and 20**

"""
from numpy import random

print("**Welcome to: Guess the number**\n**Guess the number between 0 and 20**")

#random number generator between 0 and 20
random_number = random.randint(20)

#initializing value
value = ""

#The loop will break when the value(INTEGER) is equal to the random number

while value != random_number:
    
    # This try catches if the user_input is an integer. If not, then it goes into the
    # exception
    try:
        user_input = input("Please enter a number between 0 and 20:\n")
        value = int(user_input)

        if value <= 20 and value >= 0:
    
            if value < random_number:
                print("Value is too low!")
    
            if value > random_number:
                print("Value is too high!")

            if value == random_number:
                print("CORRECT!")
                break
    
        else:
            print("Please enter a number within the range")

    except ValueError:
        try:
            value = float(user_input)
            print("Please enter a valid INTEGER. Not a Float number.")
        except ValueError:
            print("Please enter a valid INTEGER. Do not type NONSENSE")

