# https://leetcode.com/problems/maximum-subarray/description/

# GIVEN:
    # Given an integer array nums, find the subarray with the largest sum, and return its sum

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# 1 for loop to represent starting index
# 1 for loop to represent ending index
# 1 for loop to iterate from start to end

# TIME COMPLEXITY: O(n^3)

# Code:
# for start in range(len(array)):
#     for end in range(start, len(array)):
#         for i in range(i, j):
#             # compute sum here

#============================================================================================================

# ❌ ALGORITHM 2: SAVE THE SUMS OF PREVIOUS SUBARRAYS
# save the sum of each subarray
# then when shifting the end forward, simplay add the next number to the sum of previous subarray

# TIME COMPLEXITY: O(n^2)

# Code:
# for start in range(len(array)):
#     for end in range(start, len(array)):
#         currentSum += array[end]

#============================================================================================================

# ✅ ALGORITHM 3: REMOVE NEGATIVE PREFIX / SLIDING WINDOW
# If prefix (i.e. sum of elements) before a number is -ve, remove it out of the subarray

# TIME COMPLEXITY: O(n)

def maxSubarray(nums):
    max_subarray_sum = nums[0] # start finding max subarray sum from 1st element
    current_sum = 0 # current running sum of subarray

    for num in nums:
        if current_sum < 0: # if current sum until the element before num is -ve, 
            current_sum = 0 # remove from current sum
        current_sum += num # add current element to current subarray sum
        max_subarray_sum = max(max_subarray_sum, current_sum)
    return max_subarray_sum