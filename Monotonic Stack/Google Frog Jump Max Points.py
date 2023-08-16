# https://leetcode.com/discuss/interview-question/3276093/Google-Onsite-Interview-Problem
# Tags: dplc, google, stacklc, motononicstacklc, monotoniclc

# You are a frog
# Your starting position is index = -1
# points[i] is the no. of points at the ith position
# you need to jump from starting position to end (last element of array) and collect maximum points
# if you jump from index i to j, you will gain (j - i) * points[j] points
# return the maximum collected points

# EXAMPLE:
    # points = [1, 5, 2, 3, 1]
    # Starting from index -1, I jump to element 5 at index 1 -> (1-(-1)) * 5 = 10
    # Then I jump to element 3 at index 3 -> (3-1) * 3 = 6
    # Then I jump to element 1 at index 4 -> (4-3) * 1 = 1
    # Return value: 2*5 + 2*3 + 1*1 = 17

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING
# for any position i, the max points we can collect at that position will be:
    # dp[i] = max(dp[j] + (i-j) * points[i]) for all j from -1 to i-1
        # j is the index where we jump to i from

# TIME COMPLEXITY: O(n^2)
    # n = len(points)
    # for each element in the array, we are iterating over all previous elements to compute max points collected at that position
# SPACE COMPLEXITY: O(n)
    # for dp array of size n

def frogJump(points):
    dp = [0] * len(points) # dp[i] = max points we can collect at position i
    dp[0] = 1 * points[0] # jump from index -1 to index 0

    for i in range(1, len(points)):
        dp[i] = (i-(-1)) * points[i] # we first initiate dp[i] with the points collected if we jump from -1 to i directly
        for j in range(i): # we jump from j to i, j = 0 to i-1
            dp[i] = max(dp[i], dp[j] + (i-j) * points[i])
    
    return dp[-1]

#==========================================================================================================

# ✅ ALGORITHM 2: MONOTONIC STACK
# If current index is i and the next index is j, moving to next index adds points[j] to score
# From j, moving to j+1 index adds another points[j+1] to score -> total score = points[j] + points[j+1]
# However, from i, moving to j+1 index directly adds 2 * points[j+1] to score
    # therefore it makes sense to jump from i to j+1 directly if points[j+1] > points[j]
# Thus, at i, for any next index j, we should choose an index k where points[k] > points[j]
    # -> final set of jumps would contain set of elements with values in decreasing order
    # as we always choose to jump to the next greater element instead of smaller element
# STEPS:
    # Create a stack, then iterate points array
    # For each element in points, pop all elements in stack that are less than that element
    # then, finally insert that element into stack, together with its index in points array
    # calculate answer using the points and indexes in stack

# TIME COMPLEXITY: O(n)
    # n = size of points
# SPACE COMPLEXITY: O(n)
    # for stack of max size n

def frogJump(points):
    stack = [] # stack[i] = (points, index)

    for i, point in enumerate(points): # for each element in points,
        while stack and point > stack[-1][0]: # if current points is greater than points @ top of stack,
            stack.pop() # pop from top of stack
        stack.append((point, i)) # add current points and its index to stack
    
    result = 0 # return value
    prev_idx = -1 # we start jumping from index -1
    for point, idx in stack: # for each landing point in stack,
        result += (idx-prev_idx) * point # we add up the points
        prev_idx = idx # current index is now the previous index (where we jump from)
    
    return result