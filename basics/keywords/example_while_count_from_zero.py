# while example with a number controlling the loop's execution.  "for" works better in such a case.
# while best used for flags or multiple conditions.

# By starting at zero, we can use the counter to index into sequence.
i = 0
iteration_count = 10

# By starting at zero, we can use the "<" operator instead of the "<=" operator.
while i < iteration_count:
    print('index is ' , i , '; iteration count is ' , end="" ) #Skip the new line at end so i can first be updated.
    i += 1
    print(i)