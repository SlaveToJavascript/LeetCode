# https://leetcode.com/problems/search-in-rotated-sorted-array/
# MEDIUM
# Tags: binarysearchlc, #33

# GIVEN:
    # An integer array, nums, sorted in ascending order with distinct values
        # nums is possibly rotated at an unknown pivot index k
        # e.g. [0,1,2,4,5,6,7] rotated at pivot index 3 -> [4,5,6,7,0,1,2]
    # an integer target

# TASK:
    # return the index of target if it is in nums, or -1 if it is not in nums

# EXAMPLES:
    # Input: nums = [4,5,6,7,0,1,2], target = 0
    # Output: 4

    # Input: nums = [4,5,6,7,0,1,2], target = 3
    # Output: -1

    # Input: nums = [1], target = 0
    # Output: -1

###########################################################################################################

# ✅ ALGORITHM 1: BINARY SEARCH
# for a rotated sorted array, e.g. [4,5,6,7,0,1,2],
    # the left sorted portion is [4,5,6,7]
    # the right sorted portion is [0,1,2]
# first, we need to check if element at mid is in the left or right sorted array

# TIME COMPLEXITY: O(logn)
# SPACE COMPLEXITY: O(1)

def search(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        
        # check if mid is in left sorted portion or right sorted portion
        if nums[l] <= nums[mid]: # mid is in left sorted portion
            if target > nums[mid]:
                l = mid + 1 # if mid is in left sorted portion, all no.s to the left of mid are smaller than mid -> if target is greater than mid, then this target can only be on the right of mid
            elif target < nums[l]: # if target is even smaller than the leftmost no. (leftmost no. is supposed to be smallest in a normal sorted array) -> then target is on the right of mid
                l = mid + 1
            else:
                r = mid - 1
        else: # mid is in right sorted portion
            if target < nums[mid]:
                r = mid - 1 # if mid is in right sorted portion, all no.s to the right of mid are bigger than mid -> if target is smaller than mid, then this target can only be on the left of mid
            elif target > nums[r]:
                r = mid - 1 # if target is even bigger than the rightmost no. (rightmost no. is supposed to be the biggest no. in a normal sorted array) -> then target is on the left of mid
            else:
                l = mid + 1
    
    return -1 # target is not found in array

# [6,7,0,1,2,3,4]