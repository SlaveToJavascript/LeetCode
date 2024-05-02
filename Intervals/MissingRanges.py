# 163. Missing Ranges
# https://leetcode.com/problems/missing-ranges/
# EASY
# Tags: intervalslc, #163

# GIVEN:
    # an inclusive range, [lower, upper]
    # a sorted unique integer array, nums, where all elements are within the inclusive range
    # NOTE: A number x is considered missing if x is in the range [lower, upper] and x is not in nums

# TASK:
    # Return the shortest sorted list of ranges that exactly covers all the missing numbers
        # That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges

# EXAMPLES:
    # Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    # Output: [[2,2],[4,49],[51,74],[76,99]]
    # Explanation: The ranges are:
    # [2,2]
    # [4,49]
    # [51,74]
    # [76,99]

    # Input: nums = [-1], lower = -1, upper = -1
    # Output: []
    # Explanation: There are no missing ranges since there are no missing numbers.

###########################################################################################################

# ✅ ALGORITHM: INTERVALS
# for each num in nums, we check if the difference between num and its previous no. is > 1
    # if it is, we add [previous_num+1, num-1] to the result
# to handle the first interval (i.e. from lower to nums[0]), we initiate the previous no. to lower-1
# to handle the last interval (i.e. from nums[-1] to upper), we initiate the current no. to upper+1
    # these operations would ensure that if we have to add the 1st/last interval to result, the difference between previous no. and current no. would be > 1 -> hence would be correctly handled (i.e. added to result array)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def findMissingRanges(nums, lower, upper):
    result = []
    prev = lower-1 # initiate previous no. to lower-1 to correctly handle the 1st interval

    for i in range(len(nums)+1):
        if i == len(nums):
            curr == upper+1 # to correctly handle the last interval
        else:
            curr = nums[i]
        
        if curr - prev > 1:
            result.append([prev+1, curr-1])
        
        prev = curr # update previous no. to current no. for the next iteration

    return result