# Key points:
#   Nested function: A function defined inside another function.
#   Scope: The inner function is only accessible within the outer function.
#   Use cases: Encapsulating helper functions, creating closures, or organizing code.
#Summary:
#   Function nesting means defining or calling functions within other functions to organize 
#   code better, encapsulate helper tasks, or create closures in Python.
# 


# Alternatively, you can chain functions together which is also like nesting them.

def main():
# Get input from the user and convert it to a int using nested functions
    n = int(input("Enter a number: "))
    print("the input:" , n , 'is of type' , type(n))
 
    print()
    print("INFO: execute the nesting or localization of functions...")
    print(outer_function(n))


def outer_function(n):
    """
    Simple demonstration to show a local function defined in a function.
    """
    def local_function(x):
        """
        This function is local to an outer function.
        """
        return x * -1
    
    return(local_function(n) * 10)


if __name__ == "__main__":
    main()
