# Illustrate while and break

i = 1
while True:
    print('iteration #' , i)
    i += 1      # The while condition would never be false; Something in the code has to lead to a break
    if i > 5:
        #The break statement does not directly affect an if block by itself.
        #Instead, break is used to exit a loop (such as for or while) prematurely.
        break
    else:
        continue   # This is redundant here.  