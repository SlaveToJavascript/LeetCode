# 2116. Check if a Parentheses String Can Be Valid
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/
# MEDIUM
# Tags: stringlc, greedylc, #2116

# GIVEN:
    # a parentheses string, s, of length n
    # a string locked, also of length n
    # locked is a binary string consisting only of '0's and '1's
        # For each index i of locked,
            # If locked[i] is '1', you cannot change s[i]
            # But if locked[i] is '0', you can change s[i] to either '(' or ')'

# TASK:
    # Return true if you can make s a valid parentheses string
    # Otherwise, return false

# EXAMPLES:
    # Input: s = "))()))", locked = "010100"
    # Output: true
    # Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
    # We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

    # Input: s = "()()", locked = "0000"
    # Output: true
    # Explanation: We do not need to make any changes because s is already valid.

    # Input: s = ")", locked = "0"
    # Output: false
    # Explanation: locked permits us to change s[0]. 
    # Changing s[0] to either '(' or ')' will not make s valid.

###########################################################################################################

# ✅ ALGORITHM: TWO PASSES + BALANCED PARENTHESES
# MAIN APPROACH:
    # greedily check balance left-to-right balance, and then right-to-left
        # left-to-right: ensures we don't have orphan ")" parantheses
        # right-to-left: ensures we don't have orphan "(" parantheses
    # ensure that at any point in the string, the no. of open and close parenthesis can be balanced, considering the flexibility of unlocked parenthesis
# STEPS:
    # Forward pass:
        # check if string is valid from left to right
        # increments open_balance for an open parenthesis or UNLOCKED parenthesis (which can be an opening parenthesis)
        # decrements open_balance for a close LOCKED parenthesis
        # if open_balance is -ve, it means there are too many close locked parenthesis without matching openings
    # Backward pass:
        # similar to Forward pass but checks from right to left, ensuring there aren't too many locked opening parentheses without matches
# NOTE: at no point in forward/backward pass should open/close balance be -ve, as this would immediately make the string invalid

def canBeValid(s, locked):
    if len(s) % 2 != 0: # if s is odd-lengthed, it can't possibly be balanced
        return False
    
    open_balance = 0 # no. of "("
    close_balance = 0 # no. of ")"

    for i in range(len(s)):
        # FORWARD PASS
        if s[i] == "(" or locked[i] == "0":
            open_balance += 1
        else: # if s[i] is a close locked parenthesis
            open_balance -= 1
        if open_balance < 0: # too many close locked parentheses
            return False
    
        # BACKWARD PASS
        if s[len(s)-1-i] == ")" or locked[len(s)-1-i] == "0": # NOTE: len(s)-1-i corresponds to the backward index of i
            close_balance += 1
        else: # if s[len(s)-1-i] is an open locked parenthesis
            close_balance -= 1
        if close_balance < 0: # too many locked opening parenthesis
            return False