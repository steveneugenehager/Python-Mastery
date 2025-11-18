# 2025-11-14 Examples of opening a file for read and reading its contents. 

def main():
    input_file = "tmp_data.txt"
    read_by_line(input_file)
    read_with_readlines(input_file)


def read_by_line(input_file):
    # The with construct gives a scope to the file operations as the file is automatically closed after the block completes.
    print("INFO|In function 'read_by_line'.")
    with open( input_file , "r" ) as file_handle: 
        # You can simply iterate over the file handle, getting a str split on '\n'
        for line in file_handle:
            print( line.rstrip() )


def read_with_readlines(input_file):
    # The with construct gives a scope to the file operations as the file is automatically closed after the block completes.
    print("\n\nINFO|In function 'read_with_readlines'.")
    with open( input_file , "r" ) as file_handle:
        # readlines() reads the entire file and returns a list split on '\n' and including the '\n's
        lines = file_handle.readlines()

    for line in sorted( lines ):
        print( line.rstrip() )
    # If the sort wasn't needed you could just read a line at a time in the with block with a "for line in lines:"


if __name__ == '__main__':
    main()
