
x = [1.994 , 2.995 , float(3) , float('4') , 1.6666666e3 , 1e25 , 2.123456789e99 ]
print("Examples of floats:")
for _ in x:
    print(_ , '; Rounded ->' ,round(_ , 2))

# Interesting behavior - the round function doesn't work on large or small floating point numbers