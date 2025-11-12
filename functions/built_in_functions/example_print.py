# Examples of the print() built-in function.
# 2025-11-12 v1. Created.

example_list = [ 'to' , 'be' , 'or' , 'not' , 'to' , 'be' ,]
a,b,c,d,e,f = example_list
example_dict = dict(key="1",value="to")
example_tuple = ( 'to' , 'be' , 'or' , 'not' , 'to' , 'be' ,)

print('INFO|Print of a list: ' , example_list)
print('INFO|Print of multiple singleton items: ' , a,b,c,d,e,f)
print('INFO|Print of multiple singleton items without separator: ' , a,b,c,d,e,f,sep="")
print('INFO|Print of multiple singleton items with different separator:')
print(a,b,c,d,e,f,sep="|")

print() # prints a blank line
print('INFO|Print of a dictionary' , example_dict)

print() # prints a blank line
print('INFO|Print of a tuple' , example_tuple)
#