# https://leetcode.com/problems/basic-calculator-ii/description/
# MEDIUM
# Tags: stacklc, #227

# GIVEN:
    # a string s which represents a mathematical expression

# TASK:
    # evaluate this expression and return its value
    # NOTE: The integer division should truncate toward zero

# EXAMPLES:
    # Input: s = "3+2*2"
    # Output: 7

    # Input: s = " 3/2 "
    # Output: 1

    # Input: s = " 3+5 / 2 "
    # Output: 5

#############################################################################################################

# ✅ ALGORITHM: STACK
# Iterate through string s
# For each number and each + and - operation in s, we automatically push them into stack
    # e.g. s = 21 - 5 + 1: push 21 into stack, push -5 into stack, push 1 into stack
# For each * and / operation in s, we pop from stack and perform the operation on current number, then push result back into stack
# after finishing iteration, add up all numbers in stack and return result

# TIME COMPLEXITY: O(n)
    # n = length of s
# SPACE COMPLEXITY: O(n)
    # for stack

def calculate(s):
    i = 0 # for the iteration; tracks current char in s
    stack = []
    curr_num = 0 # current no. encountered in s
    op = "+" # initialize default operation as +

    while i < len(s):
        if s[i].isdigit(): # if current char is a no., 
            while i < len(s) and s[i].isdigit(): # keep iterating to get all digits of the no.
                curr_num = curr_num * 10 + int(s[i])
                i += 1
            i -= 1 # we need to -1 from i since i would be pointing at the next non-no. char after while-loop finishes
            
            if op == "-":
                stack.append(-curr_num)
            elif op == "+":
                stack.append(curr_num)
            elif op == "*":
                stack.append(stack.pop() * curr_num) # pop last no. from stack, multiply by current no., then push it back
            elif op == "/":
                # NOTE: if we do -3//2, we get -2 since it rounds down, but we want -1 instead, so we first need to check if the popped no. is -ve
                prev = stack.pop()
                if prev < 0:
                    stack.append(-(abs(prev) // curr_num)) # if popped no. is -ve, we do -(3//2) instead
                else:
                    stack.append(prev // curr_num)
            curr_num = 0 # reset current no. to 0 after pushing it to stack
        
        elif s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
            op = s[i] # change the operator
        
        i += 1 # go to the next char in s
    
    result = 0 # return value
    for num in stack:
        result += num # add up all no.s in stack
    
    return result