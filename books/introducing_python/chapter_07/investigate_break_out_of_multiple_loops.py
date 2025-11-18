class MyBreakLoop(Exception):
    pass


def loops_with_complete_breakout(x,y,magic_number):
    try:
        for i in range(x):
            for j in range(y):
                if i+j == magic_number:
                    raise MyBreakLoop
        else:
            print(f"No BreakOut, {i=} , {j=}")
    except MyBreakLoop:
        print(f"BREAKOUT: Encountered a sum of {magic_number} , {i=} , {j=}")


def main():
    loops_with_complete_breakout(10,10,42)
    loops_with_complete_breakout(10,10,-1)
    loops_with_complete_breakout(30,30,42)

main()