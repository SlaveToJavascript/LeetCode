# https://leetcode.com/problems/candy/description
# HARD
# Tags: greedylc, #135

# There are n children standing in a line
# Each child is assigned a rating value given in the integer array ratings
# You are giving candies to these children subjected to the following requirements:
    # Each child must have at least 1 candy
    # Children with a higher rating get more candies than their neighbors
# TODO: Return the minimum number of candies you need to have to distribute the candies to the children

# EXAMPLES:
    # Input: ratings = [1,0,2]
    # Output: 5
    # Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

    # Input: ratings = [1,2,2]
    # Output: 4
    # Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    # The third child gets 1 candy because it satisfies the above two conditions.

###########################################################################################################

# ✅ ALGORITHM 1: COMPARE LEFT NEIGHBOR, COMPARE RIGHT NEIGHBOR, GET MAXIMUM (not space optimized)
# STEPS:
    # Initiate 1 candy for each child
    # CHECK LEFT NEIGHBOR: Go from left to right and for each child, if it has a higher rating than its left neighbor, give this child 1 more candy than its left neighbor
    # CHECK RIGHT NEIGHBOR: Go from right to left and for each child, if it has a higher rating than its right neighbor, give this child 1 more candy than its right neighbor
    # The final no. of candies to give each child is the maximum of the values from CHECK LEFT NEIGHBOR vs CHECK RIGHT NEIGHBOR
    # Return the sum of the resulting array of candies given to each child

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def candy(ratings):
    l_to_r = [1] * len(ratings)
    r_to_l = [1] * len(ratings)

    # check left neighbor
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            l_to_r[i] = l_to_r[i-1] + 1
    
    # check right neighbor
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            r_to_l[i] = r_to_l[i+1] + 1
    
    # get max of the above 2
    for i in range(len(r_to_l)):
        r_to_l[i] = max(r_to_l[i], l_to_r[i])
    
    return sum(r_to_l)

#==========================================================================================================

# ✅ ALGORITHM 2: COMPARE LEFT NEIGHBOR, COMPARE RIGHT NEIGHBOR, GET MAXIMUM (not space optimized)
# Same as above, except we use 1 array instead of 2

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def candy(ratings):
    result = [1] * len(ratings)

    # check left neighbor
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            result[i] = result[i-1] + 1
    
    # check right neighbor
    for i in range(len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            result[i] = max(result[i], result[i+1] + 1) # get max of check left vs right neighbor
    
    return sum(result)