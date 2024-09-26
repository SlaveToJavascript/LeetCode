# 1642. Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/
# MEDIUM
# Tags: heaplc, minheaplc, greedylc, #1642

# GIVEN:
    # an integer array, heights, representing the heights of buildings
    # some bricks
    # some ladders

# TASK:
    # You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
    # While moving from building i to building i+1 (0-indexed),
        # If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
        # If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
    # Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# EXAMPLES:
    # Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    # Output: 4
    # Explanation: Starting at building 0, you can follow these steps:
    # - Go to building 1 without using ladders nor bricks since 4 >= 2.
    # - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
    # - Go to building 3 without using ladders nor bricks since 7 >= 6.
    # - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
    # It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

    # Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
    # Output: 7

    # Input: heights = [14,3,19,3], bricks = 17, ladders = 0
    # Output: 3

###########################################################################################################

# ✅✅✅ ALGORITHM 1: MIN-HEAP (greedy) (use ladders first before using bricks)
# ! MAIN IDEA: use ladders for the largest gaps, and bricks for the smaller gaps (since ladders can be used for any gap sizes but bricks are limited)
# use a min heap to store any positive differences between consecutive heights (i.e. if a building is shorter than its next building, push the heigh difference to min-heap)
# ensure that the heap size is always less than or equal to the number of ladders available
# if the heap size exceeds the number of ladders, it means there are insufficient ladders available -> use bricks instead for the smallest gaps
    # when len(heap) > ladders, pop the smallest gap from the heap and use bricks to cover the gap
# if the number of bricks is insufficient, return the current index
# if we reach the end of the array, return the last index (all buildings can be reached)

# TIME COMPLEXITY: O(n log k)
    # n = len(heights)
    # k = ladders
    # O(n) for the for-loop, O(log k) for each heap operation (max. length of heap is k)
# SPACE COMPLEXITY: O(k)
    # O(k) for the heap (max. length of heap is k since we start popping from the heap when len(heap) > ladders)

from heapq import heappush, heappop

def furthestBuilding(heights, bricks, ladders):
    min_diffs_heap = []

    for i in range(1, len(heights)):
        diff = heights[i] = heights[i-1]
        if diff > 0: # current building is shorter than next building
            heappush(min_diffs_heap, diff)
        
        if len(min_diffs_heap) > ladders:
            bricks -= heappop(min_diffs_heap)
        
        if bricks < 0: # there were insufficient bricks to cover the current gap
            return i-1
    
    return len(heights) - 1 # if we reached this point, it means we finished the loop, which means we can reach all buildings

#==========================================================================================================

# ✅ ALGORITHM 2: MAX HEAP (greedy) (use bricks first before using ladders)
# ! MAIN IDEA: use bricks for the smallest gaps, and ladders for the larger gaps (since ladders can be used for any gap sizes but bricks are limited)
# use a max-heap to store any positive differences between consecutive heights (i.e. if a building is shorter than its next building, push the heigh difference to min-heap)

# TIME COMPLEXITY: O(n log n)
    # n = len(heights)
    # O(n) for the for-loop, O(log n) for each heap operation (max. length of heap is n)
# SPACE COMPLEXITY: O(n)
    # O(n) for the heap (max. length of heap is n)

from heapq import heappush, heappop

def furthestBuilding(heights, bricks, ladders):
    max_diffs_heap = []

    for i in range(1, len(heights)):
        diff = heights[i] = heights[i-1]
        if diff > 0:
            heappush(max_diffs_heap, -diff)
            bricks -= diff # use bricks for any positive gaps
        
        if bricks < 0: # if there were insufficient bricks for the current gap,
            bricks += -heappop(max_diffs_heap) # Reimburse bricks used by replacing it with a ladder
            ladders -= 1
            if ladders < 0: # if we don't have enough ladders left,
                return i-1 # return the last reachable building
    
    return len(heights) - 1 # if we reached this point, it means we finished the loop, which means we can reach all buildings