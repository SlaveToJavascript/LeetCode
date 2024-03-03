# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description
# MEDIUM
# Tags: slidingwindowlc, leetcode75lc, lc75lc, #1456

# GIVEN:
    # string, s
    # integer, k

# TASK:
    # Return the max no. of vowel letters in any substring of s with length k

# EXAMPLES:
    # Input: s = "abciiidef", k = 3
    # Output: 3
    # Explanation: The substring "iii" contains 3 vowel letters.

    # Input: s = "aeiou", k = 2
    # Output: 2
    # Explanation: Any substring of length 2 contains 2 vowels.

    # Input: s = "leetcode", k = 3
    # Output: 2
    # Explanation: "lee", "eet" and "ode" contain 2 vowels.

###########################################################################################################

# ✅ ALGORITHM 1: SLIDING WINDOW
# we don't need to get the no. of vowels in every single subarray to get the max no.
# to get the no. of vowels in a subarray, just find out the no. of of vowels in its previous subarray, then -1 if the 1st letter of the previous subarray is a vowel and +1 if the last char in the new subarray is a vowel
    # i.e. only check the first and last elements

# TIME COMPLEXITY: O(n)
    # We apply 1 iteration over s
    # At each step in the iteration, we check if the newly added character and the removed character are in vowels, which takes constant time
    # To sum up, the time complexity is O(n)
# SPACE COMPLEXITY: O(1)

def maxVowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    window_vowels_count = sum(char in vowels for char in s[:k]) # no. of vowels in 1st window
    max_count = window_vowels_count
    l = 0 # 1st element of 1st window
    
    for r in range(k, len(s)): # start iterating from 2nd window onwards
        window_vowels_count -= (1 if s[l] in vowels else 0) # s[l] is the char removed from current window
        window_vowels_count += (1 if s[r] in vowels else 0) # s[r] is the new char in current window
        max_count = max(max_count, window_vowels_count)
        l += 1

    return max_count