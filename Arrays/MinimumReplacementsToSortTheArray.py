# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
# HARD
# Tags: arraylc, greedylc, #2366

# GIVEN:
    # integer array nums

# TASK:
    # In one operation you can replace any element of the array with any two elements that sum to it
        # e.g. nums = [5,6,7]
        # In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7]
    # Return the minimum number of operations to make an array that is sorted in non-decreasing order

# EXAMPLES:
    # Input: nums = [3,9,3]
    # Output: 2
    # Explanation: Here are the steps to sort the array in non-decreasing order:
    # - From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
    # - From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
    # There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

    # Input: nums = [1,2,3,4,5]
    # Output: 0
    # Explanation: The array is already in non-decreasing order. Therefore, we return 0. 

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# Since resulting array must be in non-decreasing i.e. increasing order, we should iterate array from back to front, to break down the larger numbers into smaller numbers
    # if we iterate from front to back, the numbers in the back may be smaller than those broken down in front -> the larger numbers in the front that was broken down now needs to be processed again
# while iterating from back to front, for any element nums[i] that is larger than its right element nums[i+1], 
    # check if nums[i] can be divided by nums[i+1] -> if yes, split nums[i] into blocks of nums[i+1] each
    # else, split nums[i] into nums[i] // nums[i+1] + 1 blocks, as evenly as possible
        # e.g. instead of splitting 7 into [1,3,3], split into [2,2,3] instead
    # increment the total no. of operations with num_elements-1
        # num_elements is the number of blocks we're splitting nums[i] into
            # e.g. if [7] -> [2,2,3], num_elements = 3
# return the total no. of operations

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def minimumReplacement(nums):
    result = 0

    for i in range(len(nums)-2, -1, -1): # iterate from 2nd last element from back to front
        if nums[i] > nums[i+1]: # if current elem greater than its right elem, need to break it down
            if nums[i] % nums[i+1] == 0: # if current elem is divisible by its right elem
                num_elements = nums[i] // nums[i+1] # no. of blocks = curr elem / right elem
            else: # if current elem is not divisible by its right elem
                num_elements = nums[i] // nums[i+1] + 1 # no. of blocks = curr elem / right elem + 1 (extra block for the remainder)
            
            result += num_elements-1 # no. of operations = no. of blocks - 1
            nums[i] = nums[i] // num_elements # replace curr elem with the min. value of the blocks before the next iteration
                # to get min. value of the blocks including the remainder blocks, we can simply do curr elem // no. of blocks
    
    return result