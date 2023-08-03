# https://leetcode.com/problems/subsets/
# MEDIUM
# Tags: backtracklc, #78

# GIVEN:
    # an integer array nums of unique elements

# TASK:
    # return all possible subsets

# EXAMPLES:
    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    # Input: nums = [0]
    # Output: [[],[0]]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING

# TIME COMPLEXITY: O(n * 2^n)
    # to generate all subsets and then copy them into output list
    # at each decision node, there are 2 choices: to include or to exclude the current element
# SPACE COMPLEXITY: O(n)
    # we use O(n) space to maintain comb, and are modifying comb in-place with backtracking

def subsets(nums):
    result = []

    def backtrack(start, comb, length): # length is the desired length of the current combination
        if len(comb) == length: # if current combination is done
            result.append(comb[:])
            return
        
        for i in range(start, len(nums)):
            comb.append(nums[i]) # add integer nums[i] into the current combination
            backtrack(i+1, comb, length) # use next integers in nums to complete the combination
            comb.pop() # backtrack by removing nums[i] from comb
    
    # since our combination can be of any length from 0 to len(nums), we iterate over all the lengths of combinations we want to add to our results
    for length in range(len(nums) + 1):
        backtrack(0, [], length)
        
    return result