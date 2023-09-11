# https://leetcode.com/problems/median-of-two-sorted-arrays/
# HARD
# Tags: binarysearchlc, #4

# GIVEN:
    # 2 sorted arrays, nums1 and nums2, of size m and n respectively

# TASK:
    # return the median of the two sorted arrays
    # NOTE: The overall run time complexity should be O(log (m+n))

# EXAMPLES:
    # Input: nums1 = [1,3], nums2 = [2]
    # Output: 2.00000
    # Explanation: merged array = [1,2,3] and median is 2.

    # Input: nums1 = [1,2], nums2 = [3,4]
    # Output: 2.50000
    # Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

###########################################################################################################

# ✅ ALGORITHM: BINARY SEARCH
# get the combined total length of both arrays
# length of each left and right partition = combined length // 2
# get size of left half of the shorter array (let's say it's array A)
    # if size is odd, left half should include the middle element
# this left half of array A, together with the 1st "combined length // 2 - size of left half of array A" elements in array B, form the left half of the combined array
# now we check if this left half is indeed the left half of the combined array of A + B
    # check if the rightmost element in the left partition in array A is <= the 1st element after the left partition of array B
    # check if the rightmost element in the left partition in array B is <= the 1st element after the left partition of array A
        # if BOTH true, the partition is done correctly, i.e. the left partition of A + the left partition of B = the correct left half of the combined array A + B
            # if combined A+B length is even
                # median = max between (rightmost element in the left partition in A VS rightmost element in the left partition in B) + min between (1st element after left partition in A VS 1st element after left partition in B), divide this sum by 2
            # else, if combined A+B length is odd,
                # median = min between (1st element after left partition in A VS 1st element after left partition in B)
        # else if rightmost element in the left partition in array A > 1st element after left partition in array B,
            # this means we have too many elements from A -> reduce size of A by moving right pointer to the left
        # else (if 1st element after left partition in array A < rightmost element in the left partition in array B),
            # increase size of A by shifting left pointer to the right

# TIME COMPLEXITY: O(log(min(m,n)))
    # m = length of nums1
    # n = length of nums2
    # we do binary search on the shorter array, so time complexity is O(log(min(m,n)))
# SPACE COMPLEXITY: O(1)

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1 # ensures that nums1 is always the shorter array
            # if nums1 is the longer array, swap nums1 and nums2
    
    combined_len = len(nums1) + len(nums2) # A+B total length
    half_len = combined_len // 2

    l, r = 0, len(nums1)-1 # left and right pointers for the shorter array (nums1)

    while True: # since we know it's guaranteed that a median will be found and returned, can do while True
        mid1 = (l+r) // 2 # midpoint of shorter array (nums1)
        nums2Pointer = half_len - 1 - (mid1 + 1) # pointer for nums2 (points to the rightmost element in the left partition in nums2)

        nums1Left = nums1[mid1] if mid1 >= 0 else float('-inf') # rightmost element in the left partition in nums1
        nums1Right = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float('inf') # 1st element after left partition in nums1
        nums2Left = nums2[nums2Pointer] if nums2Pointer >= 0 else float('-inf') # rightmost element in the left partition in nums2
        nums2Right = nums2[nums2Pointer + 1] if nums2Pointer + 1 < len(nums2) else float('inf') # 1st element after left partition in nums2

        if nums1Left <= nums2Right and nums2Left <= nums1Right: # partitioning is done correct
            if combined_len % 2 == 0: # if combined array length is even
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            else: # if combined array length is odd
                return min(nums1Right, nums2Right)
        
        elif nums1Left > nums2Right: # we have too many elements from nums1 -> reduce size of nums1
            r = mid1 - 1

        else: # if nums1Right < nums2Left
            l = mid1 + 1 # increase size of left partition of nums1