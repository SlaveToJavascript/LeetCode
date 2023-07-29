# https://leetcode.com/problems/new-21-game/description/
# MEDIUM
# Tags: hashmaplc, #837

# Alice starts with 0 points and draws numbers while she has less than k points
# During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer
# Each draw is independent and the outcomes have equal probabilities
# Alice stops drawing numbers when she gets k or more points
# Return the probability that Alice has n or fewer points

# EXAMPLES:
    # Input: n = 10, k = 1, maxPts = 10
    # Output: 1.00000
    # Explanation: Alice gets a single card, then stops.

    # Input: n = 6, k = 1, maxPts = 10
    # Output: 0.60000
    # Explanation: Alice gets a single card, then stops.
    # In 6 out of 10 possibilities, she is at or below 6 points.

    # Input: n = 21, k = 17, maxPts = 10
    # Output: 0.73278

###########################################################################################################

# ❌ ALGORITHM 1: HASHMAP CACHING (TLE 👎)

# TIME COMPLEXITY: O(k * maxPoints)
    # base case: stop at k -> we have up to k subproblems
    # for each subproblem, we have to loop up to maxPts number of times

def new21Game(n, k, maxPts):
    cache = {}

    def getProbability(score): # return the probability that score <= n
        if score >= k: # stop drawing cards when score >= k
            return 1 if score <= n else 0
        
        if score in cache: # if the subproblem with this score has already been solved before, score would be in cache
            return cache[score]
    
        prob = 0 # initialize probability to 0
        for i in range(1, maxPts+1): # i = 1 to maxPts
            prob += getProbability(score + i) # i is the value we are drawing here
        
        cache[score] = prob / maxPts # since we are always gonna be branching maxPts no. of times, we can just take prob and divide it by maxPts to get the average
        return cache[score]
    
    return getProbability(0) # since our starting score = 0

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING (SLIDING WINDOW)
