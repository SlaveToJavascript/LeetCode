# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
# MEDIUM
# Tags: dplc, intervalslc, #646

# GIVEN:
    # n array of n pairs, pairs, where pairs[i] = [lefti, righti] and lefti < righti

# TASK:
    # A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c
    # A chain of pairs can be formed in this fashion
    # Return the length longest chain which can be formed
    # NOTE: You do not need to use up all the given intervals
        # You can select pairs in any order

# EXAMPLES:
    # Input: pairs = [[1,2],[2,3],[3,4]]
    # Output: 2
    # Explanation: The longest chain is [1,2] -> [3,4].

    # Input: pairs = [[1,2],[7,8],[4,5]]
    # Output: 3
    # Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

###########################################################################################################

# ✅ ALGORITHM 1: GREEDY
# sorting based on the 1st element (start) wouldn't be effective because the 2nd element of a selected pair might be large enough to prevent the addition of numerous additional pairs
    # e.g. [1, 10], [2, 4], [5, 8], [9, 11]
# so we sort based on the 2nd element (end)

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(1)

def findLongestChain(pairs):
    pairs.sort(key=lambda x:x[1]) # sort by end times
    prev_end = pairs[0][1] # initiate to the end time of the 1st pair in pairs
    result = 1 # return value; initiate to 1 for the 1st pair in pairs
    
    for start, end in pairs[1:]: # start iterating from the 2nd pair onwards
        if prev_end < start:
            result += 1
            prev_end = end # update prev_end if current pair is used in the chain
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING
# Same as Longest Increasing Subsequence
# Create integer array dp where each dp[i] = max possible length of the chain ending at i
# Initiate dp as an array of 1's, since each chain on its own is a chain of length 1

# TIME COMPLEXITY: O(n^2)
    # O(n log n) for sorting
    # O(n^2) for nested for loop
# SPACE COMPLEXITY: O(n)
    # for dp array

def findLongestChain(pairs):
    pairs.sort()
    dp = [1] * len(pairs)

    for j in range(len(pairs)):
        for i in range(j): # inner nested for-loop; i iterates through all pairs before j
            if pairs[i][1] < pairs[j][0]: # if previous end < current start
                dp[j] = max(dp[j], 1 + dp[i]) # max length of chain ending at j = max(existing length of chain ending at j, 1 + length of chain ending at i)
                    # 1 is for the pair ending at j
    
    return max(dp)