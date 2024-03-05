# 1750. Minimum Length of String After Deleting Similar Ends
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
# MEDIUM
# Tags: twopointerslc, #1750

# GIVEN:
    # a string s consisting only of characters 'a', 'b', and 'c'

# TASK:
    # apply the following algorithm on the string any no. of times:
        # 1. Pick a substring from the FRONT of the string s where all the characters in the substring are equal
        # 2. Pick a non-empty substring from the BACK of the string s where all the characters in this substring are equal
        # 3. both substrings should not intersect at any index.
        # 4. The characters from both substrings must be the same
        # 5. Delete both substrings from the string s
    # Return the minimum length of s after performing the above operation any number of times (possibly zero times)

# EXAMPLES:
    # Input: s = "ca"
    # Output: 2
    # Explanation: You can't remove any characters, so the string stays as is.

    # Input: s = "cabaabac"
    # Output: 0
    # Explanation: An optimal sequence of operations is:
    # - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
    # - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
    # - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
    # - Take prefix = "a" and suffix = "a" and remove them, s = "".

    # Input: s = "aabccabba"
    # Output: 3
    # Explanation: An optimal sequence of operations is:
    # - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
    # - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# l and r pointers, pointing to 1st and last chars of string s respectively
# while l and r do not cross each other, if they are equal, move them both inwards by 1 each
    # now, l and r should both keep looking for consecutive chars that are equal to the original l and r values, and move pointers inwards again until the consecutive chars are no longer equal to the original l and r values
# if the chars at l and r are not equal, break out of while loop (since we can't remove anymore chars from string s)

# TIME COMPLEXITY = O(n)
    # while loop
# SPACE COMPLEXITY = O(1)

def minimumLength(s):
    l, r = 0, len(s)-1
    while l < r: # *** see NOTE
        if s[l] == s[r]:
            l += 1
            r -= 1
            while l <= r and s[l] == s[l-1]:
                l += 1
            while l <= r and s[r] == s[r+1]:
                r -= 1
        else:
            break
    
    return r-l+1

# *** NOTE: this condition cannot be l <= r as the loop will attempt to execute one last time when l = r, leading to incorrect l += 1 and r -= 1