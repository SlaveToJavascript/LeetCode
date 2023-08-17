# https://leetcode.com/problems/meeting-rooms-iii/
# HARD
# Tags: heaplc, minheaplc, intervalslc, #2402

# GIVEN:
    # an integer n
        # There are n rooms numbered from 0 to n - 1
    # a 2D integer array, meetings, where meetings[i] = [start_i, end_i)
        # start_i = starting time of meeting, end_i = ending time of meeting
        # All the values of start_i are unique
        # a meeting can end and another meeting can start at the same time

# TASK:
    # Meetings are allocated to rooms in the following manner:
        # Each meeting will take place in the unused room with the lowest number
        # If there are no available rooms, the meeting will be delayed until a room becomes free
            # The delayed meeting should have the same duration as the original meeting
        # When a room becomes unused, meetings that have an earlier original start time should be given the room
    # Return the number of the room that held the most meetings
    # If there are multiple rooms, return the room with the lowest number

# EXAMPLES:
    # Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
    # Output: 0
    # Explanation:
    # - At time 0, both rooms are not being used. The first meeting starts in room 0.
    # - At time 1, only room 1 is not being used. The second meeting starts in room 1.
    # - At time 2, both rooms are being used. The third meeting is delayed.
    # - At time 3, both rooms are being used. The fourth meeting is delayed.
    # - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
    # - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
    # Both rooms 0 and 1 held 2 meetings, so we return 0. 

    # Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    # Output: 1
    # Explanation:
    # - At time 1, all three rooms are not being used. The first meeting starts in room 0.
    # - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
    # - At time 3, only room 2 is not being used. The third meeting starts in room 2.
    # - At time 4, all three rooms are being used. The fourth meeting is delayed.
    # - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
    # - At time 6, all three rooms are being used. The fifth meeting is delayed.
    # - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
    # Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

###########################################################################################################

# ✅ ALGORITHM 1: TWO MIN-HEAPS
# Create an array numMeetings where numMeetings[i] = no. of meetings held in the ith room
# Create 2 min-heaps, busyHeap and availHeap
    # busyHeap tracks currently ongoing meetings
        # busyHeap[i] = [ end_time, room_no. ] of ith meeting
    # availHeap tracks rooms that are currently available
# Sort meetings array by start time
# For each meeting in meetings array:
    # check for any available rooms by checking if end time(s) of the previous meeting(s) (if any) is before the start time of current meeting
    # if yes, pop these meeting(s) from busyHeap and push their room(s) to availHeap
    # if availHeap is not empty (i.e. there are rooms available),
        # pop room with smallest no. from availHeap
        # push this room and current meeting's end time to busyHeap
    # else, if availHeap is empty (i.e. no rooms available),
        # pop the meeting with the earliest ending time from the busyHeap array
        # the latest possible start time of the current meeting = the end time of the earliest meeting that ends next; 
        # push the revised end time of our current meeting (accounting for delay) and the room of the meeting with the earliest ending time to busyHeap (i.e. now our delayed current meeting has started)
# in numMeetings, increment the no. of meetings held in the room assigned to our current meeting by 1
# return the smallest index of the max value in numMeetings

# TIME COMPLEXITY: O(n log n), where n = no. of meetings
    # meetings.sort() -> O(n log n)
    # for-while loop -> O(n * log n)
        # for loop = O(n)
        # within the for-loop we're basically just pushing and popping -> each push/pop operation is O(log n)
# SPACE COMPLEXITY: O(n), where n = no. of meetings
    # worst case: availHeap and busyHeap have length = n

from heapq import heappop, heappush, heapify

def mostBooked(n, meetings):
    numMeetings = [0] * n
    busyHeap = [] # for current in-progress meetings
    availHeap = [i for i in range(n)] # for available rooms (room numbers)
        # at the start, all rooms are avail -> we initiate availHeap with all the room no.s
    heapify(availHeap)
    
    meetings.sort()
    
    for start, end in meetings: # start and end time of current meeting
        while busyHeap and busyHeap[0][0] <= start: # check for any available rooms by checking if end time(s) of the previous meeting(s) (if any) is before the start time of current meeting
            e, r = heappop(busyHeap)
            heappush(availHeap, r) # pop these meeting(s) from busyHeap and push their room(s) to availHeap
        
        if availHeap: # if availHeap is not empty (i.e. there are rooms available),
            room = heappop(availHeap) # available room with smallest room no.
            heappush(busyHeap, [end, room]) # push room no. to busyHeap (this is the room assigned to current meeting) together with current meeting's end time
        else: # if there are no more empty rooms for the current meeting
            prev_end_time, room = heappop(busyHeap) # end time of the meeting that ends the earliest will be start time of our current meeting; room for that meeting will be current meeting's room
            heappush(busyHeap, (prev_end_time + end-start, room)) # the revised start time of current delayed meeting = end time of previous meeting that ended + duration of current meeting
        
        numMeetings[room] += 1 # increment the no. of meetings held in the room assigned to our current meeting by 1

    return numMeetings.index(max(numMeetings))