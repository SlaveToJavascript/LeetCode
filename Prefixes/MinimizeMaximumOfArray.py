# 2439. Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/
# MEDIUM
# Tags: prefixlc, #2439

# GIVEN:
    # a 0-indexed array, nums, comprising of n non-negative integers

# TASK:
    # In one operation, you must:
        # Choose an integer i such that 1 <= i < n and nums[i] > 0.
        # Decrease nums[i] by 1.
        # Increase nums[i - 1] by 1.
    # Return the minimum possible value of the maximum integer of nums after performing any number of operations.

# EXAPLES:
    # Input: nums = [3,7,1,6]
    # Output: 5
    # Explanation:
    # One set of optimal operations is as follows:
    # 1. Choose i = 1, and nums becomes [4,6,1,6].
    # 2. Choose i = 3, and nums becomes [4,6,2,5].
    # 3. Choose i = 1, and nums becomes [5,5,2,5].
    # The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
    # Therefore, we return 5.

    # Input: nums = [10,1]
    # Output: 10
    # Explanation:
    # It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS
    # https://youtu.be/AeHMvcKuR0Y?si=5WdZrrJnN3J8riaE&t=197
# ! MAIN IDEA: since we are subtracting values from elements on the right and adding them to elements on the left, as we iterate i from left to right, for every subarray starting from the first element and ending with element at i, calculate the average value (i.e. sum of values/no. of elements) and assign result = max(avg, result)
    # initialize result = nums[0] (1st element in nums), since we need to return the MAXIMUM element in nums, and since the 1st element can only be increased (it cannot be decreased), hence the reuslt cannot possibly be less than the 1st element

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

import math

def minimizeArrayValue(nums):
    result = prefix_sum = nums[0] # initialize result as 1st element in nums since we need result to be max. element from nums, and nums[0] can only be increased -> result can only be greater than nums[0]
        # prefix_sum is the running sum of elements in nums, incremented from left to right
    
    for i in range(1, len(nums)): # start iterating from 2nd element since we cannot pick the 1st element to decrease
        prefix_sum += nums[i]
        result = max(result, math.ceil(prefix_sum/(i+1))) # round up, since we need to return the maximum element in nums
    
    return result