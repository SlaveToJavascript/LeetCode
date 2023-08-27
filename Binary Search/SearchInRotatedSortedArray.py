# https://leetcode.com/problems/search-in-rotated-sorted-array/
# MEDIUM
# Tags: binarysearchlc, #33

# GIVEN:
    # An integer array nums sorted in ascending order with distinct values
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