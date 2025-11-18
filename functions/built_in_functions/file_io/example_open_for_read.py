with open("tmp_data.txt" , "r") as file_handle:
    lines = file_handle.readlines()

for line in lines:
        print( line.rstrip() ) 

    
