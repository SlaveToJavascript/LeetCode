# https://leetcode.com/problems/search-insert-position/description/
# EASY
# Tags: binarysearchlc, #35

# GIVEN:
    # Sorted array, nums, of distinct integers

# TASK:
    # If integer target is in nums, return the index of target in nums
    # Else, if target not in nums, return the index where it would be if it were inserted in order
    # NOTE: must be O(log n) complexity (i.e. binary search)

# EXAMPLES:
    # Input: nums = [1,3,5,6], target = 5
    # Output: 2

    # Input: nums = [1,3,5,6], target = 2
    # Output: 1

    # Input: nums = [1,3,5,6], target = 7
    # Output: 4

###########################################################################################################

# ✅ ALGORITHM 1: BINARY SEARCH
# Binary search except last step if target not found in nums: return lower +1

# Time complexity: O(log n)

def searchInsert(nums, target):
    left = -1
    right = len(nums)
    while right-left > 1: # if upper-lower = 1, that means the range is empty
        mid = (right+left)//2
        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    return left+1 # if target not found, the last left index element directly precedes where target should be inserted
    # +1 because if target is inserted in order, it would be after the last left index element