# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# MEDIUM
# Tags: stacklc, #150

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation (where operands come before operators)
    # e.g. "3 + 4" is "3 4 +" in RPN
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
    # The valid operators are '+', '-', '*', and '/'.
    # Each operand may be an integer or another expression.
    # The division between two integers always truncates toward zero.
    # There will not be any division by zero.

# EXAMPLES:
    # Input: tokens = ["2","1","+","3","*"]
    # Output: 9
    # Explanation: ((2 + 1) * 3) = 9

    # Input: tokens = ["4","13","5","/","+"]
    # Output: 6
    # Explanation: (4 + (13 / 5)) = 6

    # Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # Output: 22
    # Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    # = ((10 * (6 / (12 * -11))) + 17) + 5
    # = ((10 * (6 / -132)) + 17) + 5
    # = ((10 * 0) + 17) + 5
    # = (0 + 17) + 5
    # = 17 + 5
    # = 22

###########################################################################################################

# ✅ ALGORITHM: STACK
# Create a stack
# Iterate through tokens
# if token is a string integer, push it to stack
# if token is an operator (+, -, *, /), pop 2 integers from stack and calculate their result
# push result into stack
# after tokens are all processed, stack should have 1 result left which is the overall result of the entire arithmetic expression

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def evalRPN(tokens):
    stack = []
    op = {"+", "-", "/", "*"}

    for t in tokens:
        if t not in op: # if t is a string integer,
            stack.append(int(t)) # push it to stack
        else: # if t is operator
            right = stack.pop()
            left = stack.pop()

            if t == "+":
                result = left + right
            elif t == "-":
                result = left - right
            elif t == "/":
                result = int(left/right) # since division truncates to 0, use int(result) to achieve this
            else:
                result = left * right
        
            stack.append(result) # push result back into stack
    
    return stack[0] # after tokens are all processed, stack should have 1 result left which is the overall result of the entire arithmetic expression 