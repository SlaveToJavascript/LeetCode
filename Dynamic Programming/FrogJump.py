# https://leetcode.com/problems/frog-jump/description/
# HARD
# Tags: dplc, hashmaplc, #403

# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

# EXAMPLES:
    # Input: stones = [0,1,3,5,6,8,12,17]
    # Output: true
    # Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

    # Input: stones = [0,1,2,3,4,8,9,11]
    # Output: false
    # Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING
# MAIN IDEA: use hashmap to store the stones as keys
    # values = set of possible no. of jumps from a previous stone to get to current stone
    # e.g. for [0,1,3,5,6,8,12,17],
    # dp = {
    #     0: {0},   # we start jumping from stone 0 so we don't need any jumps to get to stone 0
    #     1: {1},   # to get to this stone, jump 1 step from stone 0
    #     3: {2},   # to get to this stone, jump 2 steps from stone 1
    #     5: {2},   # to get to this stone, jump 2 steps from stone 3
    #     6: {1,3},   # to get to this stone, jump 1 step from stone 5 OR jump 3 steps from stone 3
    #     8: {2,3},   # to get to this stone, jump 2 steps from stone 6 OR jump 3 steps from stone 5
    #     12: {4},   # to get to this stone, jump 4 steps from stone 8
    #     17: {5}    # to get to to this stone, jump 5 steps from stone 12
    # }
# Iterate through each stone in stones, and for each stone, iterate through the range of allowed jumps (k-1, k, k+1)
# If there is a potential stone (destination) we can land on for the current no. of jumps, add that no. of jumps to the dp[destination] set

# TIME COMPLEXITY: O(n^2)
    # n = len(stones)
    # for the nested for-loop
    # worst case: for each stone, we iterate over all the other stones to check the possible jumps
# SPACE COMPLEXITY: O(n)
    # for dictionary

def canCross(stones):
    dp = {stone: set() for stone in stones}
    dp[0].add(0) # it takes 0 jumps to get to our current starting position

    for i in range(len(stones)): # for each stone in stones,
        for jump in dp[stones[i]]: # for each possible no. of jumps taken to get to this stone,
            for jumps in range(jump-1, jump+2): # possible no. of jumps to get from this stone to another stone is jump-1, jump, jump+1
                if jumps > 0 and stones[i] + jumps in dp: # if the no. of jumps taken > 0 and there is a valid destination we can land on in stones with this no. of jumps taken,
                    dp[stones[i] + jumps].add(jumps) # add this no. of jumps to the destination
    
    return len(dp[stones[-1]]) > 0 # if the set of possible no. of jumps taken to get to destination (the last stone) is > 0, it means we are able to reach this last destination stone -> return True