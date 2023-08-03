# https://leetcode.com/problems/subsets-ii/
# MEDIUM
# Tags: backtracklc, #90

# GIVEN:
    # an integer array nums that may contain duplicates

# TASK:
    # return all possible subsets
    # NOTE: The solution set must not contain duplicate subsets
    # Return the solution in any order

# EXAMPLES:
    # Input: nums = [1,2,2]
    # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

    # Input: nums = [0]
    # Output: [[],[0]]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING

# TIME COMPLEXITY: O(n * 2^n)
    # to generate all subsets and then copy them into output list
    # at each decision node, there are 2 choices: to include or to exclude the current element
# SPACE COMPLEXITY: O(n)
    # we use O(n) space to maintain comb, and are modifying comb in-place with backtracking

def subsetsWithDup(nums):
    result = []
    nums.sort() # sort nums to make it easier to prevent duplicates

    def backtrack(start, comb, max_len):
        if len(comb) == max_len and comb not in result: # if current combination is done
            result.append(comb[:])
            return
        
        for i in range(start, len(nums)):
            comb.append(nums[i]) # add integer nums[i] into the current combination
            backtrack(i+1, comb, max_len)
            comb.pop()
    
    for length in range(len(nums) + 1):
        backtrack(0, [], length)
        
    return result