# https://leetcode.com/problems/merge-sorted-array/

# GIVEN:
    # two sorted integer arrays, nums1 and nums2

# TASK:
    # Merge and return nums1 and nums2 as a single sorted array
    # nums1 has m integers and nums2 has n integers
    # NOTE: modify nums1 in-place without returning the answer

# EXAMPLES:
    # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # Output: [1,2,2,3,5,6]
    # Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    # The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

    # Input: nums1 = [1], m = 1, nums2 = [], n = 0
    # Output: [1]
    # Explanation: The arrays we are merging are [1] and [].
    # The result of the merge is [1].

    # Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    # Output: [1]
    # Explanation: The arrays we are merging are [] and [1].
    # The result of the merge is [1].
    # Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

###########################################################################################################

# ✅ ALGORITHM 1: PYTHON SORT()
# Put nums2 elements into nums1, then sort nums1 with Python sort() function

# TIME COMPLEXITY: O((n+m)log(n+m))
    # Python sort() function has O(n logn) runtime
# SPACE COMPLEXITY: O(1)

def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i] # replace trailing 0's in num1 with num2 elements
    nums1.sort() # O(n logn)

#============================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS