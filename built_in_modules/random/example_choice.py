# If you import specific functions, you don't have to qualify the function calls.iterations
 
from random import choice

results = [ 'Heads' , 'Tails' ]

iterations = 10

for i in range(iterations):
    print('Trial #' , i+1 , ' results in ' , choice(results) , sep='')
