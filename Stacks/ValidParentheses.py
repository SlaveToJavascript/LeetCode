# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# EASY
# Tags: stacklc, #20

# GIVEN:
    # a string, s, containing just the characters '(', ')', '{', '}', '[' and ']'

# TASK:
    # Determine if the input string is valid
    # An input string is valid if:
        # Open brackets must be closed by the same type of brackets.
        # Open brackets must be closed in the correct order.

# EXAMPLES:
    # Input: s = "()"
    # Output: true

    # Input: s = "()[]{}"
    # Output: true

    # Input: s = "(]"
    # Output: false

    # Input: s = "([)]"
    # Output: false

    # Input: s = "{[]}"
    # Output: true

###########################################################################################################

# ✅ ALGORITHM: STACK
# create a hashmap of opening brackets mapped to their corresponding closing brackets
# initialize a stack
# iterate the string
    # if the character is an opening bracket, push it to the stack
    # if the character is a closing bracket
        # if the stack is empty, return False
        # if the stack's top is not the corresponding opening bracket, return False
        # otherwise, pop from the stack
# if the stack is empty, return True; otherwise, return False

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

from collections import deque

def isValid(s):
    pairs = {"(" : ")", "[": "]", "{": "}"}
    stack = deque()
    for char in s:
        if char in pairs: # if char is opening bracket
            stack.append(char)
        else: # if char is closing bracket
            if stack and char == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0