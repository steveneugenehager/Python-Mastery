class MyBreakLoop(Exception):
    pass


def loops_with_complete_breakout(x,y,magic_number):
    found_flag = False
    for i in range(x):
        for j in range(y):
            if ( i+j == magic_number ):
                found_flag = True
                print(f"BREAKOUT commencing: Encountered a sum of {magic_number} , {i=} , {j=}" , end="")
                break
        if found_flag:
            print("\tBREAKOUT complete.")
            break
    else:
        print(f"No BreakOut, {i=} , {j=}")
    

def main():
    loops_with_complete_breakout(10,10,42)
    loops_with_complete_breakout(10,10,-1)
    loops_with_complete_breakout(30,30,42)

main()