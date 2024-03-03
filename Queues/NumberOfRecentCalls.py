# 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/description/
# EASY
# Tags: queuelc, designlc, leetcode75lc, lc75lc, #933

# GIVEN:
    # RecentCounter class which counts the number of recent requests within a certain time frame

# TASK:
    # Implement the RecentCounter class:
        # RecentCounter() Initializes the counter with zero recent requests
        # ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (incl. the new request)
            # Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t]

    # Note: It is guaranteed that every call to ping uses a strictly larger value of t than the previous call

# EXAMPLES:
    # Input
    # ["RecentCounter", "ping", "ping", "ping", "ping"]
    # [[], [1], [100], [3001], [3002]]
    # Output
    # [null, 1, 2, 3, 3]

    # Explanation
    # RecentCounter recentCounter = new RecentCounter();
    # recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
    # recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
    # recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
    # recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

###########################################################################################################

# ✅ ALGORITHM: QUEUE

# TIME COMPLEXITY: O(n)
    # popping from front of queue is O(n) as all other elements are shifted forward
    # worst case: all elements in queue are out of the 3000ms range
# SPACE COMPLEXITY: O(n)

class RecentCounter(object):
    def __init__(self):
        self.requests = [] # this is a queue

    def ping(self, t):
        self.requests.append(t)
        while self.requests[0] < t-3000: # while 1st request in the queue is out of range
            self.requests.pop(0) # remove it from range
        return len(self.requests)