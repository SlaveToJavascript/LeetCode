# 256. Paint House
# https://leetcode.com/problems/paint-house/
# MEDIUM
# Tags: dplc, premiumlc, #256

# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
    # For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.

# EXAMPLES:
    # Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
    # Output: 10
    # Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
    # Minimum cost: 2 + 5 + 3 = 10.

    # Input: costs = [[7,6,2]]
    # Output: 2

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING
# starting from the 2nd house (i.e. 1st-indexed house), tabulate the costs of painting each house with each color by modifying the costs array
# so costs[i][j] = total cost of painting all houses up to and including house i (where house i is painted with color j)
    # i.e. for the 2nd house, if I want to paint it with the 0th color (red), I can only paint the 1st house with the 1st or 2nd colors
    # cost of painting all houses up until i'th house (and painting 2nd house with color j) = costs[i][j] + min(costs[i-1][x], costs[i-1][y]), where x and y refer to the other 2 colors that are not j

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def minCost(costs):
    n = len(costs)
        
    for i in range(1, n): # start from the 2nd house
        costs[i][0] += min(costs[i-1][1], costs[i-1][2]) # cost of painting current house red = total cost of painting all houses up till and including house i-1 + minimum of (cost of painting house i blue, cost of painting house i green)
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][1], costs[i-1][0])
    
    return min(costs[-1])