def main():

    #build a list of decimal numbers in groups of 16
    decimal_list_of_lists = []
    for i in range(16):
        decimal_inner_list = []
        for j in range(16):
            decimal_inner_list.append(16 * i + j)
        decimal_list_of_lists.append(decimal_inner_list)
        
    #convert the individual decimal numbers into a byte (binary) and combine them.
    for list in decimal_list_of_lists:
        print(bytes(list))


if __name__ == '__main__':
    main()
