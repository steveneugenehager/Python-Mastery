# match example with 
#  - multiple strings to match for a case.
#  - the "_" catchall

i=1
for letter in list('abcdefghijklmnopqrstuvwxyz'):
    print(i , letter, 'is a ' , end="")
    match letter:
        case 'a'|'e'|'i'|'o'|'u':
            print("vowel")
        case _:
            print("consonant")
    i+=1