# 624. Maximum Distance in Arrays
# https://leetcode.com/problems/maximum-distance-in-arrays/
# MEDIUM
# Tags: arraylc, greedylc, premiumlc, #624

# GIVEN:
    # m arrays, where each array is sorted in ascending order

# TASK:
    # pick up two integers from two different arrays (each array picks one) and calculate the distance
        # distance between two integers a and b to be their absolute difference |a - b|
    # return the maximum distance

# EXAMPLES:
    # Input: arrays = [[1,2,3],[4,5],[1,2,3]]
    # Output: 4
    # Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

    # Input: arrays = [[1],[1]]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# keep track of global max and global min, but only update result when we find a new maximum, i.e. |new_max - old_min| or |old_max - new_min|

# TIME COMPLEXITY: O(n)
    # n = len(arrays)
# SPACE COMPLEXITY: O(1)

def maxDistance(arrays):
    old_min, old_max = arrays[0][0], arrays[0][-1]
    result = 0

    for array in arrays[1:]:
        new_min, new_max = array[0], array[-1]
        result = max(result, abs(new_max - old_min), abs(old_max - new_min)) # this ensures that the result is derived from min and max values from 2 different arrays
        
        old_min = min(old_min, new_min)
        old_max = max(old_max, new_max)
        # NOTE: Even if old_min and old_max end up being from the same array after an update, the key is that their values were used to calculate distances against different arrays BEFORE the update
    
    return result