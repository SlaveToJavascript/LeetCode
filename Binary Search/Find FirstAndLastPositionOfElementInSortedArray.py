# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# MEDIUM
# Tags: binarysearchlc, #34

# GIVEN:
    # an array of integers, nums, sorted in non-decreasing order

# TASK:
    # find the starting and ending position of a given target value
    # If target is not found in the array, return [-1, -1]

# EXAMPLES:
    # Input: nums = [5,7,7,8,8,10], target = 8
    # Output: [3,4]

    # Input: nums = [5,7,7,8,8,10], target = 6
    # Output: [-1,-1]

    # Input: nums = [1], target = 1
    # Output: [0,0]

    # Input: nums = [], target = 0
    # Output: [-1,-1]

###########################################################################################################

# ✅ ALGORITHM: BINARY SEARCH
# Do binary search to find target in nums
# Since nums is sorted, after we find a num that is = target, keep checking for its consecutive elements on the left and right if they are = target, and add them to result if they are

# TIME COMPLEXITY: O(logn)
# SPACE COMPLEXITY: O(1)

def searchRange(nums, target):
    result = [] # return value
    l, r = 0, len(nums)-1
    
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else: # if nums[mid] = target
            result.append(mid)
            # keep checking if the numbers on the left and right of nums[mid] (which is = target) are also = target
            mid_left = mid-1
            mid_right = mid+1
            while mid_left >= 0 and nums[mid_left] == target:
                result.append(mid_left)
                mid_left -= 1
            while mid_right < len(nums) and nums[mid_right] == target:
                result.append(mid_right)
                mid_right += 1
            break # after no more numbers are = target, break out of loop
    
    if not result: return [-1, -1] # if target not found
    if len(result) == 1: return [result[0], result[0]] # if there is only 1 element found that is = target
    return [min(result), max(result)]