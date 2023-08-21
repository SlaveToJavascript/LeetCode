# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
# MEDIUM
# Tags: stacklc, #1249

# GIVEN:
    # a string, s, of '(' , ')' and lowercase English characters

# TASK:
    # remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string
    # Formally, a parentheses string is valid if and only if:
        # It is the empty string, contains only lowercase characters, or
        # It can be written as AB (A concatenated with B), where A and B are valid strings, or
        # It can be written as (A), where A is a valid string

# EXAMPLES:
    # Input: s = "lee(t(c)o)de)"
    # Output: "lee(t(c)o)de"
    # Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

    # Input: s = "a)b(c)d"
    # Output: "ab(c)d"

    # Input: s = "))(("
    # Output: ""
    # Explanation: An empty string is also valid.

###########################################################################################################

# ✅ ALGORITHM: STACK
# Iterate s
# For each char in s, if char is (, push its index to stack
    # if char is ), pop its index from stack if stack is not empty
        # if stack is empty, exclude this ) from result
    # for every other char, include it in result
# if stack is not empty, it means there are additional ('s which should not be in result
# for each ( in stack, remove it from result string

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def minRemoveToMakeValid(s):
    result = list(s) # result is an array of chars of s
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i) # if char is (, push its index to stack
        elif s[i] == ")":
            if stack:
                stack.pop() # if char is ), pop from stack (as we found a matching pair of brackets)
            else: # if stack is empty, we cannot pop from stack -> this ) char is extra and should be removed
                result[i] = "" # remove char from result array
    
    for i in stack:
        result[i] = "" # remove any additional ('s which do not have closing brackets

    return ''.join(result)