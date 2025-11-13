# If you import specific functions, you don't have to qualify the function calls.iterations
# Notes:
#   random.shuffle() shuffles the list in place.
#   It returns None to emphasize that it does not produce a new list.
 
from random import shuffle

cards = list('A23456789TJQK')
print("Original List:" , cards)
iterations = 10

for i in range(iterations):
    shuffle(cards)
    print('Trial #' , i+1 , ' results in ' , cards  , sep='')
