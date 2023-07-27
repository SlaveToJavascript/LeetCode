# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/description/
# MEDIUM

# GIVEN:
    # positive integer array, buses, where buses[i] = departure time of ith bus
    # positive integer array, passengers, where passengers[j] = arrival time of the jth passenger
    # positive integer, capacity, which is the max no. of people that can get on each bus

# TASK:
    # Return the latest time you may arrive at the bus station to catch a bus
    # NOTE: You cannot arrive at the same time as any other passenger
    # A passenger can only board the bus if:
        # 1) Their arrival time is <= bus departure time
        # 2) There is still capacity to get onto the bus

# EXAMPLES:
    # Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
    # Output: 16
    # Explanation: Suppose you arrive at time 16.
    # At time 10, the first bus departs with the 0th passenger. 
    # At time 20, the second bus departs with you and the 1st passenger.
    # Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1st passenger to catch the bus.

    # Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
    # Output: 20
    # Explanation: Suppose you arrive at time 20.
    # At time 10, the first bus departs with the 3rd passenger. 
    # At time 20, the second bus departs with the 5th and 1st passengers.
    # At time 30, the third bus departs with the 0th passenger and you.
    # Notice if you had arrived any later, then the 6th passenger would have taken your seat on the third bus.

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS (time complexity not maximized – reading from array instead of set)
# Sort both arrays
# 2 pointers, 1 for buses array, 1 for passengers
# Iterate buses array, shifting both pointers depending on whether or not the passengers can board buses
    # while iterating, also track the capacity that was taken up while passengers were boarding
# After the iteration, buses pointer should point to the bus that was last to leave, while the capacity tracked refers to the remaining capacity on that bus
# Now, if there are still remaining capacity on that bus, I just need to arrive at the same time it leaves
    # however we can't just return the last bus's departure time directly, as there may be existing passengers who are arriving at that time as well (e.g. buses=[2], passengers=[2], capacity=2)
# if there are no more seats, I need to arrive before the last passenger who got onto the bus

# TIME COMPLEXITY: O(n log n)
    # Python's sort function requires O(n log n) runtime
# SPACE COMPLEXITY: O(1)

def latestTimeCatchTheBus(buses, passengers, capacity):
    # sort the 2 arrays for easier iteration
    buses.sort()
    passengers.sort()

    b, p = 0 # b is the pointer for buses, and p is the pointer for passengers
    
    cap = capacity # cap = current capcity for current buses[b]; initialize for 1st bus
    while b < len(buses): # while index b is within buses array
        if p < len(passengers) and passengers[p] <= buses[b] and cap > 0: # if index p is within passengers array, AND, current passengers[p]'s arrival time is before or at buses[b]'s departure time, AND, there is still capacity left on this bus
            p += 1 # if all 3 conditions above are satisfied, current passenger boards -> p moves to next passenger
            cap -= 1 # capacity on current bus decreases by 1
        else: # current passenger p cannot board current bus b
            b += 1 # go to the next bus
            if b < len(buses): cap = capacity # if next bus b+1 is within buses array, reset capacity
    
    if cap > 0: # if there are still remaining capacity on that bus, 
        my_arrival_time = buses[b-1] # I just need to arrive the same time the last bus leaves
            # NOTE: last bus is b-1 since we did b+1 in the last step in the while loop before loop ends
    else: # if there are no more seats,
        my_arrival_time = passengers[p-1] # I need to find the arrival time of the last passenger who boarded the last bus, and arrive before that passenger
            # NOTE: p-1 is the last passenger who boarded the last bus, since we did p+1 in the last loop
    
    while my_arrival_time in passengers: # if I arrive at the same time as any other passenger,
        my_arrival_time -= 1 # I have to arrive at an earlier time, since I cannot arrive at the same time as any other passenger
    
    return my_arrival_time

#==========================================================================================================

