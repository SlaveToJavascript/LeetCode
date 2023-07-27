# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# MEDIUM

# GIVEN:
    # a positive integer array, arr, where arr[i] is the height of a mountain

# TASK:
    # Find and return i where arr[i] is the peak of the mountain
    # All heights on the left and right of the peak are lower
    # NOTE: must be O(log n) time complexity

# EXAMPLES:
    # Input: arr = [0,1,0]
    # Output: 1

    # Input: arr = [0,2,1,0]
    # Output: 1

    # Input: arr = [0,10,5,2]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: BINARY SEARCH
# left, right and mid pointers
# if arr[mid] < arr[mid+1], it means the peak might be in the 2nd half of the array (after mid)
    # change left pointer to mid+1 (+1 since arr[mid+1] is the bigger no., so we don't care about the smaller number at mid anymore)
# else if arr[mid] > arr[mid+1], it means the peak might be in the 1st half of the array (before mid)
    # change right pointer to mid
# repeat while loop above until left == right; return left or right

# TIME COMPLEXITY: O(log n)

def peakIndexInMountainArray(arr):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid+1] > arr[mid]: # peak is in 2nd half
            l = mid + 1
        else: # peak is in 1st half
            r = mid
    
    return l # or return r, since l = r at this point