# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/description
# EASY
# Tags: intersectionlc, arraylc, setlc, hashmaplc, #349

# GIVEN:
    # 2 integer arrays, nums1 and nums2

# TASK:
    # return an array of their intersection
    # Each element in the result must be unique and you may return the result in any order

###########################################################################################################

# ✅ ALGORITHM 1: PYTHON INTERSECTION FUNCTION/OPERATOR

# TIME COMPLEXITY: O(n + m)
    # n and m are the respective lengths of the arrays
    # NOTE: the TC of '&' operator is O(min(n,m)) since it iterates the smaller set and checks each element to see if it's in the larger set
# SPACE COMPLEXITY: O(n + m)

def intersection(nums1, nums2):
    nums1, nums2 = set(nums1), set(nums2) # convert both arrays to sets
    return nums1 & nums2 # & is the intersection operator in Python
        # OR: return nums1.intersection(nums2)