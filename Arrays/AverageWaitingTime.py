# 1701. Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/
# MEDIUM
# Tags: simulationlc, arraylc, #1701

# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arriva_i, time_i]:
    # arrival_i is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
    # time_i is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.
# Return the average waiting time of all customers

# EXAMPLES:
    # Input: customers = [[1,2],[2,5],[4,3]]
    # Output: 5.00000
    # Explanation:
    # 1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
    # 2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
    # 3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
    # So the average waiting time = (2 + 6 + 7) / 3 = 5.

    # Input: customers = [[5,2],[5,4],[10,3],[20,1]]
    # Output: 3.25000
    # Explanation:
    # 1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
    # 2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
    # 3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
    # 4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
    # So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.

###########################################################################################################

# ✅ ALGORITHM: SIMULATION

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def averageWaitingTime(customers):
    total_wait = 0 # total amount of time spent waiting by all customers
    curr_time = customers[0][0] # initialize current time to the time of arrival of the 1st customer
    for arrival, time_needed in customers:
        curr_time = max(curr_time, arrival) # if arrival time of the current customer is later than current time, then set current time to the arrival time of the customer
        total_wait += time_needed + (curr_time-arrival) # current wait time = time taken to cook for the current customer + duration between current customer's arrival and time when chef starts cooking for current customer
        curr_time += time_needed # curr_time here is updated to the time at which chef is done preparing current customer's order, which is also the time at which chef can start preparing NEXT customer's order
    
    return float(total_wait) / len(customers)