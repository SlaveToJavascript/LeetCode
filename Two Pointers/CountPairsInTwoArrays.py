# 1885. Count Pairs in Two Arrays
# https://leetcode.com/problems/count-pairs-in-two-arrays/description
# MEDIUM
# Tags: twopointerslc, binarysearchlc, premiumlc, #1885

# GIVEN:
    # 2 integer arrays, nums1 and nums2, of length n each

# TASK:
    # count the pairs of indices (i, j) such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j]
    # Return the number of pairs satisfying the condition

# EXAMPLES:
    # Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
    # Output: 1
    # Explanation: The pairs satisfying the condition are:
    # - (0, 2) where 2 + 2 > 1 + 1.

    # Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
    # Output: 5
    # Explanation: The pairs satisfying the condition are:
    # - (0, 1) where 1 + 10 > 1 + 4.
    # - (0, 2) where 1 + 6 > 1 + 1.
    # - (1, 2) where 10 + 6 > 4 + 1.
    # - (1, 3) where 10 + 2 > 4 + 5.
    # - (2, 3) where 6 + 2 > 1 + 5.

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# Get an array of differences of nums1[i] - nums2[i] for each index i in nums1 and nums2
# sort this array of differences
# use 2 pointers, l and r, to point to the 1st (smallest) and last (largest) elements in the differences array
# while l < r:
    # if the sum of the 2 elements (smallest and largest differences) > 0, it means that nums1[l] + nums1[r] > nums2[l] + nums2[r]
        # since differences array is sorted, all the pairs that start at l...r-1 and end at r are also valid pairs -> there are r-l valid pairs in this case
        # since we have found a valid pair, move on to r-1
    # else, if the sum of the 2 elements <= 0, it is not a valid pair and we need to find a bigger pair -> l+1 to get a bigger sum

# TIME COMPLEXITY: O(n log n)
    # for sorting differences array
# SPACE COMPLEXITY: O(n)
    # for differences array which has length n

def countPairs(nums1, nums2):
    n = len(nums1)
    diffs = [nums1[i]-nums2[i] for i in range(n)]
    diffs.sort()
    result = 0

    l, r = 0, n-1 # 2 pointers
    while l < r:
        if diffs[l] + diffs[r] > 0: # this means that nums1[l] + nums1[r] > nums2[l] + nums2[r], which makes it a valid pair
            result += r-l # there are r-l valid pairs starting at l...r-1 and ending at r
            r -= 1 # move on to the next pair
        else: # this means l and r is not a valid pair
            l += 1 # move on to the next pair which would result in a larger sum since diffs array is sorted

    return result

#==========================================================================================================

# ✅ ALGORITHM 2: BINARY SEARCH
# TODO