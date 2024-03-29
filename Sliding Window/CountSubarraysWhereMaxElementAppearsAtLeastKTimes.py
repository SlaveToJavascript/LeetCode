# 2962. Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# MEDIUM
# Tags: slidingwindowlc, #2962

# GIVEN:
    # an integer array, nums
    # a positive integer, k

# TASK:
    # Return the no. of subarrays where the maximum element of nums appears at least k times in that subarray

# EXAMPLES:
    # Input: nums = [1,3,2,3,3], k = 2
    # Output: 6
    # Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

    # Input: nums = [1,4,2,1], k = 3
    # Output: 0
    # Explanation: No subarray contains the element 4 at least 3 times.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# 1. Generate all subarrayscountSubarrays
# 2. Check if the maximum element appears at least k times in that subarray
# 3. Count the no. of subarrays that satisfy the condition

# TIME COMPLEXITY: O(n^2) ❌
# SPACE COMPLEXITY: O(1)

#==========================================================================================================

# ✅ ALGORITHM 2: SLIDING WINDOW
# MAIN IDEA:
    # if a window starting at l and ending at r is a valid subarray (i.e. has at least k occurrences of max element), then all windows starting at 0, 1, 2...up until l and ending at r will be a valid subarray

# TIME COMPLEXITY: O(n) ✅
# SPACE COMPLEXITY: O(1)

def countSubarrays(nums, k):
    target = max(nums) # this is the element we're looking for in nums
    target_count = 0 # no. of occurrences of target in the current window
    result = 0 # return value

    l = 0 # left boundary of sliding window
    for r in range(len(nums)):
        if nums[r] == target: # if num at right pointer is target,
            target_count += 1 # increment target_count

        while target_count == k: # once target_count = k, every subarray ending at r and starting from any index <= l meets the criteria -> "shrink" window from left to find out how many of such subarrays exist
            if nums[l] == target: # if num at left pointer is target,
                target_count -= 1 # decrement target_count as we "shrink" the window to look for the starting point of the smallest valid subarray ending at r
            l += 1 # "shrink" window from left by shifting l pointer forward
        
        result += l # this works bc we kept shifting l pointer until target_count < k, so in this line, we're basically adding the no. of valid subarrays starting from (0...l) and ending at r to result
 
    return result