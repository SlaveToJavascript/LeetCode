# https://leetcode.com/problems/merge-intervals/description/
# MEDIUM
# Tags: intervalslc, #56

# GIVEN:
    # an array of positive integers, intervals, where intervals[i] = [starti, endi]

# TASK:
    # merge all overlapping intervals
    # return an array of the non-overlapping intervals that cover all the intervals in the input

# EXAMPLES:
    # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    # Output: [[1,6],[8,10],[15,18]]
    # Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    # Input: intervals = [[1,4],[4,5]]
    # Output: [[1,5]]
    # Explanation: Intervals [1,4] and [4,5] are considered overlapping.

###########################################################################################################

# ✅ ALGORITHM: COMPARE WITH PREVIOUS INTERVAL
# Sort intervals array in increasing order of 1st element (i.e. element at 0th index)
# Iterate through intervals array
# for each interval, if current interval's start is less than/equal to previous interval's end, there is an overlap -> update end value of the merged interval as current interval's end time
# append to result array

# TIME COMPLEXITY: O(nlogn)
    # for sorting the array at the start
# SPACE COMPLEXITY: O(n)
    # for sort() function

def merge(intervals):
    intervals.sort() # sort by 1st element (at index 0) of each interval
    result = [intervals[0]] # add 1st interval to result first

    for s, e in intervals[1:]: # start iterating from 2nd interval in array
        prev_start, prev_end = result.pop() # pop previous interval from result to get prev start and end
        if s <= prev_end: # if current interval's start is less than/equal to prev interval's end,
            s = prev_start # start value of merged interval = start value of previous interval
            e = max(e, prev_end) # end value of merged interval = the greater end value between current VS previous interval
        else: # if no overlap
            result.append([prev_start, prev_end]) # add the popped interval back into result
        
        result.append([s, e]) # if overlap, [s,e] will be the merged array; if no overlap, [s,e] is the current array in iteration of intervals
    
    return result