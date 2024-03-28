# 1493. Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
# MEDIUM
# Tags: slidingwindowlc, lc75lc, leetcode75lc, #1493

# GIVEN:
    # binary array, nums

# TASK:
    # Return the size of the longest non-empty subarray containing only 1's in the resulting array
    # Return 0 if there is no such subarray

# EXAMPLES:
    # Input: nums = [1,1,0,1]
    # Output: 3
    # Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

    # Input: nums = [0,1,1,1,0,1,1,0,1]
    # Output: 5
    # Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

    # Input: nums = [1,1,1]
    # Output: 2
    # Explanation: You must delete one element.

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# keep a window starting at index l and ending at index r. Both l and r start from 0
# keep a zero counter that tracks how many zeros there are in the window
# if zero counter becomes > 1, shift l pointer forward until zero_counter = 1
    # at the same time, decrease zero counter whenever the element at l is 0 (this is the removed element)
# update max length of 1's after every increment of r

# TIME COMPLEXITY: O(n)
    # Each element will be iterated over 2x max
        # Each element will be iterated over for the first time in the for loop
        # then, it might be possible to re-iterate while shrinking the window in the while loop
    # Therefore, the total time complexity would equal O(n)

def longestSubarray(nums):
    l = 0
    max_window = 0
    zero_count = 0
    
    for r in range(len(nums)): # l and r both start at 0; r iterates over nums but l stays @ the same place unless zero_count > 1
        # expand window from the right
        # if last element in window is 0, increase zero_count by 1
        if nums[r] == 0:
            zero_count += 1
        # More sophisticated way to write this: 
            # zero_count += int(nums[r] == 0)

        while zero_count > 1: # while more than 1 zero (which is not allowed)
            if nums[l] == 0:
                zero_count -= 1 # shrink window from left until zero_count = 1
            # this code can be written as:
                # zero_count -= int(nums[l] == 0)
            l += 1
        
        # at this point, there would be max 1 zero in window
        max_window = max(max_window, r-l+1)
    
    return max_window-1 # we need to -1 since there can be either 1 zero or no zeros in max_window. In either case, we need to remove 1 element, so remove either a zero or a one