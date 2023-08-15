# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
# MEDIUM
# Tags: intervalslc, #452

# There are some spherical balloons taped onto a flat wall that represents the XY-plane
# The balloons are represented as a 2D integer array, points, where points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches between x_start and x_end (both inclusive)
# Arrows can be shot up directly vertically from different points along the x-axis
# A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end
# A shot arrow keeps traveling up infinitely, bursting any balloons in its path
# TODO: return the minimum number of arrows that must be shot to burst all balloons

# EXAMPLES:
    # Input: points = [[10,16],[2,8],[1,6],[7,12]]
    # Output: 2
    # Explanation: The balloons can be burst by 2 arrows:
    # - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    # - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

    # Input: points = [[1,2],[3,4],[5,6],[7,8]]
    # Output: 4
    # Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

    # Input: points = [[1,2],[2,3],[3,4],[4,5]]
    # Output: 2
    # Explanation: The balloons can be burst by 2 arrows:
    # - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
    # - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# Sort points array by x_end
    # why x_end? Because if we shoot the arrow at x_end of a balloon, it's more likely that this arrow will shoot the other balloons that overlap with this balloon
# Increase no. of arrows when the x_start of current balloon is greater than x_end of previous balloon -> i.e. no overlap (so we shoot a new arrow)
    # we also set previous x_end = current x_end if there is no overlap, since we're moving to the next balloon that hasn't been shot
# if got overlap, i.e. current x_start <= previous x_end, current balloon can be burst by previous arrow

def findMinArrowShots(points):
    points.sort(key=lambda x: x[1]) # sort points by increasing x_end

    arrows = 1
    prev_end = points[0][1] # initialize previous balloon as current balloon; we only need to track previous ends

    for start, end in points[1:]: # start iterating from 2nd balloon onwards
        if start > prev_end: # if current balloon does not overlap with previous balloon,
            arrows += 1
            prev_end = end # set previous balloon as current balloon, as we're moving to the next balloon that hasn't been shot
    
    return arrows