# Demonstrate that an empty string passed on the python command line is not in sys.argv. 

import sys

print( sys.argv )

#When I tested this on Windows command line with:
#PS> python.exe investigate_empty_string_on_command_line.py "" '' x " " ' '  
# 
# The empty strings are not seen in argv....
# ['investigate_empty_string_on_command_line.py', 'x', ' ', ' ']