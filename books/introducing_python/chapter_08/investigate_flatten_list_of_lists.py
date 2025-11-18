def flatten(in_list):
    flattened_list = []
    for i in in_list:
        if isinstance(i,list) or isinstance(i,tuple):
            flattened_list.extend(flatten(i))
        else:
            flattened_list.append(i) 
    return flattened_list

def main():

    lists_to_test = []
    lists_to_test.append( 'abc')  # Unsure how this should be handled. It is not really interesting behavior as an "edge case".
    lists_to_test.append( '' )
    lists_to_test.append( [ ] )
    lists_to_test.append( [ 1 , 2 , 3] )
    lists_to_test.append( [ 1 , 2 , (3,)] )
    lists_to_test.append( [ 1 , 2 , [3, 4 ] ] )
    lists_to_test.append( [ 1 , 2 , [3, 4 , [5,6,7]] ] )
    lists_to_test.append( [ 1 , 2 , [3, 4 , [5,6,7]] , 8] )
    lists_to_test.append( [ 1 , 2 , [3, 4 , (5,6,7)] , 8] )
    for l in lists_to_test:
        print(flatten(l))
    

main()