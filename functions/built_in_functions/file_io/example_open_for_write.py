strings = [ 'abc' , 'def' , 'xyz' ]

with open("tmp_data.txt" , "a") as file_handle:
    for str in sorted(strings):
        file_handle.write(str + "\n")

