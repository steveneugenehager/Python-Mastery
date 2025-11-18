my_list = []
for i in range(1,5+1):
    my_list.append(i)
byte_var = bytes(my_list)
print(byte_var)
print('length = ' , len(byte_var))


my_list = []
for i in range(1,15+1):
    my_list.append(i)
bytearray_var = bytearray(my_list)
print(bytearray_var)
print('length = ' , len(bytearray_var))

print()
byte_var , bytearray_var = bytearray_var,byte_var
print('byte_var =' , byte_var)
print('bytearray_var = ' , bytearray_var)


print()
try:
    byte_var = byte_var + byte_var
except BufferError as be:
    print("BufferError " + str(be))
bytearray_var+=bytearray_var
print('byte_var =' , byte_var)
print('bytearray_var = ' , bytearray_var)
