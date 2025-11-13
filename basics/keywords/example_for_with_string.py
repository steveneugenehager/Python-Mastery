# for example with a string controlling the loop's execution.  

print("Using for loop with string...")
my_string='rstuvwxyz'
len_of_my_string = len(my_string)
print("length  of my_string =" , len_of_my_string)
print('my_string =' , my_string)
for index in range(len_of_my_string):
    print("index is" , index , "; my_string [", index,  "] =" , my_string[index])
