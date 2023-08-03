# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# MEDIUM
# Tags: slidingwindowlc, #209

# GIVEN:
    # an array of positive integers, nums
    # a positive integer, target

# TASK:
    # return the minimal length of a subarray whose sum is greater than or equal to target
    # if there is no such subarray, return 0 instead

# EXAMPLES:
    # Input: target = 7, nums = [2,3,1,2,4,3]
    # Output: 2
    # Explanation: The subarray [4,3] has the minimal length under the problem constraint.

    # Input: target = 4, nums = [1,4,4]
    # Output: 1

    # Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    # Output: 0

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# For each element in nums, get every subarray with that element and check if sum of subarray = target
# There are n elements; each element can form ~n different subarrays with the other elements

# TIME COMPLEXITY: O(n^2) ❌

#==========================================================================================================

# ✅ ALGORITHM 2: SLIDING WINDOW
# keep a window starting at index l and ending at index r. Both l and r start from 0
# keep a total sum counter that tracks the sum of the window
# if sum becomes >= target, shift l pointer forward until sum < target and subtract the removed element from total sum of the window
    # at the same time, keep track of and update minimum length of window
    # since sum >= target now, we can continue shifting our window to find if there is any smaller windows whose sum also >= target
# return minimum length of window or 0

# TIME COMPLEXITY: O(n)
    # Even tho there's a while loop inside a for loop, the left and right pointer both can only move n times each
# SPACE COMPLEXITY: O(1)

def minSubArrayLen(nums, target):
    left = 0
    min_len = float('inf')
    total_sum = 0
    
    for right in range(len(nums)):
        total_sum += nums[right]

        while total_sum >= target:
            min_len = min(min_len, right-left+1) # update minimum length of window
            total_sum -= nums[left] # remove leftmost element of the window from total sum
            left += 1 # shift left pointer forward
    
    return min_len if min_len < float('inf') else 0 # if min_len = infinity, it means the subarray is not found