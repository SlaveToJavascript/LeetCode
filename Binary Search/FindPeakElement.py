# https://leetcode.com/problems/find-peak-element/
# MEDIUM
# Tags: binarysearchlc, #162

# GIVEN:
    # a 0-indexed integer array, nums

# TASK:
    # find a peak element, and return its index
    # A peak element is an element that is strictly greater than its neighbors
    # If the array contains multiple peaks, return the index to any of the peaks
    # NOTE: You must write an algorithm that runs in O(log n) time

# EXAMPLES:
    # Input: nums = [1,2,3,1]
    # Output: 2
    # Explanation: 3 is a peak element and your function should return the index number 2.

    # Input: nums = [1,2,1,3,5,6,4]
    # Output: 5
    # Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

###########################################################################################################

# ✅ ALGORITHM: BINARY SEARCH
# left, right and mid pointers
# if nums[mid] < nums[mid+1], it means the peak might be in the 2nd half of the array (after mid)
    # change left pointer to mid+1 (+1 since nums[mid+1] is the bigger no., so we don't care about the smaller number at mid anymore)
# else if nums[mid] > nums[mid+1], it means the peak might be in the 1st half of the array (before mid)
    # change right pointer to mid
# repeat while loop above until left == right; return left or right

# TIME COMPLEXITY: O(log n)
    # for binary search
# SPACE COMPLEXITY: O(1)

def findPeakElement(nums):
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if mid+1 < len(nums) and nums[mid+1] > nums[mid]: # peak is in 2nd half
            l = mid + 1
        else: # peak is in 1st half or at nums[mid]
            r = mid
    
    return l # or return r, since l = r at this point