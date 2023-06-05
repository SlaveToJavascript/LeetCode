# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# GIVEN:
    # sorted integer array, nums

# TASK:
    # remove duplicates from integer array nums
        # relative order of elements should be kept the same
    # have the result be placed in the first part of the array nums
    # if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result
    # NOTE: Do not allocate extra space for another array

# RETURN: k after placing the final result in the first k slots of nums

###########################################################################################################

# ALGORITHM 1: SORT IN-PLACE USING [:]
def removeDuplicates(nums):
    nums[:] = sorted(set(nums)) # WRONG: nums = sorted(set(nums))
    return len(nums)
# CORRECT: nums[:] replaces element in place
    # It is a slice from the beginning to the end, usually producing a shallow copy
        # shallow copy constructs a new list and inserts references into it to the objects found in the original
# WRONG: nums doesn't replace elements in the original list (creates a new list object)

#============================================================================================================

# ALGORITHM 2: TWO POINTERS
def removeDuplicates(nums):
    first = 0
    second = 1
    while second < len(nums):
        if nums[first] == nums[second]:
            second += 1
        else: 
            nums[first+1] = nums[second]
            first += 1
            second += 1
    return second+1