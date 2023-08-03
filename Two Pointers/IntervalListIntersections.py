# https://leetcode.com/problems/interval-list-intersections/description/
# MEDIUM
# Tags: twopointerslc, #986

# GIVEN:
    # 2 lists of closed intervals, firstList and secondList, 
    # where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]
    # Each list of intervals is pairwise disjoint and in sorted order

# TASK:
    # Return the intersection of these two interval lists

# EXAMPLES:
    # Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    # Input: firstList = [[1,3],[5,9]], secondList = []
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# maintain 2 pointers, 1 for 1st array, 1 for 2nd array
# between 2 intervals, if the max start <= min end, then there is an overlap
    # the overlap intersection is [max_start, min_end]
# increment the pointer index for the array with the interval that has the min_end

# TIME COMPLEXITY: O(min(len(firstList), len(secondList)))
# SPACE COMPLEXITY: O(min(len(firstList), len(secondList)))
    # for the worst case where every interval intersects

def intervalIntersection(firstList, secondList):
    p1, p2 = 0, 0
    intersections = []

    while p1 < len(firstList) and p2 < len(secondList):
        s1, e1 = firstList[p1]
        s2, e2 = secondList[p2]
        
        maxStart = max(s1, s2)
        minEnd = min(e1, e2)
        
        if maxStart <= minEnd: # there is overlap
            intersections.append([maxStart, minEnd])
        
        if e1 == minEnd: # increment the pointer index for the array with the interval that has the min_end
            p1 += 1
        else:
            p2 += 1

    return intersections