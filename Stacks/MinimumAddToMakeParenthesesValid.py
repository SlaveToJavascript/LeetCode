# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# MEDIUM
# Tags: stacklc, #921

# A parentheses string is valid if and only if:
    # It is the empty string,
    # It can be written as AB (A concatenated with B), where A and B are valid strings, or
    # It can be written as (A), where A is a valid string.

# GIVEN:
    # a parentheses string, s

# TASK:
    # In one move, you can insert a parenthesis at any position of the string
        # For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))"
    # Return the minimum number of moves required to make s valid

# EXAMPLES:
    # Input: s = "())"
    # Output: 1

    # Input: s = "((("
    # Output: 3

###########################################################################################################

# ✅ ALGORITHM 1: STACK (my solution)
# use a stack to keep track of the opening brackets, and for each ")" encountered, pop from the stack
# if a closing bracket is encountered and the stack is empty, increment the result counter (it is an invalid closing bracket)
# if there's anything remaining in the stack after iterating the string, increment the result counter by the length of the stack (these are invalid opening brackets)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def minAddToMakeValid(s):
    result = 0
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        else: # if char = ")"
            if stack and stack[-1] == "(": # if stack is not empty and top of stack is (
                stack.pop()
            else:
                result += 1
    
    return result + len(stack)

#==========================================================================================================

# ✅ ALGORITHM 2: Open Bracket Counter
# Create 2 variables: openBrackets (to track unmatched open brackets) and minAddsRequired both initialized to 0
# Iterate string s:
    # If the current character is an open bracket (, increment the openBrackets counter, as it is unmatched for now
    # If the current character is a close bracket ):
        # Check if there are any unmatched open brackets (openBrackets > 0).
        # If an unmatched open bracket exists, decrement openBrackets to indicate that a matching pair has been formed.
        # If no unmatched open brackets are available, increment minAddsRequired as we need to add an open bracket to make this close bracket valid.
# The total number of additions required will be the sum of minAddsRequired and any remaining unmatched open brackets (openBrackets). Return this value as the result.

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def minAddToMakeValid(s):
    open_brackets = 0
    min_adds_required = 0

    for char in s:
        if char == "(":
            open_brackets += 1
        else:
            if open_brackets > 0:
                open_brackets -= 1
            else:
                min_adds_required += 1
    
    return min_adds_required + open_brackets