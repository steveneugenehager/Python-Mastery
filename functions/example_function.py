# A function is defined using the def keyword.
# A function definition includes the parameters (zero or more) the function accepts.
# When a function is called from the callee the parameters are referred to as arguments.
# Functions must be defined before used.
# It is recommended to include a main() function first holding the most important flow of
#   the solution that is then followed by the other subsidiary functions.
# It is necessary to invoke main().
# It is a best practice to invoke main() conditionally to support the cases where the
#   python script is tested standalone and also from an import statement in another script.
#
# 2025-11-12 v1.  Created. To Do:  How should None be handled?  This occurs when the argument is invalid.
# 2025-11-12 v2.  Added test cases for edge cases - None and Booleans. A list of numbers.
#
# Purpose: Demonstrate a simple function definition and execute it with a few arguments of differing types.

import inspect


def main():
    print("INFO|Running " , __name__)
    # test integers, decimals, floats, imaginary.
    # test invalid data.
    numbers = [ 0 , 9 , 3.14 , 3e20, -7 , 3+7j , 'cat' , None , True , False , [1,2] ]
    for n in numbers:
        print(n , ' squared is ', square(n))


# it is typical to name the parameters in a meaningful way.
# n here just means any old number.
def square(n):
    print("INFO|Running " , inspect.currentframe().f_code.co_name)
    try:
        return (n ** 2)
    except TypeError:
        print("ERROR|Invalid data type.  Singleton Numbers only.")


# This should always be used. This construct allows the flow of the program to be laid out
# top to bottom.
if __name__ == "__main__":
    main()


