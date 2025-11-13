# Simple program demonstrating the ZeroDivisionError exception

numerator = [ -1, 0, 1, 2]
denominator = [ -1, 0, 1, 2 ]

for m in numerator:
    for n in denominator:
        print('numerator =' , m ,'; denominator =' , n , end="")
        try:
            result = m / n 
            print(' ; result =' , result)
        except ZeroDivisionError as zde:
            print(" ; WARNING: ZeroDivisionError:" , zde ) 

#2025-11-12 v2. Added capture and display of full error message. 