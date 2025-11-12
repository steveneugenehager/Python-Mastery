# Purpose understand if the object id of the argument and parameter are the same or not within a function call.
#  Show the different behavior of immutable (e.g., str) and mutable (e.g., list) data types.

# Moral to the story - when you pass a mutable object to a function, that function can in fact change the mutable object
#  without returning it for assignment.  

def main():
    print("Investigating passing immutable data...")
    str = 'abcdefghijklmnopqrstuvwxyz'

    print( 'ID of argument:\t\t\t' , id(str))
    my_str_function(str)

    print("\nInvestigating passing mutable data...")
    list = ['a' , 'b' , 'c']

    print('list =' , list)
    print( 'ID of argument:\t\t\t' , id(list))
    my_list_function(list)
    print('list =' ,list)
    
def my_str_function(parameter):
    print("\tIn str function...")
    print('\tID of parameter:\t' , id(parameter))
    parameter += '?'
    print('\tID of changed parameter:' , id(parameter))

def my_list_function(parameter):
    print("\tIn list function...")
    print('\tID of parameter:\t' , id(parameter))
    parameter.append('?')
    print('\tID of changed parameter:' , id(parameter))

if __name__ == '__main__':
    main()