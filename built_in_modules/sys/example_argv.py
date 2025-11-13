#Simple example of sys.argv usage - positional arguments for the python script.

import sys

arg_count = len(sys.argv)
for offset in range(1, arg_count):
    print('sys.argv[' , offset, '] =' , sys.argv[offset])