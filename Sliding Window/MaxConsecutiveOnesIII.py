# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# MEDIUM

# GIVEN:
    # integer array, nums
    # integer, k

# TASK:
    # Return the max no. of consecutive 1's in nums if you can flip at most k 0's

# EXAMPLES:
    # Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    # Output: 6
    # Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    # Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    # Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    # Output: 10
    # Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    # Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

###########################################################################################################

# ✅ ALGORITHM 1: SLIDING WINDOW
# l and r pointers keep track of sliding window
# if elem at end of window = 0, zero counter +1
# while zero counter > k, shift left pointer until zero counter = k
# keep track of max count

def longestOnes(nums, k):
    if k == 0 and 1 not in nums: return 0 # for edge case where nums = [0, 0, 0], k = 0
    l = zero_count = max_count = 0
    for r in range(len(nums)):
        zero_count += int(nums[r] == 0) # if nums[r] = 0, zero_count += 1

        while zero_count > k: # if there are more 0's than k, start shifting left pointer until number of 0's = k
            zero_count -= int(nums[l] == 0) # if nums[l] = 0, zero_count -= 1
            l += 1
        
        max_count = max(max_count, r-l)
    
    return max_count+1 # since length = right pointer - left pointer + 1

#==========================================================================================================

# ✅ ALGORITHM 2: OPTIMIZED SLIDING WINDOW (hard to understand)

def longestOnes(nums, k):
    left = 0
    for right in range(len(nums)):
        k -= 1 - nums[right] # if nums[right] = 0, k - 1

        if k < 0:
            k += 1 - nums[left] # if nums[left] = 0, k + 1
            left += 1

    return right - left + 1