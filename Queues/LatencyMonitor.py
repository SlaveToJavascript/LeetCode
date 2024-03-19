# GOOGLE TECHNICAL PHONE SCREEN INTERVIEW QUESTION
# 7 August 2023
# Tags: queuelc, designlc, google, interviewlc

# PART 1:
# Create a program that measures server latency periodically
# The program receives one latency (ping) value at a time and after each value is received, calculates the average latency for the latest K values

# PART 2:
# Server may have latency spikes and we want the average latency to be tolerant by only measuring 95th percentile of values.
# In other words, we ignore the top X values (where X is 5% of K) in the average.

# EXAMPLES:
    # K = 5 (Note K should have been 40 to make X = 2, setting it to 5 for brevity of the example.)
    # X = 2
    # For the window from previous example (60, 70, 50, 100, 10), the largest 2 values are 100 and 70.

    # Another example is (70, 70, 50, 100, 10), the largest 2 values are still 100 and 70, note there is another 70 that should be included in the average.

###########################################################################################################

# ✅ ALGORITHM: QUEUE

# PART 1
class LatencyMonitor:
    def __init__(self, k):
        self.k = k # no. of latest values to consider for averaging
        self.q = [] # queue of ping values

    def add_ping(self, latency):
        self.q.append(latency) # add new ping value to queue
        if len(self.values) > self.k:
            self.values.pop(0) # Ensure we only keep the latest k values

    def get_avg_latency(self):
        # Calculate the average of the latest k latency values
        if not self.values:
            return 0  # Return 0 if there are no latency values
        return sum(self.values) / len(self.values)

# PART 2
# Add this new function to LatencyMonitor class:
def get_95th_percentile_avg(self):
    num_vals_to_ignore = max(1, round(0.05 * len(self.values))) # no. of values from the top (i.e. 5%) to ignore
        # "0.05 * len(self.values)" calculates 5% of the current no. of ping values stored in self.q
        # round() rounds the calculation to the nearest whole number
        # max(1, ...) ensures that at least 1 value is ignored (still ignore at least the single highest value when calculating the 95th percentile average)
    self.q.sort()
    self.q = self.q[:-num_vals_to_ignore] # Remove the top 5% of values to calculate the 95th percentile average

    if self.q:
        average = sum(self.q) / len(self.q)
    else:
        average = 0
    
    return average