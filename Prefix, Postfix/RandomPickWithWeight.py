# https://leetcode.com/problems/random-pick-with-weight/
# MEDIUM
# Tags: prefixlc, binarysearchlc, #528

# GIVEN:
    # array of positive integers, w, where w[i] = weight of the ith index

# TASK:
    # implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it
    # The probability of picking an index i is w[i] / sum(w)
        # e.g. if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%)

# EXAMPLES:
    # Input
        # ["Solution","pickIndex"]
        # [[[1]],[]]
    # Output
        # [null,0]
    # Explanation
        # Solution solution = new Solution([1]);
        # solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

    # Input
        # ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
        # [[[1,3]],[],[],[],[],[]]
    # Output
        # [null,1,1,1,1,0]
    # Explanation
        # Solution solution = new Solution([1, 3]);
        # solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
        # solution.pickIndex(); // return 1
        # solution.pickIndex(); // return 1
        # solution.pickIndex(); // return 1
        # solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

        # Since this is a randomization problem, multiple answers are allowed.
        # All of the following outputs can be considered correct:
        # [null,1,1,1,1,0]
        # [null,1,1,1,1,1]
        # [null,1,1,1,0,0]
        # [null,1,1,1,0,1]
        # [null,1,0,1,0,0]
        # ......
        # and so on.

###########################################################################################################

# ❌ ALGORITHM 1: RANDOM.CHOICES() WEIGHTED PROBABILITIES (TLE)
# Python has a built-in function, random.choices(array, weights=[...], k=1) which selects k elements from array where the weight of each choice is given in weights

# TIME COMPLEXITY: O(n^2) 👎
    # for each of the n elements in self.w, we find self.w[i]/sum(self.w)
        # sum() is O(n) -> overall = O(n^2)

import random

class Solution(object):
    def __init__(self, w):
        self.w = w
        
    def pickIndex(self):
        return random.choices([i for i in range(len(self.w))], weights=[self.w[i]/sum(self.w) for i in range(len(self.w))])

#==========================================================================================================

# ✅ ALGORITHM 2: PREFIX SUMS + BINARY SEARCH