# https://leetcode.com/problems/combinations/
# MEDIUM
# backtracklc, #77

# GIVEN:
    # 2 integers, n and k

# TASK:
    # return all possible combinations of k numbers chosen from the range [1, n]

# EXAMPLES:
    # Input: n = 4, k = 2
    # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    # Explanation: There are 4 choose 2 = 6 total combinations.
    # Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

    # Input: n = 1, k = 1
    # Output: [[1]]
    # Explanation: There is 1 choose 1 = 1 total combination.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE BACKTRACKING

# TIME COMPLEXITY: O(nk)
    # backtrack function is called n times, because there are n possible starting points for the subset
    # For each starting point, the backtrack function iterates through all k elements
        # This is because the comb list must contain all k elements to be a valid subset
# SPACE COMPLEXITY: O(k)
    # The comb list stores at most k elements

def combine(n, k):
    result = []

    # when doing recursive backtracking, we need to remember which value we started at so we only choose values after it
    # we need current combinations as, when we go down decision tree, we need to know what previous values we added
    
    def backtrack(start, curr_combination): 
        # start is the value we start making combinations from
            # e.g. if start = 2, combinations = [2, 3], [2, 4], etc.
        if len(curr_combination) == k: # we stop the backtracking when we have k combinations – we don't add anymore elements to it
            result.append(curr_combination.copy()) # since we will continue to add to curr_combination in other recursive calls, we add a copy of it to result so when we update combinations we don't add it to result
            return
        
        for i in range(start, n+1): # i = 1 to n
            curr_combination.append(i)
            backtrack(i+1, curr_combination)
            curr_combination.pop() # after choosing i, now we want to choose the next value -> clean up the i before we add the next one
    
    backtrack(1, []) # we start at 1 since the values we can form combinations with are 1-n
    return result