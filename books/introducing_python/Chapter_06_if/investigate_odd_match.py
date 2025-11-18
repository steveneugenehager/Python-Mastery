subject = [3,5]
match subject:
    case x , 4:
        print('1st')
    case x, 5:
        print('2nd')
        print(f"{x=}")
        print(f"{y=}") # I think there was a typo / bug in the book's example. Referencing "y" made no sense there. It causes a name error here.
    case _:
        print('catchall')