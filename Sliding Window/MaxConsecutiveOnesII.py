# 487. Max Consecutive Ones II
# https://leetcode.com/problems/max-consecutive-ones-ii/
# MEDIUM
# Tags: slidingwindowlc, #487

# GIVEN:
    # binary array, nums

# TASK:
    # return the maximum number of consecutive 1's in the array if you can flip at most one 0

# EXAMPLES:
    # Input: nums = [1,0,1,1,0]
    # Output: 4
    # Explanation: 
    # - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
    # - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
    # The max number of consecutive ones is 4.

    # Input: nums = [1,0,1,1,0,1]
    # Output: 4
    # Explanation: 
    # - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
    # - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
    # The max number of consecutive ones is 4.

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# use a sliding window to keep track of the longest substring with at most 1 zero
# use a zero_count variable to keep track of the no. of 0's in window
# if zero_count > 1 (not allowed), shrink the window from the left until zero_count = 1
# update the max length of the window

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def findMaxConsecutiveOnes(nums):
    max_window_len = 0
    zero_count = 0
    
    l = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zero_count += 1
        
        while zero_count > 1:
            if nums[l] == 0:
                zero_count -= 1 # shrink window from the left
            l += 1 # move left pointer forward to shrink window
        
        max_window_len = max(max_window_len, r-l+1) # update result
    
    return max_window_len