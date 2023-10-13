# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# EASY
# Tags: dplc, #746

# GIVEN:
    # integer array, cost, where cost[i] is the cost of ith step on a staircase
    # Once you pay the cost, you can either climb one or two steps
    # You can either start from step with index 0, or step with index 1
    # NOTE: top of floor is not represented by the last element of cost; the top floor is after last element of cost

# TASK:
    # Return the minimum cost to reach the top of the floor

# EXAMPLE:
    # Input: cost = [10,15,20]
    # Output: 15
    # Explanation: You will start at index 1.
    # - Pay 15 and climb two steps to reach the top.
    # The total cost is 15.

    # Input: cost = [1,100,1,1,1,100,1,1,100,1]
    # Output: 6
    # Explanation: You will start at index 0.
    # - Pay 1 and climb two steps to reach index 2.
    # - Pay 1 and climb two steps to reach index 4.
    # - Pay 1 and climb two steps to reach index 6.
    # - Pay 1 and climb one step to reach index 7.
    # - Pay 1 and climb two steps to reach index 9.
    # - Pay 1 and climb one step to reach the top.
    # The total cost is 6.

###########################################################################################################

# ✅ ALGORITHM 1: ITERATIVE DP (fill dp array backwards)
# Create an integer dp array where dp[i] is the min cost to climb from step i to the top floor
# essentially, the min cost to climb from nth floor to top of floor = minimum between (cost of nth floor + cost of next (n+1th) floor i.e. take 1 step) AND (cost of nth floor + cost of nextnext (n+2th) floor i.e. take 2 steps)
# since we can start from step 0 or 1, return the minimum between the 0th and 1st element of dp

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def minCostClimbingStairs(cost):
    dp = [0] * (len(cost) + 1) # +1 to represent the top floor (its cost is 0)
    cost.append(0) # additional 0 to represent the top floor so that len(cost) = len(dp)
    dp[-2] = cost[-2] # from the last step, you can only take 1 step (itself) to the top floor
    for i in range(len(dp)-3,-1,-1): # reverse iteration from the 2nd last step
        dp[i] = min(cost[i] + dp[i+1], cost[i] + dp[i+2]) # find min between taking 1 step from step i VS taking 2 steps from step i
    return min(dp[0], dp[1]) # since we can start from step 0 or step 1, choose to start from the step that requires the min cost

#==========================================================================================================

# ✅ ALGORITHM 1B: ITERATIVE DP (fill dp array from front to back)
# cost[i] is the cost of TAKING the ith step, not the cost of REACHING the ith step
    # i.e. when we reach the ith step, the cost incurred is 0
# dp[i] is the cost of REACHING the ith step
# dp[0] and dp[1] are initialized to 0 as we can start from either of these steps without incurring any cost
# For each step i from 2 to n+1 (n+1 is the destination step), the minimum cost dp[i] to reach that step is the minimum of:
    # cost to reach the previous (i-1)th step (which costs dp[i-1]) and then taking a single step (the i-1th step) to reach step i, which costs dp[i-1] + cost[i-1]
    # cost to reach the 2nd previous (i-2)th step (which costs dp[i-2]) and then taking a double step to reach step i, which costs dp[i-2] + cost[i-2]

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def minCostClimbingStairs(cost):
    dp = [0] * (len(cost)+1)

    # NOTE: dp[0] and dp[1] are initialized to 0 as we can start from either of these steps without incurring any cost
    for i in range(2, len(dp)):
        dp[i] = min(dp[i-1] + cost[i-1] , dp[i-2] + cost[i-2])
    
    return dp[-1] # the last element in dp is the min cost to reach the last step (destination)