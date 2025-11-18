import random
import math
import sys
from enum import Enum 


MAX_NBR = 128 # a "constant" used in many places herein.

class Boundary(Enum):
    LOW = 0
    HIGH = 1

def main():
    # Generate a random integer
    the_number = int(math.ceil( random.random() * MAX_NBR ))

    # This range is used to guide the user's guesses. It is seeded here.
    possible_range = [1,MAX_NBR]
    # A stack of distances for the user's guesses from the number to be guessed.
    # Used to provide you are cold|warm feedback for their guesses.
    distances = [MAX_NBR]

    #Loop until the user guesses correctly.
    while True:
        #Handle invalid data like a string or empty string. Convert strings that look like floats to int.
        try:
            #Get the user's guess
            guess=int(float(input(f"Enter your guess, 1-{MAX_NBR}: ")))
        #Tell the user if bad data is encountered. Skip to the next iteration.
        except ValueError as e:
            print("Invalid input.  Must be a number.")
            continue
        # Give the user feedback if the guess is known to be a very bad one, based on prior guesses or just the rules of the game.
        if guess < possible_range[Boundary.LOW.value] or guess > possible_range[Boundary.HIGH.value]:
            print("That is a bad choice. You know the range is:" , possible_range)
        else:
            # Determine if the guess is wrong and update the possible range to provide a new hint to the user.
            if guess < the_number:
                print("\tToo low. " , end="")
                possible_range[Boundary.LOW.value] = guess + 1
            elif guess > the_number:
                print("\tToo High. " , end="")
                possible_range[Boundary.HIGH.value] = guess - 1
            # If the guess is correct, the game is over.
            else:
                print("You guessed the number," , the_number)
                break
            # The game continues
            # Give the user some extra information and motivation.
            distances.append(abs(the_number-guess))
            if distances[-1] <= distances[-2]:
                print("You are getting warmer...")
            else:
                print("You are getting colder...")

            # Provide the user new guidance and a hint for their next guess.
            best_next_guess = (possible_range[Boundary.HIGH.value] - possible_range[Boundary.LOW.value]) // 2 \
                                + possible_range[Boundary.LOW.value]
            print('\tHINT: ' , f"{possible_range=}" , f"{best_next_guess=}")


if __name__ == '__main__':
    main()