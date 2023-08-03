# https://leetcode.com/problems/maximum-average-subarray-i/description/
# EASY
# Tags: slidingwindowlc, #643

# GIVEN:
    # integer array, nums
    # integer, k

# TASK:
    # Find a contiguous subarray of length = k that has the max avg value and return this value

# EXAMPLES:
    # Input: nums = [1,12,-5,-6,50,3], k = 4
    # Output: 12.75000
    # Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    # Input: nums = [5], k = 1
    # Output: 5.00000

###########################################################################################################

# ✅ ALGORITHM 1: SLIDING WINDOW
# We don't need to calculate the average of each subarray!
# Since the sum of each subarray is divided by the same no. (4), goal is basically to find subarray with the max sum
# Instead of computing the sum of subarrays over and over, can simply subtract first element of subarray and add next element after subarray to find the sum of next subarray

# TIME COMPLEXITY: O(n)
    # We iterate over the given nums array of length n once only
# SPACE COMPLEXITY: O(1)

def findMaxAverage(nums, k):
    k_sum = sum(nums[0:k])
    maxx = k_sum
    l, r = 0, k
    while r < len(nums):
        k_sum = k_sum - nums[l] + nums[r]
        maxx = max(maxx, k_sum)
        l += 1
        r += 1
    return maxx/float(k)