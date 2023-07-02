# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# MEDIUM

# GIVEN:
    # sorted integer array, nums

# TASK:
    # remove duplicates in-place such that each unique element appears at most twice
    # have the result be placed in the first part of the array nums
    # if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result
    # NOTE: Do not allocate extra space for another array

# RETURN: k after placing the final result in the first k slots of nums

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS

def removeDuplicates(nums):
    left = 2 # start from index 2 since we don't care about the first 2 elements in the array - they may either be different or the same
    for right in range(2, len(nums)):
        # if nums[right] == nums[left-2]:
            # both are equal, meaning there is a duplicate and updation needed
            # left remains at the same index (which needs to be updated), while right continues incrementing to find the next no. that is different (to update left with it)
        if nums[right] != nums[left-2]: # no duplicate OR a different no. is found
        # no.s are different, meaning it can be used to replace the repeated no.
            nums[left] = nums[right] # replace the number at left which was needed to be replaced
            i += 1
    return i