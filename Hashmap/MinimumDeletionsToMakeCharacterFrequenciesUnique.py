# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
# MEDIUM
# Tags: hashmaplc, #1647

# GIVEN:
    # string s
    # string s is called good if there are no 2 different characters in s that have the same frequency
        # The frequency of a character in a string is the number of times it appears in the string
            # e.g. in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1

# TASK:
    # return the minimum number of characters you need to delete to make s good

# EXAMPLES:
    # Input: s = "aab"
    # Output: 0
    # Explanation: s is already good.

    # Input: s = "aaabbbcc"
    # Output: 2
    # Explanation: You can delete two 'b's resulting in the good string "aaabcc".
    # Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

    # Input: s = "ceabaacb"
    # Output: 2
    # Explanation: You can delete both 'c's resulting in the good string "eabaab".
    # Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

###########################################################################################################

# ✅ ALGORITHM 1: HASHMAP + SET
# Create hashmap of each char in s and frequency of that char in s
# create a set that will track unique frequencies of chars in hashmap
# iterate hashmap
    # if any char has a frequency that is already in the unique frequencies hashmap, it means this frequency is repeated
        # keep deleting 1 instance of this char until char's new frequency is no longer in unique frequencies set OR frequency of this char = 0
            # track no. of deletions made
    # add new frequency of char to unique frequencies set
# return no. of deletions

# TIME COMPLEXITY: O(n)
    # Counter(s) takes O(n) time
    # for loop takes O(n) time in the worst case (when frequency of each char = 1)
# SPACE COMPLEXITY: O(n)

from collections import Counter

def minDeletions(s):
    hm = Counter(s) # creates hashmap of each unique char in s and its frequency in s
    deletions = 0 # return value
    unique_freqs = set() # tracks frequencies encountered as we iterate through hashmap

    for char in hm: # iterate hashmap
        while hm[char] in unique_freqs and hm[char] > 0: # if frequency of current char is already in set, we need to delete instance(s) of it
            hm[char] -= 1 # delete 1 instance of char
            deletions += 1
        unique_freqs.add(hm[char]) # add updated (unique) frequency of current char to set
    
    return deletions