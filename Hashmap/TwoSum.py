# https://leetcode.com/problems/two-sum/

# GIVEN:
# integer array, nums
# integer target

# TASK:
# find and return the indices of 2 no.s in nums that add up to target
# NOTE: there is exactly 1 solution, and you may not use the same element twice
# return integer array answer of the 2 indices in any order

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# 2 for-loops

# Time complexity: O(n^2) ❌
# Space complexity: O(1)

def twoSum(nums, target):
    for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]

#==========================================================================================================

# ✅ ALGORITHM 2: DICTIONARY SEARCH
# Iterate nums to create hashmap of (target-nums) results (i.e. 2nd number in the required pair) as key, 
    # and index of current num (i.e. 1st number in the required pair) as value
# Concurrently in the iteration, if the 2nd number in the pair is found in hashmap, return indices of pair

# Time complexity: O(n)
# Space complexity: O(n)
    # extra space required depends on the no. of items in dictionary, which stores exactly n elements

def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            return [d[num], i]
        else:
            d[target - num] = i