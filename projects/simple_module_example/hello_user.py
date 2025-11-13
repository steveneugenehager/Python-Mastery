from greetings import hello 
import sys
print("I am in " + __name__)

if len(sys.argv) != 2:
    sys.exit("ERROR - incorrect usage")

hello(sys.argv[1])
