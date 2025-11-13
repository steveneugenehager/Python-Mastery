# Example of looping until the user input is valid and the operation succeeds.
# No else is strictly necessary as the return is a "break" out of the function.
# The "return" is not executed if the functions (int, float) fail.
# The except keeps us in the loop, looking for valid input.

def main():
    print( 'The integer is' , get_int() )


def get_int():
    while True:
        try:
            return int(float(input("Enter a number: ")))
        except ValueError as ve:
            print("ERROR -" , ve)


if __name__ == '__main__':
    main()