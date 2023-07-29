# https://leetcode.com/problems/longest-increasing-subsequence/
# MEDIUM
# Tags: dplc, #300

# GIVEN:
    # integer array, nums

# RETURN:
    # the length of the longest strictly increasing subsequence

# EXAMPLES:
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    # Input: nums = [0,1,0,3,2,3]
    # Output: 4

    # Input: nums = [0,1,0,3,2,3]
    # Output: 4

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE (DFS)
# For each element in nums, if current element > previous element, there are 2 choices: to include the element or not (because we may get a smaller element somewhere ahead which is greater than previous and picking that would be optimal) -> We try both options
# If the current element <= previous element, it can't be picked

# TIME COMPLEXITY = O(2^n) ❌
    # At each index, we have choice to either take or not take the element and we explore both ways
    # -> 2 * 2 * 2...n times = O(2^n)

def lengthOfLIS(nums):
    def solve(nums, i, prev): # i is the iterator for nums
        if i >= len(nums): return 0 # i is out of bounds -> terminate
        take, dontTake = 0, solve(nums, i + 1, prev)
        if(nums[i] > prev): # if current num > previous num,
            take = 1 + solve(nums, i + 1, nums[i]) # length of sequence + 1
        return max(take, dontTake) # return whichever choice gives max LIS
    
    return solve(nums, 0, float('-inf'))

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING
# Create integer array dp where each dp[i] = length of the LIS ending at i

#              0  1  2  3  4
# e.g. nums = [1, 2, 4, 3, 5]

# for LIS[0], there are no previous elements to compare -> the only LIS is [1] -> LIS[0] = 1

# for LIS[1], there may be:
    # LIS[1] = LIS[0], LIS[1], or
    # LIS[1] = LIS[1]
# -> LIS[1] = max(LIS[0] + 1, LIS[1]) = 2

# for LIS[2], there may be:
    # LIS[2] = LIS[0], LIS[2], or
    # LIS[2] = LIS[1], LIS[2], or
    # LIS[2] = LIS[2]
# -> LIS[2] = max(LIS[0] + LIS[2], LIS[1] + LIS[2], LIS[2])

# for LIS[3], there may be:
    # LIS[3] = LIS[0], LIS[3], or
    # LIS[3] = LIS[1], LIS[3], or
        # (note that there is no LIS[2], LIS[3] since LIS[2] > LIS[3] ❌)
    # LIS[3] = LIS[3],
# -> LIS[3] = max(LIS[0] + LIS[3], LIS[1] + LIS[3], LIS[3])

# for LIS[4], there may be:
    # LIS[4] = LIS[0], LIS[4], or
    # LIS[4] = LIS[1], LIS[4], or
    # LIS[4] = LIS[2], LIS[4], or
    # LIS[4] = LIS[3], LIS[4], or
    # LIS[4] = LIS[4]
# -> LIS[4] = max(LIS[0] + LIS[4], LIS[1] + LIS[4], LIS[2] + LIS[4], LIS[3] + LIS[4], LIS[4])

# ... and so on

# ALGORITHM FOR THE ABOVE:
# Outer for-loop, j, iterates nums array (j will always be on the right of i)
# Inner for-loop, i, iterates all elements before j (i will always be on the left of j)
# If current i < current j (which is what we want, i.e. we can extend the subsequence from i to j),
    # LIS[j] = max(existing value of LIS[j], LIS[i] + 1)
        # -> this gets the length of the longest possible subsequence up till LIS[j]
# Return max length in LIS dp array

# TIME COMPLEXITY: O(n^2)
    # We iterate over nums once, and for each element, we iterate over the entire nums array that comes before that element
# SPACE COMPLEXITY: O(n)
    # We build a dp array of size n, which takes O(n) space

def lengthOfLIS(nums):
    dp = [1] * len(nums) # initiate dp array with all 1's as length of any sequence is at least 1

    for j in range(len(nums)): # outer for-loop (j will be always be on the right side of i)
        for i in range(j): # inner nested for-loop; i iterates through all numbers before j
            if nums[i] < nums[j]: # we want nums[i] < nums[j] -> increasing subsequence
                dp[j] = max(dp[j], 1 + dp[i])
    
    return max(dp)