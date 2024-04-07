# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string
# MEDIUM
# Tags: stringlc, greedylc, #678

# GIVEN:
    # a string s containing only three types of characters: '(', ')' and '*'

# TASK:
    # return true if s is valid
    # The following rules define a valid string:
        # Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        # Any right parenthesis ')' must have a corresponding left parenthesis '('.
        # Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        # '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string ""

# EXAMPLES:
# Input: s = "()"
# Output: true

# Input: s = "(*)"
# Output: true

# Input: s = "(*))"
# Output: true

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# since we have 3 possible values for "*", we need to consider the min. and max. balance of ( and ) in the string, factoring for the various possible values of *
    # "balance" = no. of "(" - no. of ")"
    # GOAL: balance = 0 -> this means there are equal no. of "(" and ")"
# TODO: keep track of the min_balance and max_balance of the string
    # when we encounter a "(", both min_balance+1 and max_balance+1
    # when we encounter a ")", both min_balance-1 and max_balance-1
    # when we encounter a "*", min_balance-1 and max_balance+1
        # min_balance-1 : we consider "*" as a ")" -> we are reducing the no. of "("
        # max_balance+1 : we consider "*" as a "(" -> we are increasing the no. of "("
    # NOTE: if min_balance < 0, we reset it to 0 since we only consider the valid range of possible values for balance (i.e. at least 1 of the * cannot be considered as "(")
    # NOTE: if max_balance < 0, it means we have extra ")"s which is not balanced by "("s or "*"s
        # once max_balance < 0, it means there are already too many extra ")"s and we can no longer balance them with "(" or "*" -> the whole string will be invalid no matter what the remaining characters are
            # -> return False

# TIME COMPLEXITY: O(n)
    # n = len(s)
# SPACE COMPLEXITY: O(1)

def checkValidString(s):
    min_balance = max_balance = 0

    for char in s:
        if char == "(":
            min_balance += 1
            max_balance += 1
        elif char == ")":
            min_balance -= 1
            max_balance -= 1
        else: # char = "*"
            min_balance -= 1
            max_balance += 1
        
        if max_balance < 0: # if max_balance < 0, it means we have extra ")"s which is not balanced by "("s or "*"s
            return False
        
        if min_balance < 0: # since we previously did min_balance-1 if char = "*", if min_balance < 0, we only consider the valid range of possible values for balance (i.e. at least 1 of the * cannot be considered as "(")
            min_balance = 0 # reset to 0
    
    return min_balance == 0 # if we reached this line, it means max_balance >= 0 which is valid
        # if min_balance > 0, it means we have extra "("s which is not balanced by ")"s or "*"s