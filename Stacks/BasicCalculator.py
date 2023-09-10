# https://leetcode.com/problems/basic-calculator/description/
# HARD
# Tags: stacklc, #224

# GIVEN:
    # a string s representing a valid expression
    # NOTE: s consists of digits, '+', '-', '(', ')', and ' '

# TASK:
    # implement a basic calculator to evaluate it, and return the result of the evaluation

# EXAMPLES:
    # Input: s = "1 + 1"
    # Output: 2

    # Input: s = " 2-1 + 2 "
    # Output: 3

    # Input: s = "(1+(4+5+2)-3)+(6+8)"
    # Output: 23

###########################################################################################################

# ✅ ALGORITHM: STACK
# sign = 1 represents + (plus), sign = -1 represents - (subtraction)
    # this is so that we can multiply sign by result to achieve intended effect (e.g. -3 = -1 * 3 where sign = -1 and result = 3)
# for each char in s:
    # if char is a digit,
        # add char to current number
    # else if char is + or - (i.e. if char is an operator),
        # 1st, we add the number on the left of the operator (curr) to the result
        # 2nd, we update sign with current operator (if +, sign = 1; if -, sign = -1)
        # 3rd, reset curr to 0 so that it can next move to and hold the number on the right of current operator
            # e.g. s = 123 - 465, and we are currently at the + character
                # 1st, add 123 to result
                # 2nd, update sign to -1 since current operator is -
                # 3rd, set curr = 0
    # else if char is (,
        # 1st, push the result of the equation on the left of the ( into the stack, so that after the equation in the bracket is evaluated, we can pop from stack and compute the left equation result with the bracket result
        # 2nd, push the sign into the stack
            # this sign would be the operator that comes right before the (
            # we need this sign so that if the equation is e.g. -(4+5+6), we can do -1 * bracket result, i.e. -1 * (4+5+6)
        # 3rd, reset result
            # since result has been pushed into stack, we reset result so now result can be used to compute the equation in bracket
        # 4th, reset sign
            # since sign has been pushed into stack, we reset sign back to 1 (+), i.e. its default value
        # e.g. s = 3 - (4+5+2), and we are currently at the ( character
            # now, result = 3 -> push into stack
            # now, sign = -1 (since sign before "(" is minus) -> push into stack
            # reset result = 0 so result can then be used to calculate 4+5+2 (i.e. bracket result)
            # reset sign = 1 (+) so that 4 uses + sign by default
    # else if char is ),
        # 1st, add the last number before ) to result
            # now, result = result of only numbers in bracket
        # 2nd, pop from stack -> this is the sign before the corresponding opening bracket (
            # since result is now bracket result, and this sign is the sign before (, multiply sign with result
        # 3rd, pop from stack again -> this is the result of the equation on the left of the bracket
            # add popped value to result
        # 4th, reset curr to 0 so that it can next move to and evaluate the equation on the right of )
            # e.g. s = 7 - (4+5-2), and we are currently at the ) character
                # 1st, add -2 to result -> result now = bracket result
                # 2nd, sign -1 is popped from stack -> multiply result (bracket result) with -1
                # 3rd, 7 is popped from stack -> this is the result of the equation before opening bracket "(" -> add this 7 to result
                # 4th, reset curr = 0
# process the last number/s (left in curr), if any, by adding them to result
# return result

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def calculate(s):
    curr = 0
    result = 0 # return value
    stack = []
    sign = 1 # 1 for plus (+), -1 for minus (-)

    for char in s:
        if char.isdigit():
            curr = curr * 10 + int(char) # add char digit to curr number
        elif char == "+" or char == "-":
            result += curr * sign # add no. on the left of this operator to result
                # NOTE: sign here is still the sign of curr, which is the no. on the left of this operator
            sign = -1 if char == "-" else 1 # update sign with this operator
            curr = 0 # reset curr so it can then hold the number on the right of this operator
        elif char == "(":
            stack.append(result) # push existing result (before the "(" to stack)
            stack.append(sign) # push the sign before the "(" to stack
            result = 0 # reset result, so it will then be used to track the result of the bracket
            sign = 1 # reset sign
        elif char == ")":
            result += sign * curr # add the last number before ")" to result
            result *= stack.pop() # the sign before the opening bracket (-1 or 1) is popped -> since result is now bracket result, this popped sign is for the bracket result
            result += stack.pop() # this popped value is the result of the equation on the left of the bracket -> add it to bracket result
            curr = 0 # reset curr
    
    return result + sign * curr # process whatever's left in curr (if any), i.e. the last number/s in s