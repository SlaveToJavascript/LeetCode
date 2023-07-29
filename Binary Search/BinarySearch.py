# https://leetcode.com/problems/binary-search/
# EASY
# Tags: binarysearchlc, #704

# Given integer array nums sorted in ascending order, and integer target,
# search for target in nums array.
# If target exists in nums, return its index. Otherwise, return -1.

def search(nums, target):
    upper = len(nums)
    lower = -1
    while upper-lower > 1: # if upper-lower = 1, that means the range is empty
        mid = (upper+lower)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lower = mid
        else:
            upper = mid
    return -1

# Time complexity = O(log n)
    # Reducing an area of size n down to an area of size 1:
    # 2^3 = 8
    # 2^2 = 4
    # 2^1 = 2
    # 2^0 = 1