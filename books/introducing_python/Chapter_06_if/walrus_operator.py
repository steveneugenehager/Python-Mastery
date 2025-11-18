import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

if ( diff := x-y ) > 0:
    print('x < y' , f"{diff=}")
elif diff < 0:
    print('x > y' , f"{diff=}")
else:
    print('x = y' , f"{diff=}")
    