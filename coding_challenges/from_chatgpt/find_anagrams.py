# find_anagrams.py
#
# 2025-11-15 Steve Hager
#
# A coding challenge given by ChatGPT.
#
#  
#Givens:
 
#Assumptions
# 1.   
# Key concepts or learning:
#    

import random

def main():
    given_anagram = 'abc'
    # build a long test string to see if they work too.
    random_string=''
    for i in range(100):
        random_string += random.choice(['a','b','c','X'])


    strings_to_test = [ "cbaebabacd" , random_string ,'bac' * 3 , 'cab' * 2 , 'abc' , "" ] 
    for str in strings_to_test:
        print(str , '->' , find_anagrams(str , given_anagram))


def find_anagrams(string,anagram):
    """
    """
    window_size = len(anagram)
    # Initialize the list to be built and then returned.
    results = []
    sorted_anagram = ''.join(sorted(anagram)) # In the challenge, the given anagram was already sorted.
    # Step through the trying to extract all the 3"window_size"-character snippets within.
    for index in range(0, len(string)-window_size+1):
        # Compare the snippet to the anagram, both of which have been sorted so the list equality can be determined.
        if sorted_anagram == ''.join(sorted(string[index:index+window_size])):
            # If matched, add the snippet's offset to the results.
            results.append(index)

    return results


if __name__ == '__main__':
    main()