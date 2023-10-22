4.4

"""
Write a game where the computer draws a random integer between 1 and 10.
The user tries to guess the number until they guess the right number.
After each guess the program prints out a text: Too high, Too low or Correct.
Notice that the computer must not change the number between guesses.
"""

import random
number = random.randint(1,10)

while True:
    guess = int(input("Give your guess integer: "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct")
        break

