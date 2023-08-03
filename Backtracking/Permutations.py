# https://leetcode.com/problems/permutations/
# MEDIUM
# Tags: backtracklc, #46

# GIVEN:
    # an array, nums, of distinct integers

# TASK:
    # return all the possible permutations
    # You can return the answer in any order

# EXAMPLES:
    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    # Input: nums = [0,1]
    # Output: [[0,1],[1,0]]

    # Input: nums = [1]
    # Output: [[1]]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# Base case: if length of current combination = length of nums, append current combination to results array
# for every element in num, if current num does not already exist in current combination, add current num to current combination and backtrack
    # all elements in nums are distinct!

# TIME COMPLEXITY: O(n * n!)
    # n! to generate n! different permutations
    # For each of the n! combinations, we need O(n) time to copy each combination into result array
# SPACE COMPLEXITY: O(n)
    # The extra space here is for comb and the recursion call stack
    # The depth of the call stack is equal to the length of comb, which is limited to n

def permute(nums):
    result = []
        
    def backtrack(comb):
        if len(comb) == len(nums): # if length of current combination = length of nums, we found what we want
            result.append(comb[:])
            return
        
        for i in range(len(nums)): # for every element in nums,
            if nums[i] not in comb: # if current num not in current combination,
                comb.append(nums[i]) # add current num to current combination
                backtrack(comb)
                comb.pop()
        
    backtrack([])
    return result