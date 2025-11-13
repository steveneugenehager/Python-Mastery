# Simple program demonstrating TypeError where the operand was not numeric and the operation failed.

test_items = [ -1, 0, 1, 3.14234723847 , 5+4j , 1e99 , 'cat' , None, True, False, [1,2] ]
for n in test_items:
    print('value = ' , n , end="")
    try:
        square = n ** 2
        print(" ; square = " , square)
    except TypeError:
        print(" ; WARNING, TypeError occurred but was handled...")
