# Simple program demonstrating the ZeroDivisionError exception

numerator = [ -1, 0, 1, 2]
denominator = [ -1, 0, 1, 2 ]

for m in numerator:
    for n in denominator:
        print('numerator =' , m ,'; denominator =' , n , end="")
        try:
            result = m / n 
            print(' ; result =' , result)
        except ZeroDivisionError:
            print(" ; WARNING: ZeroDivisionError: division by zero; was caught and handled without crashing the program.")