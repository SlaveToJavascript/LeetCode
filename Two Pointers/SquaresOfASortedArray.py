# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# EASY
# Tags: sortlc, twopointerslc, #977

# GIVEN:
    # integer array, nums, sorted in increasing order

# TASK:
    # return an array of the squares of each number sorted in increasing order

# EXAMPLES:
    # Input: nums = [-4,-1,0,3,10]
    # Output: [0,1,9,16,100]
    # Explanation: After squaring, the array becomes [16,1,0,9,100].
    # After sorting, it becomes [0,1,9,16,100].

    # Input: nums = [-7,-3,2,3,11]
    # Output: [4,9,9,49,121]

# ✅ ALGORITHM 1: SQUARE AND SORT
# Easiest approach is to just square each element of the array, then sort it and return

# TIME COMPLEXITY: O(n log n) 👎
    # for sorting
# SPACE COMPLEXITY: O(n)
    # Python's sort() function uses O(n) space

def sortedSquares(nums):
        return sorted([n*n for n in nums])

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: TWO POINTERS
# Since we know array is already sorted, keep comparing the absolute 1st and last values of nums and add the square of the bigger element to the resulting array

# TIME COMPLEXITY: O(n) 👍
# SPACE COMPLEXITY: O(n)
    # additional result array

def sortedSquares(nums):
    l, r = 0, len(nums)-1 # left and right pointers
    result = [0] * len(nums)
    for rp in range(len(nums)-1, -1, -1): # rp is the pointer for result array
        if abs(nums[l]) > abs(nums[r]):
            result[rp] = nums[l] * nums[l]
            l += 1
        else:
            result[rp] = nums[r] * nums[r]
            r -= 1
    return result