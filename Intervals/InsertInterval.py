# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/
# MEDIUM
# Tags: intervalslc, blind75lc, #57

# GIVEN:
    # an array of non-overlapping intervals, intervals
        # intervals[i] = [start_i, end_i] represent the start and the end of the ith interval
        # intervals is sorted in ascending order by star_i
    # an interval, newInterval = [start, end] that represents the start and end of another interval

# TASK:
    # Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary)
    # Return intervals after the insertion
    # NOTE: you don't need to modify intervals in-place. You can make a new array and return it.

# EXAMPLES:
    # Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    # Output: [[1,5],[6,9]]

    # Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    # Output: [[1,2],[3,10],[12,16]]
    # Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

###########################################################################################################

# ✅ ALGORITHM: CHECK FOR INTERVAL OVERLAPS WITH 3 CASES
# 3 POSSIBLE CASES encountered when iterating intervals array:
    # 1. entire newInterval comes before current interval (non-overlapping)
        # add newInterval to result first
        # add all remaining intervals to result (including current interval at current iteration)
        # return result
        # NOTE: don't need to continue iterating remaining intervals since we know there are no overlaps with newInterval and between any other intervals
    # 2. entire newInterval comes after current interval (non-overlapping)
        # add ONLY current interval to result
            # because there is no overlap between current interval and newInterval, but newInterval might still overlap with a later interval
            # so we don't add newInterval yet
    # 3. newInterval overlaps with current interval
        # update newInterval to become the merged interval
        # don't append updated newInterval yet, since it might possibly overlap with yet another interval encountered later

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def insert(intervals, newInterval):
    result = []
    
    for i in range(len(intervals)):
        s, e = intervals[i]
        
        # case 1: entire newInterval comes before current interval (non-overlapping)
        if newInterval[1] < s:
            result.append(newInterval) # add newInterval to result first
            # we know that all intervals from and including current interval onwards are non-overlapping -> add these intervals to array and return result (don't need to continue while loop)
            result += intervals[i:]
            return result
        
        # case 2: entire newInterval comes after current interval (non-overlapping)
        elif newInterval[0] > e:
            result.append(intervals[i])
            # don't append newInterval yet, since it might possibly overlap with another interval encountered in a later iteration
        
        # case 3: newInterval overlaps with current interval!
        else:
            newInterval = [min(newInterval[0], s), max(newInterval[1], e)] # update newInterval to become the merged interval
            # don't append updated newInterval yet, since it might possibly overlap with another interval encountered later
    
    result.append(newInterval)
    return result