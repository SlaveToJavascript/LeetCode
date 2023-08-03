# https://leetcode.com/problems/combination-sum-iii/
# MEDIUM
# Tags: backtracklc, #216

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    # Only numbers 1 through 9 are used.
    # Each number is used at most once.

# Return a list of all possible valid combinations
# The list must not contain the same combination twice, and the combinations may be returned in any order

# EXAMPLES:
    # Input: k = 3, n = 7
    # Output: [[1,2,4]]
    # Explanation:
    # 1 + 2 + 4 = 7
    # There are no other valid combinations.

    # Input: k = 3, n = 9
    # Output: [[1,2,6],[1,3,5],[2,3,4]]
    # Explanation:
    # 1 + 2 + 6 = 9
    # 1 + 3 + 5 = 9
    # 2 + 3 + 4 = 9
    # There are no other valid combinations.

    # Input: k = 4, n = 1
    # Output: []
    # Explanation: There are no valid combinations.
    # Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING

# NOTE: to prevent duplicate combinations:
    # sort the candidates array
    # if we choose to include 1, we can include all 1's from the rest of the array
    # if we choose to skip 1, we cannot include any more 1's in our combination
# The idea behind this is that, if in one decision path we include 1's while in the other decision path we don't include any 1's, then the combinations from these 2 different decision paths will always be different

# TIME COMPLEXITY: O(k * 9^k)
    # Recursion depth is k and at each level we have 9 digits to choose from -> O(9^k)
# SPACE COMPLEXITY: O(k)
    # in the worst case, result array has a size of k

def combinationSum3(k, n):
    result = []

    def backtrack(start, comb, total):
        if total == n and len(comb) == k: # this is the desired state
            result.append(comb[:]) # add deep copy of current combi to result
            return
        
        if start > 9 or total > n or len(comb) > k: # base cases
            return
        
        for i in range(start, 10): # i = 1 to 9
            comb.append(i)
            backtrack(i+1, comb, total + i)
            comb.pop()
    
    backtrack(1, [], 0)
    return result