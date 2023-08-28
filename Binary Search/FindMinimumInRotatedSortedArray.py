# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description
# MEDIUM
# Tags: binarysearchlc, #153

# GIVEN:
    # An integer array, nums, sorted in ascending order with distinct values
        # nums is possibly rotated at an unknown pivot index k
        # e.g. [0,1,2,4,5,6,7] rotated at pivot index 3 -> [4,5,6,7,0,1,2]

# TASK:
    # return the smallest number in array

# EXAMPLES:
    # Input: nums = [3,4,5,1,2]
    # Output: 1
    # Explanation: The original array was [1,2,3,4,5] rotated 3 times.

    # Input: nums = [4,5,6,7,0,1,2]
    # Output: 0
    # Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

    # Input: nums = [11,13,15,17]
    # Output: 11
    # Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

###########################################################################################################

# ✅ ALGORITHM: BINARY SEARCH
# for a rotated sorted array, e.g. [4,5,6,7,0,1,2],
    # the left sorted portion is [4,5,6,7]
    # the right sorted portion is [0,1,2]
# first, we need to check if element at mid is in the left or right sorted array
    # if mid is in left sorted portion (e.g. mid element is 7), smallest no. could be at the left or right
        # if right no. is smaller than mid number, e.g. [4,5,6,7,0,1,2] -> smallest no. is on the right of mid
        # if right no. is bigger than mid number, e.g. [0,1,2,4,5,6,7] -> smallest no. is on the left of mid
    # if mid is in the right sorted portion, e.g. [6,7,0,1,2,3,4], smallest no. is DEFINITELY on the left of mid or smallest number = mid
        # because if mid is in the right sorted portion, all numbers to the right of mid are bigger than mid!

# TIME COMPLEXITY: O(logn)
# SPACE COMPLEXITY: O(1)

def findMin(nums):
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r) // 2
        # check if mid is in left sorted portion or right sorted portion
        if nums[mid] >= nums[l]: # mid is in left sorted portion
            if nums[r] < nums[mid]: # if right no. < mid no., e.g. [4,5,6,7,0,1,2] -> smallest no. is on the right
                l = mid + 1
            else: # if right no. < mid no., e.g. [0,1,2,4,5,6,7] -> smallest no. is on the left
                r = mid - 1
        else: # mid is in right sorted portion
            r = mid # smallest is mid or on the left of mid, bc all no.s on the right of mid are bigger than mid, e.g. [6,7,0,1,2,3,4]
                # note: cannot do r = mid-1 as mid might be smallest no.

    return nums[l] # at this point, l=r