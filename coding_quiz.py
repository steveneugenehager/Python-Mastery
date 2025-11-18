#Problem:
#   Given a string, find the first character that does not 
#   repeat anywhere in the string. If all characters repeat, return None.

def main():
    strings = ( 'a' , 'bb' , 'test' , 'abc' * 2 , 'ssswisswwisX123' , "")
    for string in strings:
        print('Testing:' , string , '->' , first_character_nonrepetition(string))


def first_character_nonrepetition(input):
    for ch in input:
        if input.count(ch) == 1:
            return ch
    return None

if __name__ == '__main__':
    main()  