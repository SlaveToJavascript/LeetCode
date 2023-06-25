# https://leetcode.com/problems/find-pivot-index/

# GIVEN:
    # integer array nums

# TASK:
    # find and return pivot index of array nums, i.e. 
    # sum of elements on the left of pivot index = sum of elements on the right of pivot index
    # return -1 if there is no pivot index

# EXAMPLES:
    # Input: nums = [1,7,3,6,5,6]
    # Output: 3
    # Explanation:
        # The pivot index is 3.
        # Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        # Right sum = nums[4] + nums[5] = 5 + 6 = 11

    # Input: nums = [1,2,3]
    # Output: -1
    # Explanation:
        # There is no index that satisfies the conditions in the problem statement.

    # Input: nums = [2,1,-1]
    # Output: 0
    # Explanation:
        # The pivot index is 0.
        # Left sum = 0 (no elements to the left of index 0)
        # Right sum = nums[1] + nums[2] = 1 + -1 = 0

###########################################################################################################

# ✅ ALGORITHM 1: COMPARE LEFT AND RIGHT SUMS FOR EACH ELEMENT
# Iterate nums and compare if sum of elements on the left = sum of elements on the right

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def pivotIndex(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]): # exclude pivot element in left and right element sums
            return i
    return -1 # pivot index not found