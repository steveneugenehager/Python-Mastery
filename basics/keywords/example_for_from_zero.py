# for example with a number controlling the loop's execution.  

# By starting at zero, we can use the counter to index into sequence.
i = 0
iteration_count = 5

# By starting at zero, we can use the "<" operator instead of the "<=" operator.
print("Example for loop with range") 
for i in range(iteration_count):
    print('index is ' , i , '; iteration count is ' , i+1 )
print()

print("Using for loop with list...")
my_list=list('abcdef')
print('my_list =' , my_list)
for item in my_list:
    print("Item is" , item)
print()

print("Using for loop with string...")
my_string='rstuvwxyz'
print('my_string =' , my_string)
for index in range(len(my_string)):
    print("index is" , index , "; Item is" , my_string[index])
print()