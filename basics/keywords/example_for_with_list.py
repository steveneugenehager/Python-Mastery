# for example with a list controlling the loop's execution.  

print("Using for loop with list...")
my_list=list('abcdef')
print('my_list =' , my_list)
i=0
for item in my_list:
    print("Offset is " , i , " ; Item #", i+1 ," is my_list[ " , i ," ] = " , item, sep="")
    i+=1
