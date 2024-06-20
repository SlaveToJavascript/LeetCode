# https://leetcode.com/problems/non-overlapping-intervals/description/
# MEDIUM
# intervalslc, #435

# GIVEN:
    # an array of intervals, intervals, where intervals[i] = [start_i, end_i]

# TASK:
    # return the minimum no. of intervals you need to remove to make the rest of the intervals non-overlapping

# EXAMPLES:
    # Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    # Output: 1
    # Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

    # Input: intervals = [[1,2],[1,2],[1,2]]
    # Output: 2
    # Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

    # Input: intervals = [[1,2],[2,3]]
    # Output: 0
    # Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# Sort the intervals by their start times
# Get the end times of previous interval
# Whenever there is an overlap between current and previous interval, we keep the interval with the earlier ending time
    # an interval with the lower ending time is less likely to overlap with other intervals behind
    # since we just need to return the count of intervals deleted and don't need to actually delete the intervals deleted from array, we can just increment deleted_count by 1 and set previous interval's end time to the minimum of the previous interval's end time and current interval's end time
# If there is no overlap, we update the previous interval with the current interval
# Return the deleted_count

# TIME COMPLEXITY: O(n log n)
    # sorting takes O(n log n) time
# SPACE COMPLEXITY: O(n)
    # for the sort function

def eraseOverlapIntervals(intervals):
    intervals.sort()
    deleted_count = 0
    prev_end = intervals[0][1] # the ending time of the previous interval; we initialize it to the ending time of the 1st interval

    for start, end in intervals[1:]: # we start iterating from the 2nd interval
        if start >= prev_end: # if there is no overlap between current and prev intervals
            prev_end = end # update prev_end to the ending time of current interval
        else: # there is overlap between current and prev intervals
            deleted_count += 1 # increment deleted_count by 1
            prev_end = min(prev_end, end) # update prev_end to the ending time of the earliest interval that ends
    
    return deleted_count