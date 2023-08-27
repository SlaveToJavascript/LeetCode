# https://leetcode.com/problems/generate-parentheses/description/
# MEDIUM
# Tags: backtracklc, #22

# GIVEN:
    # n pairs of parentheses

# TASK:
    # write a function to generate all combinations of well-formed parentheses

# EXAMPLES:
    # Input: n = 3
    # Output: ["((()))","(()())","(())()","()(())","()()()"]

    # Input: n = 1
    # Output: ["()"]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# RULES:
    # for a valid combination, no. of "(" = no. of ")" = n
        # "(" can only be added if no. of "(" in combination < n
    # ")" can only be added if no. of ")" < no. of "("

# TIME COMPLEXITY: O(4^n / sqrt(n))
    # Each valid sequence has at most n steps during the backtracking procedure.
    # At every step, we can append open or close to the current sequence.
    # Therefore, the total number of steps during the backtracking procedure is 2n
    # However, not every sequence is valid.
    # For example, for n = 6, we have (((((()))))), where the first 5 "(" are valid, but the last "(" is not valid.
    # Thus, we have to subtract the number of invalid steps from the total number of steps to get the number of valid steps.
    # The number of invalid steps is the Catalan number Cn.
    # Thus, the time complexity is O(2n - Cn) = O(4^n / sqrt(n)).
# SPACE COMPLEXITY: O(n)
    # for the recursive call stack
    # each recursive call either adds a left parenthesis or a right parenthesis, and the total number of parentheses is 2n -> at most O(n) levels of recursion will be created

def generateParenthesis(n):
    result = [] # return value

    def backtrack(open, close, comb): # open = no. of "(", close = number of ")", comb = array of current combination of parantheses
        if open == close == n:
            result.append(''.join(comb))
            return
        
        if open < n: # can add more "(" to comb
            comb.append("(")
            backtrack(open+1, close, comb) # added 1 "(" -> open+1
            comb.pop()

        if close < n: # can add more ")" to comb
            comb.append(")")
            backtrack(open, close+1, comb)
            comb.pop()
    
    backtrack(0, 0, [])
    return result