# ✅ ALGORITHM 1A: TWO POINTERS (time complexity optimized – reading from set instead of array)
# This solution is exact same as the above, except we convert passengers array into a set at the last step so we are reading from a set instead of array to check for my_arrival_time in passengers
    # => time complexity slightly improves

# TIME COMPLEXITY: O(n log n)
    # Python's sort function requires O(n log n) runtime
# SPACE COMPLEXITY: O(n)

def latestTimeCatchTheBus(buses, passengers, capacity):
    # sort the 2 arrays for easier iteration
    buses.sort()
    passengers.sort()

    b, p = 0 # b is the pointer for buses, and p is the pointer for passengers
    
    cap = capacity # cap = current capcity for current buses[b]; initialize for 1st bus
    while b < len(buses): # while index b is within buses array
        if p < len(passengers) and passengers[p] <= buses[b] and cap > 0: # if index p is within passengers array, AND, current passengers[p]'s arrival time is before or at buses[b]'s departure time, AND, there is still capacity left on this bus
            p += 1 # if all 3 conditions above are satisfied, current passenger boards -> p moves to next passenger
            cap -= 1 # capacity on current bus decreases by 1
        else: # current passenger p cannot board current bus b
            b += 1 # go to the next bus
            if b < len(buses): cap = capacity # if next bus b+1 is within buses array, reset capacity
    
    if cap > 0: # if there are still remaining capacity on that bus, 
        my_arrival_time = buses[b-1] # I just need to arrive the same time the last bus leaves
            # NOTE: last bus is b-1 since we did b+1 in the last step in the while loop before loop ends
    else: # if there are no more seats,
        my_arrival_time = passengers[p-1] # I need to find the arrival time of the last passenger who boarded the last bus, and arrive before that passenger
            # NOTE: p-1 is the last passenger who boarded the last bus, since we did p+1 in the last loop
    
    passengers = set(passengers) # *** THIS IS THE LINE THAT IS MODIFIED FOR OPTIMIZATION ***
    while my_arrival_time in passengers: # if I arrive at the same time as any other passenger,
        my_arrival_time -= 1 # I have to arrive at an earlier time, since I cannot arrive at the same time as any other passenger
    
    return my_arrival_time

#==========================================================================================================

# ✅ ALGORITHM 1B: TWO POINTERS (slightly cleaner code)
# This solution is same as above, except that instead of using a while-loop + 2 pointers, we use a for-while-loop + 1 pointer

# TIME COMPLEXITY: O(n log n)
    # Python's sort function requires O(n log n) runtime
# SPACE COMPLEXITY: O(n)

def latestTimeCatchTheBus(buses, passengers, capacity):
    # sort the 2 arrays for easier iteration
    buses.sort()
    passengers.sort()

    p = 0 # p is the pointer for passengers
    
    cap = capacity # cap = current capcity for current buses[b]; initialize for 1st bus
    
    # *** THE BELOW for-while LOOP IS THE SLIGHT MODIFICATION FROM SOLUTION ABOVE ***
    for depart_time in buses:
        cap = capacity
        while p < len(passengers) and passengers[p] <= depart_time and cap > 0: # p can board this bus
            p += 1
            cap -= 1
    
    if cap > 0: # if there are still remaining capacity on that bus, 
        my_arrival_time = depart_time # I just need to arrive the same time the last bus leaves
            # NOTE: last bus is b-1 since we did b+1 in the last step in the while loop before loop ends
    else: # if there are no more seats,
        my_arrival_time = passengers[p-1] # I need to find the arrival time of the last passenger who boarded the last bus, and arrive before that passenger
            # NOTE: p-1 is the last passenger who boarded the last bus, since we did p+1 in the last loop
    
    passengers = set(passengers) # *** THIS IS THE LINE THAT IS MODIFIED FOR OPTIMIZATION ***
    while my_arrival_time in passengers: # if I arrive at the same time as any other passenger,
        my_arrival_time -= 1 # I have to arrive at an earlier time, since I cannot arrive at the same time as any other passenger
    
    return my_arrival_time