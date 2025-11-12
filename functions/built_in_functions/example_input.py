# Simple example(s) of the built-in "input()" function.
# The output of input() is always a str.
# Numbers returned as strings would have to be cast before using arithmetic on them.
# Casts would need to be tested for conversion/type errors.
# 
# 2025-11-12 v2. Added display of type(input()). Test the script to show numbers entered are strings.
 

user_input = input("Enter a string: ")
print("INFO|The user entered the string '" , user_input , "'.",sep="")
print("INFO|The data type of the return value of the input() function is:" , type(user_input))