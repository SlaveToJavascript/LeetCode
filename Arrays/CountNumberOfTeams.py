# 1395. Count Number of Teams
# https://leetcode.com/problems/count-number-of-teams/
# MEDIUM
# Tags: arraylc, greedylc, dplc, #1395

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
    # Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    # A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# EXAMPLES:
    # Input: rating = [2,5,3,4,1]
    # Output: 3
    # Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

    # Input: rating = [2,1,3]
    # Output: 0
    # Explanation: We can't form any team given the conditions.

    # Input: rating = [1,2,3,4]
    # Output: 4

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING / GREEDY
# ! MAIN IDEA: iterate through all possible middle elements of any triplet in rating array, and check for no. of LOWER ratings on the LEFT and no. of HIGHER ratings on the RIGHT (to detect increasing subsequences), AND check for no. of HIGHER ratings on the LEFT and no. of LOWER ratings on the RIGHT (to detect decreasing subsequences)
# no. of increasing subsequences = left_lower * right_higher
# no. of decreasing subsequences = left_higher * right_lower
    # NOTE: why is it * and not +? Because given the numbers we can pick from (on the left and right), we are just picking combinations from the left and right -> there are left_lower/higher * right_higher/lower combinations we can form

# TIME COMPLEXITY: O(n^2)
    # iteration for middle element: O(n)
    # within each iteration (for middle element), 2 inner loops each take ~O(n) time -> TC = O(n^2) time
# SPACE COMPLEXITY: O(1)

def numTeams(rating):
    result = 0

    for m in range(1, len(rating)-1): # find every potential middle element (iterate from 2nd element, end at 2nd last element in rating)
        left_smaller = right_larger = 0
        
        for l in range(m): # check for smaller elements on the left of m
            if rating[l] < rating[m]:
                left_smaller += 1
        
        for r in range(m+1, len(rating)): # check for larger elements on the right of m
            if rating[r] > rating[m]:
                right_larger += 1
        
        result += left_smaller * right_larger # no. of increasing subsequences
    
        # since all elements in rating are unique, all numbers are either smaller or larger
        left_larger = m - left_smaller
        right_smaller = len(rating)-m-1 - right_larger
        result += left_larger * right_smaller # no. of decreasing subsequences
    
    return result