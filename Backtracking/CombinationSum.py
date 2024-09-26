# https://leetcode.com/problems/combination-sum/
# MEDIUM
# Tags: backtracklc, #39

# GIVEN:
    # an array of distinct integers, candidates
    # a target integer, target

# TASK:
    # return a list of all unique combinations of candidates where the chosen numbers sum to target
    # You may return the combinations in any order

# EXAMPLES:
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    # These are the only two combinations.

    # Input: candidates = [2,3,5], target = 8
    # Output: [[2,2,2,2],[2,3,3],[3,5]]

    # Input: candidates = [2], target = 1
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# MAIN IDEA: we start by choosing one of 2 choices: to include the 1st element of candidates or not
    # if we include the 1st element:
        # we can include it again
        # we can exclude it this time
    # if we exclude the 1st element, we have another 2 choices:
        # include the 2nd element in candidates array
        # do not include this 2nd element
    # ...and so on
# at each decision made, we have a resulting 2 different choices to make
# therefore we can do recursion to get all the desired combinations

# TIME COMPLEXITY: O(n^k)
    # n = length of candidates array
    # k = max length of array
# SPACE COMPLEXITY: O(k)
    # for storing the combination, which could be of length k at max

def combinationSum(candidates, target):
    result = []

    def backtrack(i, comb):
        # pointer i tracks which candidates we're still allowed to choose
            # i.e. if i = 2, we can choose from candidates[2:] onwards (including element at index 2)
        # comb is a 1D list of numbers which is the current combination
            # e.g. [2,2,3] is a combination
        
        if sum(comb) == target:
            result.append(comb[:]) # since we're going to continue using the "comb" variable after this, we store a deep copy of it into the result, instead of comb itself
            return
        
        # base case where it's impossible to find a combination:
            # 1) if i is out of bounds
            # 2) if sum of combination > target
        if i >= len(candidates) or sum(comb) > target:
            return
        
        # we have 2 choices to choose from: 
            # 1) include the value at index i, OR
            # 2) exclude the value at index i
        
        # CHOICE 1: include the value at current index i
        comb.append(candidates[i])
        backtrack(i, comb) # we add the current element at i to comb
            # here, i stays the same as we're not restricting which candidates we're allowed to choose
        comb.pop() # remove candidates[i] from current combination before we go to the 2nd choice

        # CHOICE 2: do not include the value at index i
        backtrack(i+1, comb)
            # i+1 indicates we can't include any occurrences of candidates[i]
            # comb remains the same as we didn't add anything to it here
        
    backtrack(0, [], 0) # starts at the 1st element, with sum of combinations = 0
    return result