# Example of looping until the user input is valid and the operation succeeds.
# The else indicates a successful 'try' block.
# The except keeps us in the loop, looking for valid input.

while True:
    try:
        n = int(float(input("Enter a number: ")))
    except ValueError as ve:
        print("ERROR -" , ve)
    else:
        break
print("The integer is" , n )