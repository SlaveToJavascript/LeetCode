# https://leetcode.com/problems/maximum-subarray/description/
# MEDIUM
# Tags: kadanelc, #918

# GIVEN:
    # a circular integer array nums of length n

# TASK:
    # return the maximum possible sum of a non-empty subarray of nums
        # NOTE: A circular array means the end of the array connects to the beginning of the array

# EXAMPLES:
    # Input: nums = [1,-2,3,-2]
    # Output: 3
    # Explanation: Subarray [3] has maximum sum 3.

    # Input: nums = [5,-3,5]
    # Output: 10
    # Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

    # Input: nums = [-3,-2,-3]
    # Output: -2
    # Explanation: Subarray [-2] has maximum sum -2.

###########################################################################################################

# ✅ ALGORITHM 1: KADANE'S ALGORITHM
# if we know which elements are part of the maximum subarray sum (we can find out using the solution for MaximumSubarray.py), then we know which elements are part of the minimum subarray sum
    # e.g. for nums = [1,-2,3,-2], since [3] is the maximum contiguous subarray, the minimum contiguous subarray is everything else (i.e. [1, -2, -2]) -> this is a contiguous minimum subarray since the array is circular
# Therefore, if we find out what's the minimum contiguous subarray, we will also know the maximum contiguous subarray (by taking all elements that are not part of the minimum contiguous subarray)
    # max_contiguous_sum = sum(nums) - global_min
# EDGE CASE: if every element in nums is -ve, we would return 0 as sum(nums) - global_min = 0
    # but this is wrong since we cannot take an empty subarray as the max contiguous sum
    # if every number in nums is -ve, global_max would be -ve also
    # therefore, we need to check if global_max is -ve, and if it is, return global_max instead of sum(nums) - global_min

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def maxSubarraySumCircular(nums):
    global_min = curr_min = float('inf') # initiate global_min and curr_min
    global_max = curr_max = float('-inf') # initiate global_max and curr_max

    for num in nums: # for each no. in nums,
        curr_min = min(num, curr_min + num) # get the min between current no. sum of no.s from 1st to current no.
        global_min = min(global_min, curr_min) # update global_min after every curr_min update
        curr_max = max(num, curr_max + num) # get the max between current no. sum of no.s from 1st to current no.
        global_max = max(global_max, curr_max) # update global_max after every curr_max update
    
    # Handle edge case where all no.s in nums is negative -> 0 will be wrongly returned
    if global_max < 0:
        return global_max

    return max(sum(nums) - global_min, global_max)