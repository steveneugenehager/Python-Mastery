def while_loop(in_list):
    index = 0
    while index < len(in_list):
        print('\tnumber =' ,in_list[index])
        if in_list[index] % 2 == 0:
            print("BREAKING out...even number seen!!!")
            break
        index += 1
    else:
        print("loop completed without BREAKING out...only odd numbers seen!!!")


def main():
    odd_numbers_only = [ 1 , 3 , 5 ]
    numbers = [ 1 , 2 , 3 , 5 ]

    for l in [odd_numbers_only , numbers]:
        while_loop(l)


if __name__ == '__main__':
    main()