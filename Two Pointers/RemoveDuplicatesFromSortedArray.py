# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# EASY

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

# ✅ ALGORITHM 1: SORT IN-PLACE USING [:]

def removeDuplicates(nums):
    nums[:] = sorted(set(nums)) # WRONG: nums = sorted(set(nums))
    return len(nums)
# CORRECT: nums[:] replaces element in place
    # It is a slice from the beginning to the end, usually producing a shallow copy
        # shallow copy constructs a new list and inserts references into it to the objects found in the original
# WRONG: nums doesn't replace elements in the original list (creates a new list object)

#==========================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def removeDuplicates(nums):
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
        else: 
            nums[left+1] = nums[right]
            left += 1
            right += 1
    return right+1 # since right is the INDEX of the right pointer, k (no. of non-duplicate elements) should be right+1