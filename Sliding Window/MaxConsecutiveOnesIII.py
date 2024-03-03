# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# MEDIUM
# Tags: slidingwindowlc, leetcode75lc, lc75lc, #1004

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

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def longestOnes(nums, k):
    zero_count = max_window = 0
    l = 0
    for r in range(len(nums)):
        # expand window from the right
        # if last element in window is 0, increase zero_count by 1
        if nums[r] == 0:
            zero_count += 1
        # More sophisticated way to write this: 
            # zero_count += int(nums[r] == 0)

        while zero_count > k: # while there are more 0's than k (which is not allowed),
            if nums[l] == 0:
                zero_count -= 1 # shrink window from left until number of 0's = k
            # More sophisticated way to write this: 
                # zero_count -= int(nums[l] == 0)
            l += 1
        
        max_window = max(max_window, r-l+1)
    
    return max_window

#==========================================================================================================

# ✅ ALGORITHM 2: OPTIMIZED SLIDING WINDOW (hard to understand)
# this algorithm implicitly keeps track of the maximum length by not shrinking the window more than necessary
    # Since right pointer +1 in each iteration until the of nums, and left pointer is only moved when window has more than k 0's, the final value of right-left+1 when right pointer reaches end of array gives the maximum length of valid subarray

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def longestOnes(nums, k):
    left = 0
    for right in range(len(nums)):
        k -= 1 - nums[right] # if nums[right] = 0, k - 1

        if k < 0: # if k is -ve, current window includes more than k 0's which is not allowed
            # shrink window from left:
            k += 1 - nums[left] # if nums[left] = 0, k + 1
            left += 1

    return right - left + 1