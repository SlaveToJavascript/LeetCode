# https://leetcode.com/problems/binary-search/
# EASY
# Tags: binarysearchlc, #704

# Given integer array nums sorted in ascending order, and integer target,
# search for target in nums array.
# If target exists in nums, return its index. Otherwise, return -1.

# TIME COMPLEXITY: O(log n)
# SPACE COMPLEXITY: O(1)

# ✅ SOLUTION 1:
def search(nums, target):
    left = 0
    right = len(nums)-1 # here, left and right pointers are within boundaries
    
    while left <= right: # if there is only 1 element in the window, left == right == mid
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 # since mid < target, target is in right half -> discard left half including mid
        else:
            right = mid - 1 # since mid > target, target is in left half -> discard right half including mid
    
    return -1


# ✅ SOLUTION 2:
def search(nums, target):
    left = -1
    right = len(nums) # here, left and right pointers are beyond boundaries
    
    while right-left > 1: # if right-left = 1, that means the range is empty
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    
    return -1


# Time complexity = O(log n)
    # Reducing an area of size n down to an area of size 1:
    # 2^3 = 8
    # 2^2 = 4
    # 2^1 = 2
    # 2^0 = 1