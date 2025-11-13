# for example with a number controlling the loop's execution.  

# By starting at zero, we can use the counter to index into sequence.
i = 0
iteration_count = 5

# By starting at zero, we can use the "<" operator instead of the "<=" operator.
print("Example for loop with range") 
for i in range(iteration_count):
    print('index is ' , i , '; iteration count is ' , i+1 )
