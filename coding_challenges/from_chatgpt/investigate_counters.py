
def main():

# Example:
    string = "cbaebabacd"
    p = "abc"
    print(find_anagrams(string, p))
# Output: [0, 6]


def find_anagrams(string, p):
    from collections import Counter
    
    result = []
    anagram_count = Counter(p)
    window_size = len(p)
    string_count = Counter(string[:window_size - 1])  # Initialize with first window - 1
    print(string_count)
    
    for i in range(len(string) - window_size + 1):
        # Include the new character in the window
        string_count[string[i + window_size - 1]] = string_count.get(string[i + window_size - 1], 0) + 1
        print('\t' , string_count)
        
        # If counts match, it is an anagram starting index
        if string_count == anagram_count:
            result.append(i)
        
        # Remove the leftmost character of the window for next iteration
        string_count[string[i]] -= 1
        if string_count[string[i]] == 0:
            del string_count[string[i]]
    
    return result

#Explanation:
#
##Use Counter to track character frequencies.
#Slide a window of size len(p) across s.
#Compare the window's character count with p's character count.
#Collect starting indices where they match.
#Let me know if you'd like a detailed step-by-step explanation!

main()