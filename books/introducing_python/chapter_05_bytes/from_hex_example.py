hex_string='FF 01 61 62 63 64 65 66'
byte_var = bytes.fromhex(hex_string)
print(byte_var == b'\xff\x01abcdef')
print()
print(byte_var == b'\xff\x01\x61\x62\x63\x64\x65\x66')
print()
print(byte_var)
print(byte_var.hex())

for i in range(len(byte_var)):
    print( i , byte_var[i] , chr(byte_var[i]))