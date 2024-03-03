# 2390. Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/
# MEDIUM
# Tags: stacklc, leetcode75lc, lc75lc, #2390

# GIVEN:
    # a string s, which contains stars "*"

# TASK:
    # for each star, remove the closest non-star character to its left, as well as remove the star itself
    # Return the string after all stars have been removed

# EXAMPLES:
    # Input: s = "leet**cod*e"
    # Output: "lecoe"
    # Explanation: Performing the removals from left to right:
    # - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
    # - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
    # - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
    # There are no more stars, so we return "lecoe".

    # Input: s = "erase*****"
    # Output: ""
    # Explanation: The entire string is removed, so we return an empty string.

###########################################################################################################

# ✅ ALGORITHM: STACK
# Iterate through s, adding each non-star character to a stack
# if the char is a *, pop the last char from stack (if any)
# return stack as a string

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def removeStars(s):
    stack = []

    for i in range(len(s)):
        if s[i] == "*":
            if stack: # if stack is not empty,
                stack.pop()
        else:
            stack.append(s[i])
    
    return ''.join(stack)