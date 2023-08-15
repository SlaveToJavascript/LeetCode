# https://leetcode.com/problems/koko-eating-bananas/description/
# MEDIUM
# Tags: binarysearchlc, #875

# There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# TODO: Return the minimum integer k such that she can eat all the bananas within h hours.

# EXAMPLES:
    # Input: piles = [3,6,7,11], h = 8
    # Output: 4

    # Input: piles = [30,11,23,4,20], h = 5
    # Output: 30

    # Input: piles = [30,11,23,4,20], h = 6
    # Output: 23

###########################################################################################################

# ✅ ALGORITHM: BINARY SEARCH
# The search boundary is between 1 and max(piles)
    # we can't eat 0 or less bananas because in that case we're not eating anything
    # we're eating no more than 1 pile of bananas per hour -> max speed is max(piles) bananas per hour
# since we are finding the minimum no. of bananas to be eaten per hour, we continue the binary search until lower bound = upper bound

# TIME COMPLEXITY: O(n log max(piles))
    # since the search boundary is 1 to max(piles) -> O(log max(piles)) time
    # for each binary search operation, we have to iterate piles once to calculate hours needed -> O(n) for each operation
    # total = O(n log max(piles))
# SPACE COMPLEXITY: O(1)

import math

def minEatingSpeed(piles, h):
    l, r = 1, max(piles) # min eaten per hour = 1, max eaten per hour = max(piles)

    while l < r:
        mid = (l+r) // 2
        
        hours_needed = 0 # no. of hours needed to finish all bananas if we eat mid bananas per hour
        for pile in piles:
            hours_needed += math.ceil(pile / mid) # ceil() rounds up the value of pile/mid
        
        if hours_needed <= h: # can finish eating all bananas at speed of k bananas per hour
            r = mid # search for a smaller k
        else: # cannot finish eating all bananas -> need a higher speed
            l = mid + 1 # search for higher k

    # at this point, l = r
    return l