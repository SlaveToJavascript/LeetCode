# https://leetcode.com/problems/delete-and-earn/description/
# MEDIUM
# Tags: dplc, #740

# GIVEN:
    # an integer array, nums, of points that can be earned

# TASK:
    # maximize the no. of points earned by performing the following operation any no. of times:
        # Pick any nums[i] and delete it to earn nums[i] points
        # Afterwards, you must delete every occurrence of nums[i]-1 and nums[i]+1

# EXAMPLES:
    # Input: nums = [3,4,2]
    # Output: 6
    # Explanation: You can perform the following operations:
    # - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
    # - Delete 2 to earn 2 points. nums = [].
    # You earn a total of 6 points.

    # Input: nums = [2,2,3,3,3,4]
    # Output: 9
    # Explanation: You can perform the following operations:
    # - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
    # - Delete a 3 again to earn 3 points. nums = [3].
    # - Delete a 3 once more to earn 3 points. nums = [].
    # You earn a total of 9 points.

###########################################################################################################

# ✅ ALGORITHM 1: ITERATIVE DP
# Hint: If you take a number i, have to delete all i-1's and i+1's, so you might as well take all i's (to maximize no. of points earned)
# For each num in nums, add it to a dictionary as key and its corresponding value as frequency in nums
# Create integer array dp of len(dictionary) (where each dp[i] should be the max no. of points that can be earned up till i)
# But first, start by populating dp with total points earned from deleting each no.
    # i.e. each number (key) in dictonary * frequency (value) of that number
# also get a list, s, of unique sorted integers in nums (which should have the same length as dp)
# formula for each dp[i] (where dp[i] = max no. of points that can be earned up till i):
    # if s[i]-s[i-1] == 1, dp[i] = max(dp[i] + dp[i-2], dp[i-1])
    # else, dp[i] = dp[i] + dp[i-1]
# return the last element in dp

# TIME COMPLEXITY: O(n logn), to sort s
# SPACE COMPLEXITY: O(n), for dictionary and dp

from collections import Counter

def deleteAndEarn(nums):
    if len(nums) == 1: return nums[0]
    nums.sort()
    d = Counter(nums) # dictionary of each unique no. in nums (as key) and their corresponding frequencies (as values)
    if len(d) == 1: # edge case
        return list(d)[0] * list(d.values())[0]
    dp = []
    for key in d:
        dp.append(key * d[key])
    s = sorted(list(d))
    dp[1] = max(dp[1], dp[0]) if s[1]-s[0]==1 else dp[1]+dp[0]
    for i in range(2, len(dp)):
        dp[i] = max(dp[i] + dp[i-2], dp[i-1]) if s[i]-s[i-1]==1 else dp[i]+dp[i-1]
    return dp[-1]