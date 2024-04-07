# 280. Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/
# MEDIUM
# Tags: arraylc, sortlc, greedylc, #280

# GIVEN:
    # an integer array, nums

# TASK:
    # reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]...
    # You may assume the input array always has a valid answer

# EXAMPLES:
    # Input: nums = [3,5,2,1,6,4]
    # Output: [3,5,1,6,2,4]
    # Explanation: [1,6,2,5,3,4] is also accepted.

    # Input: nums = [6,6,5,6,3,8]
    # Output: [6,6,5,6,3,8]

###########################################################################################################

# ✅ ALGORITHM 1: SORT AND SWAP
# sort the array and swap adjacent elements starting from the 2nd element
    # i.e. iterate through the array, for any index i where i is odd, swap this element with the element at i+1

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(1)

def wiggleSort(nums):
    nums.sort()
    
    for i in range(len(nums)-1):
        if i % 2 != 0: # i is odd
            nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums

#============================================================================================================

# ✅✅✅ ALGORITHM 2: GREEDY
# elements at even indexes should be SMALLER than their previous/next neighbors
# elements at odd indexes should be LARGER than their previous/next neighbors
# THEREFORE, iterate through the array and compare each element at i with their next neighbor ; if the above requirements are not fulfilled, swap nums[i] and nums[i+1]

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def wiggleSort(nums):
    for i in range(len(nums)-1):
        if i % 2 == 0: # i is even -> nums[i] should be SMALLER than next element
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i] # requirement not satisfied -> swap
        else: # i is odd -> nums[i] should be LARGER than next element
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i] # requirement not satisfied -> swap
    
    return nums