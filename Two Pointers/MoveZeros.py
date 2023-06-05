# https://leetcode.com/problems/move-zeroes/description/

# GIVEN:
    # integer array nums

# TASK:
    # move all 0's to the end of nums while maintaining the order of the other elements
    # Note that you must do this in-place without making a copy of the array

# RETURN:
    # nums after moving all 0's to the back

# EXAMPLES:
    # Input: nums = [0,1,0,3,12]
    # Output: [1,3,12,0,0]

    # Input: nums = [0]
    # Output: [0]

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# left pointer (for zeros) and right pointer (iterate through nums)
# right pointer iterates through nums:
    # if right != 0, swap with left (this brings all non-zero elements to the left)
        # with every swap, left pointer +1

# TIME COMPLEXITY: O(n)

def moveZeros(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right]: # if nums[right] != 0
            nums[left], nums[right] = nums[right], nums[left] # elements at left and right swap places
            left += 1

#============================================================================================================

# ✅ ALGORITHM 2: STORE ZEROS IN SEPARATE ARRAY
# iterate through nums, deleting 0's and appending them to another array
# extend() nums array with zeros array

# TIME COMPLEXITY: O(n)

def moveZeros(nums):
    i = 0
    zeros = []
    while i < len(nums):
        if not nums[i]: # if nums[i] = 0
            zeros.append(nums.pop(i))
        else:
            i += 1 # increment i only if no elements have been deleted
    nums.extend(zeros)