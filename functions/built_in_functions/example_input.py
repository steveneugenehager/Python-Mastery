# Simple example(s) of the built-in "input()" function.
# The output of input() is always a str.
# Numbers returned as strings would have to be cast before using arithmetic on them.
# Casts would need to be tested for conversion/type errors. 

user_input = input("Enter a string: ")
print("INFO|The user entered the string '" , user_input , "'.",sep="")