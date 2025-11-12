# Demonstrate how to specify a parameter's default value.

def main():
    print("INFO|Demonstrate a call to hello() with no argument:")
    print(hello())
    print()

    username = input("Name?").title()
    print("INFO|Demonstrate a call to hello() with an argument:")
    print(hello(username))
    print()

    print("INFO|Demonstrate a call to hello() with argument 'None':")
    print(hello(None))
    print()


def hello(name="World"):
    # if None is passed explicitly, the default value is not used.
    # None would cause a TypeError exception in the + operation. 
    if name:
        return 'Hello, ' + str(name) + '!'
    else:   
        return None

if __name__ == '__main__':
    main()