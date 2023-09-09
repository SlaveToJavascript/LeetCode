# https://leetcode.com/problems/combination-sum-iv/
# MEDIUM
# Tags: dplc, #377

# GIVEN:
    # an array of distinct integers nums
    # a target integer target

# TASK:
    # return the number of possible combinations that add up to target

# EXAMPLES:
    # Input: nums = [1,2,3], target = 4
    # Output: 7
    # Explanation:
    # The possible combination ways are:
    # (1, 1, 1, 1)
    # (1, 1, 2)
    # (1, 2, 1)
    # (1, 3)
    # (2, 1, 1)
    # (2, 2)
    # (3, 1)
    # Note that different sequences are counted as different combinations.

    # Input: nums = [9], target = 3
    # Output: 0

#############################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING + CACHING
# MAIN IDEA: for every element num1, num2, num3, ... in nums, no. of combinations summing up to target = (no. of combinations summing up to target - num1) + (no. of combinations summing up to target - num2) + (no. of combinations summing up to target - num3) + ...
    # this is like saying: now that we've chosen num1, how many combinations of numbers sum up to the remaining value target - num1?
    # helper(remaining_target-num1) will return the number of combinations that sum up to the new target (remaining_target - num1) and we add the result to our running total
# dp is a hashmap where key = current target, value = no. of combinations that sum up to current target
# Base case: if remaining_target = 0, return 1
    # if remaining_target = 0, we have found a combi that adds up to target -> return 1 to count this valid combi
# if remaining_target < 0, return 0
    # if remaining_target < 0, sum of the current combi exceeds the target -> not a valid combi

# TIME COMPLEXITY: O(n * target)
    # n = length of nums
    # max depth of recursive tree = target (worst case: keep subtracting 1 from target until we reach 0)
    # max breadth of recursive tree = we are branching out n times (since we run for-loop over each element in nums at each level of recursion tree
# SPACE COMPLEXITY: O(target)
    # The size of the recursion tree can go up to target
    # dp array of size target is used

def combinationSum4(nums, target):
    dp = {}

    def helper(remaining_target):
        if remaining_target in dp:
            return dp[remaining_target]
        
        if remaining_target == 0: # we found a valid combi that sums up to target -> return 1 to count this valid combi
            return 1
        if remaining_target < 0: # sum of current combi exceeds target -> not a valid combi
            return 0
        
        combinations = 0 # return value (i.e. no. of valid combis that sum up to remaining_target)
        for num in nums:
            combinations += helper(remaining_target - num)
        
        dp[remaining_target] = combinations # add result to dp
        return combinations
    
    return helper(target)