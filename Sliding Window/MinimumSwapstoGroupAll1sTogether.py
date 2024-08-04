# 1151. Minimum Swaps to Group All 1's Together
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/
# MEDIUM
# Tags: slidingwindowlc, premiumlc, #1151

# GIVEN:
    # a binary array data

# TASK:
    # return the min. no. of swaps required to group all 1’s present in the array together in any place in the array

# EXAMPLES:
    # Input: data = [1,0,1,0,1]
    # Output: 1
    # Explanation: There are 3 ways to group all 1's together:
    # [1,1,1,0,0] using 1 swap.
    # [0,1,1,1,0] using 2 swaps.
    # [0,0,1,1,1] using 1 swap.
    # The minimum is 1.

    # Input: data = [0,0,0,1,0]
    # Output: 0
    # Explanation: Since there is only one 1 in the array, no swaps are needed.

    # Input: data = [1,0,1,0,1,0,0,1,1,0,1]
    # Output: 3
    # Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# since we need to group all 1's together, first find out the total no. of 1's in the array (let this no. be "total")
# then we find the window of length = total that has the max. no. of 1's in the array
    # by finding the window with the max. no. of 1's, we can find the min. no. of swaps needed to make this window become all 1's

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def minSwaps(data):
    total = sum(data) # total no. of 1's in the array
    max_ones_count = 0 # max no. of 1's in any window of size=total
    curr_ones_count = 0 # no. of 1's in the current window

    start = 0
    for end in range(len(data)):
        if data[end] == 1:
            curr_ones_count += 1
        if end-start < total-1: # current window is too small (not size=total yet)
            continue
        elif end-start > total-1: # current window is too large -> shrink window from the left
            if data[start] == 1:
                curr_ones_count -= 1
            start += 1 # shrink window

        max_ones_count = max(curr_ones_count, max_ones_count) # window of length=total with max no. of 1's
    
    return total - max_ones_count # min. no. of swaps