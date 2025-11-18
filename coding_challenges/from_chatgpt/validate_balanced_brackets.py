# validate_balanced_brackets.py
#
# 2025-11-15 Steve Hager
#
# A coding challenge given by ChatGPT.
#
#  
#Givens:
 
#Assumptions
# 1.   
# Key concepts or learning:
#   Using the dictionary data structure to associate the open brackets with their closed brackets.



def main():
    input_str = [ "something{word[hello()caller()]}" , 
                  "some(error()thing[])abc" ,
                  "some()thing[]" ,
                  "something{word[hello(])}"  ,
                  "hello(" ,
                  "hell(o" ,
                  "something[" ,
                  "somethin[g" ,
                  "some(thing[]" ,
                  "some()error(thing[]" ,
                  "some(error()thing[]" ,
                  ] 
    for str in input_str:
        print(str , '->' , validate_balanced_brackets(str))

def validate_balanced_brackets(string):
    """
    Verifies the three types of brackets are balanced.

    Returns True or False
    Empty String not interesting.
    Didn't bother with handling None input.  
    """
    
    # Associate the open symbol for each of the three types of closing bracket.
    bracket_mapping = { '}':'{' , ']':'[' , ')':'(' }
    # Empty the stack initially
    stack = []
    
    # Iterate through the string
    for ch in string:
        #If an open flavor of bracket, put it on the stack
        if ch in '{[(':
            stack.append(ch)
        #If a closed flavor of bracket, verify it matches the last open bracket seen. If not, the brackets are unbalanced.
        elif ch in '}])':
            if not stack or stack.pop() != bracket_mapping[ch]: 
                return False
    # The solution I compared mine too didn't cover the possibility that a bracket was opened and never closed. This statement addresses that case.
    if stack:
        return False 
    
    return True

if __name__ == '__main__':
    main()