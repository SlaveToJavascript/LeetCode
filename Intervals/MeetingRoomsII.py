# https://leetcode.com/problems/meeting-rooms-ii/
# MEDIUM
# Tags: intervalslc, #253

# GIVEN:
    # an array of meeting time intervals, intervals, where intervals[i] = [start_i, end_i]

# TASK:
    # return the minimum number of conference rooms required

# EXAMPLES:
    # Input: intervals = [[0,30],[5,10],[15,20]]
    # Output: 2

    # Input: intervals = [[7,10],[2,4]]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: COMPARE MEETINGS START AND END TIMES
# Keep track of the no. of rooms by comparing start and end times of each meeting
# Create 2 arrays, 1 for sorted start times and 1 for sorted end times
# Create 2 pointers, 1 for each array, to track current start and end times respectively
# If current start time is smaller than current end time, it means a new meeting started before the previous one ended -> no. of rooms occupied + 1
# if current end time is greater than/equals to current start time, it means a meeting ended before/at the same time the next meeting starts -> no. of rooms occupied - 1
# Return the max no. of rooms occupied at any point in time

# TIME COMPLEXITY: O(n log n)
    # n = length of intervals
    # for sorting starts and ends arrays
# SPACE COMPLEXITY: O(n)
    # for starts and ends arrays of length n each

def roomsNeeded(intervals):
    max_rooms = 0 # return value
    starts, ends = [], [] # all start and end times, each sorted

    for s, e in intervals:
        starts.append(s)
        ends.append(e)
    
    starts.sort()
    ends.sort()
    s, e = 0, 0 # s = pointer for starts array, e = pointer for ends array
    rooms = 0 # track no. of rooms needed at any point in time; this is not max_rooms (max_rooms tracks the max value of rooms)

    while s < len(starts): # s will definitely reach the end before e does since start times are always before end times
        if starts[s] < ends[e]: # if current start time is less than current end time -> new meeting started before previous one ended -> 1 additional room needed for this new meeting
            rooms += 1
            s += 1
        else: # if current end time is less than/equals to current start time -> a meeting ended before/at the same time the next meeting starts -> the room occupied by the ended meeting is now free
            rooms -= 1
            e += 1
        max_rooms = max(max_rooms, rooms)
    
    return max_rooms