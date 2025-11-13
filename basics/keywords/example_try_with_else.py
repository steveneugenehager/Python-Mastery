# A simple example of try with else

items_to_test = [ -1, 0 , 42 , 1e30 , 9.99 , 'cat' , None , 1+2j , [0] , (1,2) , {} ]

for n in items_to_test:
    print('Original =' , n ,  "; " , end="")
    try:
        result = int(n)
    except ValueError as ve:
        print('WARNING - ValueError =' , ve)
    except TypeError as te:
        print('WARNING - TypeError =' , te)
    else:
        print('result = ' , result)
