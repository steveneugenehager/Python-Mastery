#  Method chaining is a programming technique where multiple methods are called on an
#  object in a single statement, one after the other. This is possible when each method returns
#  the object itself (self) or another object that has further methods.
 
my_string = "  Hello, World!  "
print("Original:" , my_string)
print("Stripped:" , my_string.strip())
print("Stripped & Uppered:" , my_string.strip().upper())
print("Stripped, Uppered, and Replaced:" , my_string.strip().upper().replace("!", "?"))


#Each method returns a new string (since strings are immutable in Python), allowing
#  subsequent methods to be called on the result.

#Benefits:
#  Concise and readable code.