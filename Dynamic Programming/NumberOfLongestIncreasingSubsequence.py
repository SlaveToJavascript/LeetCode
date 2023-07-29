# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# MEDIUM
# Tags: dplc, #673

# GIVEN:
    # integer array, nums

# TASK:
    # return the number of longest increasing subsequences
    # NOTE: the sequence has to be strictly increasing

# EXAMPLES:
    # Input: nums = [1,3,5,4,7]
    # Output: 2
    # Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

    # Input: nums = [2,2,2,2,2]
    # Output: 5
    # Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING (BOTTOM UP)
# Create 2 dp arrays, each initialized to [1] * len(nums): 
    # (1) lengths dp array: length[i] = length of the LIS ending at i
                        #  0 1 2 3
        # e.g. for nums = [1,3,2,4]:
            # lengths[0] = 1 since LSI ending at 1 is [1]
            # lengths[1] = 2 since LSI ending at 3 is [1,3]
            # lengths[2] = 2 since LSI ending at 2 is [1,2]
            # lengths[3] = 3 since LSI ending at 4 is [1,3,4] or [1,2,4] (max length = 3)
    # (2) counts dp array: counts[i] = number of LISs ending at i
                        #  0 1 2 3
        # e.g. for nums = [1,3,2,4]:
            # counts[0] = 1 because there is 1 LIS, [1], ending at 1
            # counts[1] = 1 because there is 1 LIS, [1,3], ending at 3
            # counts[2] = 1 because there is 1 LIS, [1,2], ending at 2
            # counts[3] = 2 because there are 2 LISs, [1,3,4] and [1,2,4], ending at 4

# Outer for-loop, j, iterates nums array (j will always be on the right of i)
# Inner for-loop, i, iterates all elements before j (i will always be on the left of j)
# If current i < current j (which is what we want, i.e. we can extend the subsequence from i to j),
    # if lengths[i] + 1 > lengths[j], 
        # it means we found a longer subsequence that ends at j compared to the subsequence ending at i
            # -> lengths[j] = lengths[i] + 1
        # Therefore, the count of LISs at j = count of LISs at i (since subsequence ending at j is an extension of subsequence ending at i)
            # i.e. counts[j] = counts[i]
    # else if length[i] + 1 = lengths[j],
        # it means we can extend every LIS ending at i with element at j to create new longest increasing subsequences ending at j
            # -> we add counts[i] into counts[j] so the updated counts[j] includes all LISs up till nums[i] + all LISs up till nums[j]
            # i.e. counts[j] += counts[i]
# Find max possible length of any LIS
# Find the no. of LISs possessing this max possible length and return it

# TIME COMPLEXITY: O(n^2)
    # We iterate over nums once, and for each element, we iterate over the entire nums array that comes before that element
# SPACE COMPLEXITY: O(n)
    # We build 2 dp arrays of size n, which takes O(n) space

def findNumberOfLIS(nums):
    lengths = [1] * len(nums) # initiate lengths dp array as all 1's (since each nums[i] can be a subsequence on its own)
    counts = [1] * len(nums) # initiate counts dp array as all 1's (since each nums[i] is a subsequence on its own, i.e. [nums[i]])

    for j in range(len(nums)): # outer for-loop (j will be always be on the right side of i)
        for i in range(j): # inner nested for-loop; i iterates through all numbers before j
            if nums[i] < nums[j]: # we want nums[i] < nums[j] -> increasing subsequence
                if lengths[i] + 1 > lengths[j]: # this means we found a longer subsequence that ends at j compared to the subsequence ending at i 
                    lengths[j] = lengths[i] + 1 # we update length of subsequence ending at j with the number at i to get the greater length for lengths[j]
                    counts[j] = counts[i] # the count of LISs at j = count of LISs at i (since subsequence ending at j is an extension of subsequence ending at i)
                elif lengths[i] + 1 == lengths[j]: # this means we can extend every LIS ending at i with element at j to create new longest increasing subsequences ending at j
                    counts[j] += counts[i] # we add counts[i] into counts[j] so the updated counts[j] includes all LISs up till nums
    
    max_len = max(lengths) # max possible length of LISs
    count_of_max_LSIs = 0 # return value; no. of LSIs with the max possible length

    for i, length in enumerate(lengths):
        if length == max_len: # if length of current nums[i] = the max possible length,
            count_of_max_LSIs += counts[i] # update the no. of LSIs with max possible length with the count of LSIs at i
    
    return count_of_max_LSIs