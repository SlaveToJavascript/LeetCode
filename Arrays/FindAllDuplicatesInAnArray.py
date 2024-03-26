# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# MEDIUM
# Tags: arraylc, hashmaplc, #442

# GIVEN:
    # integer array, nums
        # of length n, where all the integers of nums are in the range [1, n] and each integer appears once or twice

# TASK:
    # return an array of all the integers that appears twice
    # NOTE: You must write an algorithm that runs in O(n) time and uses only constant extra space

# EXAMPLES:
    # Input: nums = [4,3,2,7,8,2,3,1]
    # Output: [2,3]

    # Input: nums = [1,1,2]
    # Output: [1]

    # Input: nums = [1]
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: MARK VISITED ELEMENTS IN INPUT ARRAY (CUSTOM HASHMAP)
# MAIN IDEA:
    # for every element x in nums, x-1 is a valid index in nums -> nums[x-1] is a valid reference to an element in nums
        # because we know that every element in nums is in the range [1, n], since the indices of n are in the range [0, n-1]
    # we can use that index x-1 as a hash key, and the sign of the element (+ve / -ve) as a presence indicator
# STEPS:
    # 1. for every num in nums, check if nums[abs(num)-1] is negative
        # if it is negative, it means num has been visited before, so it is a duplicate -> add abs(num) to result array
        # if it is positive, it means num has not been visited before -> mark it as visited by making it negative
    # 2. return the result array

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def findDuplicates(nums):
    result = []

    for num in nums:
        if nums[abs(num)-1] < 0: # abs(num) has been visited -> it is a duplicate!
            result.append(abs(num))
        else:
            nums[abs(num)-1] *= -1 # mark abs(num) as visited
    
    return result