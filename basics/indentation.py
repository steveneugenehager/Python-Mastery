# Indentation in Python is used to define the structure and scope of code blocks. It indicates which 
# statements belong together, such as inside functions, loops, conditionals, classes, and other
#  control structures.
#
# Why is indentation important?
#   In Python, indentation is mandatory and used instead of braces {} or other delimiters found in many languages.
#   Proper indentation defines code blocks and ensures correct program execution.
# Summary:
#   Indentation is used in Python to organize code into blocks for functions, loops, conditionals, classes, 
#   and more, making code readable and syntactically correct.

# Common uses of indentation in Python:

# Defining functions:
def main():
    print(my_function('mlb'))

# Within loops:
    for _ in range(3):
        print(_)

    person=Person('John')
    print(person , person.f_name)

def my_function(str):
    return(str.upper())

# Within classes:
class Person:
    def __init__(self, f_name):
        self.f_name = f_name

# Inside control statements:
if __name__ == '__main__':
    main()
