# Integers are known as "int" in Python

# There is no limit to the size of an integer
print("INFO|Generate some progressively larger numbers...")
next_big_number = 2 ** 25
for _ in range(10):
    print("Iteration", _+1 , "; # of digits:" , len(str(next_big_number)) , ":\n" , next_big_number ,  "is of type" , type(next_big_number))
    next_big_number = next_big_number ** 2