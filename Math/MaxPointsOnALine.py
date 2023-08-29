# https://leetcode.com/problems/max-points-on-a-line/
# HARD
# Tags: mathlc, hashmaplc, #149

# GIVEN:
    # an array of points where points[i] = [xi, yi] represents a point on the X-Y plane

# TASK:
    # return the maximum number of points that lie on the same straight line

# EXAMPLES:
    # Input: points = [[1,1],[2,2],[3,3]]
    # Output: 3

    # Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # Output: 4

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Go through each pair of points to get the gradient of the 2 points, then iterate through every other point to find out if this point is on the same line as the other 2 points

# TIME COMPLEXITY: O(n^3) ❌

#==========================================================================================================

# ✅ ALGORITHM 2: HASHMAP
# Outer for-loop iterates through each point (this is called the pivot point)
# Inner for-loop iterates through every other point and gets the gradients between this point and pivot point
# Store this gradient in the hashmap, with key = gradient, and value = no. of points on a line with this gradient
    # hashmap[i] = { gradient : no. of points on a line with this gradient }
# For points on a vertical line, whose gradient is undefined (because you're dividing by 0), we store in the hashmap with gradient = infinity
# NOTE: each time the outer loop iterates to another pivot point, the hashmap is emptied as we are now finding the gradients between every other point and a new pivot point
    # therefore it's necessary to update max result every time for every pair
# update the result by getting the max no. of points on a line with a particular gradient + 1
    # the +1 is to include the pivot point itself, since in hashmap we only store the counts of the non-pivot points when iterating through them

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)

from collections import defaultdict

def maxPoints(points):
    # 1. For each pt determine if it lies on the longest line
    # 2. Count all pts with same slope
    # 3. Update result with max
    
    result = 1 # we're guaranteed to have at least 1 point, so minimum answer = 1
    hashmap = defaultdict(int)

    for i in range(len(points)): # outer loop where points[i] is the pivot point
        x1, y1 = points[i]
        hashmap.clear() # each time we use a new pivot point, hashmap is emptied as we are now finding the gradients between every other point and this new pivot point
        for j in range(i+1, len(points)): # inner loop that iterates every other point that's not pivot point
            x2, y2 = points[j]
            if x1 == x2: # if the 2 points are on a vertical line, then the gradient is undefined (dividing by 0)
                gradient = float('inf') # manually set gradient to infinity
            else:
                gradient = (y2 - y1) / (x2 - x1) # gradient formula
            hashmap[gradient] += 1 # add this point (i.e. the non-pivot point) to hashmap for this gradient
            result = max(result, hashmap[gradient]+1) # +1 to include the pivot point itself
    
    return result