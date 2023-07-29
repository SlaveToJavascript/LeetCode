# https://leetcode.com/problems/increasing-triplet-subsequence/description/
# MEDIUM
# Tags: #334

# GIVEN:
    # integer array, nums

# TASK:
    # return true if there exists a triple of indices where i < j < k and nums[i] < nums[j] < nums[k]
    # If no such indices exists, return false

# EXAMPLES:
    # Input: nums = [1,2,3,4,5]
    # Output: true
    # Explanation: Any triplet where i < j < k is valid

    # Input: nums = [5,4,3,2,1]
    # Output: false
    # Explanation: No triplet exists

    # Input: nums = [2,1,5,0,4,6]
    # Output: true
    # Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6

###########################################################################################################

# ✅ ALGORITHM 1
# Initialize first and second to infinity
# Iterate through nums
    # if num in nums <= first, first = num (i.e. getting the smallest number)
    # else if num in nums <= second, second = num (by this point, num is definitely > first)
    # else, return true (by this point, num is definitely > second)

# TIME COMPLEXITY: O(n)
    # because we are doing a single pass through the list
# SPACE COMPLEXITY: O(1)
    # because we are using only a constant amount of space to store the first and second variables

def increasingTriplet(nums):
    first = second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second: # i.e. first < num <= second
            second = num
        else: # i.e. first < second < num
            return True
    return False