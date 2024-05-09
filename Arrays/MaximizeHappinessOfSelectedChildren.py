# 3075. Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/
# MEDIUM
# Tags: arraylc, sortlc, greedylc, #3075

# GIVEN:
    # an array, happiness, of length n
    # a positive integer, k

# TASK:
    # There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
    # In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
    # TODO: Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

# EXAMPLES:
    # Input: happiness = [1,2,3], k = 2
    # Output: 4
    # Explanation: We can pick 2 children in the following way:
    # - Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
    # - Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
    # The sum of the happiness values of the selected children is 3 + 1 = 4.

    # Input: happiness = [1,1,1,1], k = 2
    # Output: 1
    # Explanation: We can pick 2 children in the following way:
    # - Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
    # - Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
    # The sum of the happiness values of the selected children is 1 + 0 = 1.

    # Input: happiness = [2,3,4,5], k = 1
    # Output: 5
    # Explanation: We can pick 1 child in the following way:
    # - Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
    # The sum of the happiness values of the selected children is 5.

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# Greedy: on each turn, always select child with highest happiness value, since the objective is to maximize result

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)
    # sort() function takes O(n) space

def maximumHappinessSum(happiness, k):
    result = 0 # return value
    happiness.sort()
    
    turns = 0 # keep track of no. of turns so at each turn, decrease remaining happiness values by 1
    for _ in range(k):
        if happiness:
            max_num = happiness.pop()
            result += max_num - turns if max_num-turns > 0 else 0
            turns += 1
    
    return result