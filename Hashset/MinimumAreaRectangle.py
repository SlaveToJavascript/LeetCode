# 939. Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/description/
# MEDIUM
# Tags: setlc, arraylc, #939

# GIVEN:
    # an array of points in the X-Y plane, points, where points[i] = [xi, yi]

# TASK:
    # Return the min. area of a rectangle formed from these points, with sides parallel to the X and Y axes
    # If there is not any such rectangle, return 0

# EXAMPLES:
    # Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    # Output: 4

    # Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    # Output: 2

###########################################################################################################

# ✅ ALGORITHM: HASH SET
    # https://youtu.be/IQKIm0wEu4w?si=ISyF4dHV892tQ5md
# Assume the following rectangle:
    # (x1,y1)   (x2,y1)
    #    *         *

    #    *         *
    # (x1,y2)   (x2,y2)
# if we have the coords of 2 diagonal points (x1,y1) and (x2,y2), we can calculate the coords of the other 2 points that form a rectangle and see if these 2 calculated points exist in the set
# if they do, a rectangle can be formed from (x1,y1), (x2,y2) and the 2 other calculated points -> calculate the area of the rectangle
# if they don't, add (x1,y1) to the set and continue

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)

def minAreaRect(points):
    points_set = set()
    min_size = float('inf')

    for x1, y1 in points:
        for x2, y2 in points_set: # we are looking for (x2,y2) as being the diagonal point to (x1,y1)
            if (x1,y2) in points_set and (x2,y1) in points_set: # if the 2 other points are found,
                min_size = min(min_size, abs(x1-x2) * abs(y1-y2)) # check if area of current rectangle is the min. size
        points_set.add((x1,y1)) # add (x1,y1) to the set so that it can be used by future searches
    
    return min_size if min_size != float('inf') else 0 # if no rectangle can be formed, return 0