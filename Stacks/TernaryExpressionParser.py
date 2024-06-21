# 439. Ternary Expression Parser
# https://leetcode.com/problems/ternary-expression-parser/
# MEDIUM
# Tags: stacklc, premiumlc, #439

# GIVEN:
    # a string, expression, representing arbitrarily nested ternary expressions

# TASK:
    # evaluate the expression, and return the result of it
    # NOTE:
        # You can always assume that the given expression is valid and only contains digits, '?', ':', 'T', and 'F' where 'T' is true and 'F' is false. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9])
        # The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F'

# EXAMPLES:
    # Input: expression = "T?2:3"
    # Output: "2"
    # Explanation: If true, then result is 2; otherwise result is 3.

    # Input: expression = "F?1:T?4:5"
    # Output: "4"
    # Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
    # "(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
    # or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"

    # Input: expression = "T?T?F:5:3"
    # Output: "F"
    # Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
    # "(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
    # "(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"

###########################################################################################################

# ✅ ALGORITHM 1A: STACK (my solution)
# using a while loop, iterate the string "expression" from back to front
# create a stack
# 3 CASES:
    # 1. if char = ":", do not add char to stack, continue to next iteration
    # 2. if char = "T" or "F" or digits, add char to stack, continue to next iteration
    # 3. if char = "?", check if the character on the left of this char "?" is "T" or "F"
        # if character on the left of "?" is "T", then the answer to this ternary expression is the last item in the stack
        # if character on the right of "?" is "F", then the answer to this ternary expression is the 2nd last item in the stack
# return the only remaining element left in stack, which would be the overall ternary expression

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def parseTernary(expression):
    stack = []
    i = len(expression)-1
    
    while i >= 0:
        char = expression[i]
        if char == "?":
            i -= 1 # i is now the character on the left of "?" char
            if expression[i] == "T":
                answer = stack.pop()
                stack.pop()
            else: # expression[i] == "F"
                stack.pop()
                answer = stack.pop()
            stack.append(answer)
        elif char != ":":
            stack.append(char)
        
        i -= 1
    
    return stack[0]

#==========================================================================================================

# ✅✅ ALGORITHM 1B: STACK (my solution but optimized by ChatGPT)
# for the above solution, within the "if expression[i] == "T"" block, instead of doing popping and appending operations so many times, we can simplify it by popping both the "true expression" (i.e. last element in stack) and "false expression" (i.e. 2nd last element in stack) and append the respective expression to stack based on whether the character in front of "?" is "T" or "F"

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def parseTernary(expression):
    stack = []
    i = len(expression) - 1

    while i >= 0:
        char = expression[i]
        if char == '?':
            true_expression = stack.pop()
            stack.pop()  # pop the ":" character
            false_expression = stack.pop()
            i -= 1
            stack.append(true_expression if expression[i] == 'T' else false_expression)
        elif char != ':':
            stack.append(char)
        
        i -= 1

    return stack[0]