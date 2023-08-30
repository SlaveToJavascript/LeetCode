# https://leetcode.com/problems/gas-station/description/
# MEDIUM
# Tags: arraylc, greedylc, #134

# There are n gas stations along a circular route, where the amount of gas at the ith station = gas[i]
# it costs cost[i] of gas to travel from the ith station to the next (i + 1)th station
# You begin the journey with an empty tank at one of the gas stations.
# Given 2 integer arrays gas and cost, return the starting gas station, i, if you can travel around the circuit once in the clockwise direction, otherwise return -1
# If there exists a solution, it is guaranteed to be unique

# EXAMPLES:
    # Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    # Output: 3
    # Explanation:
    # Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    # Travel to station 4. Your tank = 4 - 1 + 5 = 8
    # Travel to station 0. Your tank = 8 - 2 + 1 = 7
    # Travel to station 1. Your tank = 7 - 3 + 2 = 6
    # Travel to station 2. Your tank = 6 - 4 + 3 = 5
    # Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    # Therefore, return 3 as the starting index.

    # Input: gas = [2,3,4], cost = [3,4,3]
    # Output: -1
    # Explanation:
    # You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
    # Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    # Travel to station 0. Your tank = 4 - 3 + 2 = 3
    # Travel to station 1. Your tank = 3 - 3 + 3 = 3
    # You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
    # Therefore, you can't travel around the circuit once no matter where you start.

###########################################################################################################

# ✅ ALGORITHM 1: GREEDY
# For each gas station i, we can start from i if gas[i]-cost[i] > 0
# if sum(gas) < sum(cost), the nett +ve will be less than the nett -ve, so -1 should be returned (we cannot finish the full path back to start)
# else, if sum(gas) >= sum(cost), we can definitely finish the path and will not return -1
# therefore, if we start from a gas station i, we will definitely be able to make a full loop -> we don't have to loop back to the start of the array after reaching the end of the array!

def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost): # we will not be able to finish this path
        return -1
    
    total = 0 # nett result of gas[i]-cost[i]
    start = 0 # starting index (return value)
    
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0 # reset total
            start = i+1 # shift start to the next gas station i
    
    return start