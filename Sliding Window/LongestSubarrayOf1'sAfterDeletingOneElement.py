# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
# MEDIUM
# Tags: slidingwindow;c, #1493

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

# ✅ ALGORITHM 1: SLIDING WINDOW
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
    l = max_count = zero_count = 0
    
    for r in range(len(nums)): # l and r both start at 0; r iterates but l stays @ the same place unless zerocount > 1
        zero_count += int(nums[r] == 0) # this code can be written as: 
        # if nums[r] == 0: zero_count += 1

        while zero_count > 1: # if more than 1 zero, shift l pointer forward until zerocount = 1
            zero_count -= int(nums[l] == 0) # this code can be written as: 
            # if nums[l] == 0: zero_count -= 1
            l += 1
        
        # at this point, there would be max 1 zero in window
        max_count = max(max_count, r-l)
    
    return max_count # instead of returning max_count + 1 which is the total length including zero (if any), we return max_count instead as we do not include the 0
    # even if there were no 0's in the max count string, we still have to delete one element according to the question