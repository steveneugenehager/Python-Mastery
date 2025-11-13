#Simple example of sys.exit usage 

import sys

# Define a main to show the most important logic or functionality of your program.

def main(): 
    # Push less interesting code into a function so the most interesting content is left herein.
    check_arguments()

    # This is the raison detre of the program.  Processing input and making name tags.
    for arg in sys.argv[1:]:
        # leave print here so the function doesn't have side effects. It returns a value and makes it testable.
        name_tag = create_name_tag( arg )
        if name_tag:
            print( name_tag )


def create_name_tag( name ):
    """
    This function accepts a string and creates the text for a new name tag.
    First name is expected first with last Name (and middle names) following, optionally.
    Empty input strings are dropped with a WARNING.
    """
    if name.strip() != "":
        return("Hello, my name is " + name.strip().title() + '.')
    else:
        print("Warning.  Name was an empty string or solely whitespace and ignored.")
        return None


def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Usage Error: Too Few Arguments.")


if __name__ == '__main__':
    main()