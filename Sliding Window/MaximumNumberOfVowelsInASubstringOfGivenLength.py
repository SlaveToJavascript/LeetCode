# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description
# MEDIUM
# Tags: slidingwindowlc, #1456

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
    v = {'a', 'e', 'i', 'o', 'u'}
    v_count = len([char for char in s[:k] if char in v])
    max_count = v_count

    for i in range(k, len(s)):
        v_count += int(s[i] in v) # s[i] is the char to be included in new sliding window
        v_count -= int(s[i - k] in v) # s[i-k] is the char to remove from existing sliding window
        max_count = max(max_count, v_count)

    return max_count