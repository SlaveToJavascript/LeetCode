# https://leetcode.com/problems/sliding-window-maximum/description/
# HARD
# Tags: monotonicqueuelc, monotoniclc, slidingwindowlc, #239

# GIVEN:
    # an array of integers, nums
    # positive integer, k, where k is the size of the sliding window
        # sliding window is moving from left to right
        # each time the sliding window moves right by one position
        # You can only see the k numbers in the window

# TASK:
    # Return an array of the max numbers from each sliding window

# EXAMPLES:
    # Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    # Output: [3,3,5,5,6,7]
    # Explanation: 
    # Window position                Max
    # ---------------               -----
    # [1  3  -1] -3  5  3  6  7       3
    #  1 [3  -1  -3] 5  3  6  7       3
    #  1  3 [-1  -3  5] 3  6  7       5
    #  1  3  -1 [-3  5  3] 6  7       5
    #  1  3  -1  -3 [5  3  6] 7       6
    #  1  3  -1  -3  5 [3  6  7]      7

    # Input: nums = [1], k = 1
    # Output: [1]

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE WITH TWO POINTERS
# l and r pointers pointing to the starting and ending element of the window
# above is achieved with outer for-loop that iterates nums array
# Inner for-loop that iterates within each sliding window of length k to geet max no. within the window
# add the max no. for each window into an array, and return the array

# TIME COMPLEXITY: O(n*k)
    # outer for-loop that iterates across nums: O(n)
    # inner for-loop that iterates across window of length k: O(k)
# SPACE COMPLEXITY: O(n)
    # for the result array
    # for a nums array of length n, there will be approx n windows

def maxSlidingWindow(nums, k):
    result = []
    
    l = 0 # left pointer
    for r in range(k-1, len(nums)): # right pointer
        max_num = nums[l] # for each window, initialize max no. to the 1st element in window
        for j in range(1, k): # iterate within the sliding window
            max_num = max(max_num, nums[l+j]) # get the max no. in each sliding window
        l += 1
        
        result.append(max_num)
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: MONOTONIC QUEUE / DEQUE
# NOTE: monotonic queue is a double-ended queue where we can pop from both left and right
# Create a monotonic queue which will always hold the index of the biggest number in any sliding window
# Before adding any new element to q (i.e. the rightmost element of the new window), keep popping from q if the last element in q is smaller than new element
    # the smaller numbers will definitely not be the max number in current window -> pop them
# Remove the leftmost element from q if the leftmost element is the largest element in previous window
# if current window size is at least k, add largest no. in current window (i.e. 1st element in q) to result array
# increment l and r pointers

# TIME COMPLEXITY: O(n)
    # each element can only be added to the queue once -> queue is limited to n pushes
    # Every iteration of the while loop uses 1 pop -> while loop will not iterate more than n times in total, across all iterations of the for-loop
# SPACE COMPLEXITY: O(k)
    # max possible length of queue = k

from collections import deque

def maxSlidingWindow(nums, k):
    result = [] # return value
    q = deque() # monotonic queue stores indexes
    l = r = 0 # l and r denote the boundaries of the queue

    while r < len(nums):
        # keep popping from queue if the value is smaller than current nums[r]
        while q and nums[r] > nums[q[-1]]:
            q.pop()
        
        q.append(r) # add current nums[r] to queue

        # remove the leftmost value of the previous window from current window
        if l > q[0]:
            q.popleft()
        
        # edge case: since we initiate r to 0, we need to ensure window is at least size k in order to start adding elements to result; if current window is less than size k, we continue with the next r
        if r-l+1 >= k: # if window is at least size k,
            result.append(nums[q[0]]) # 1st element in q is the max element in current window
            l += 1 # move window forward
        
        r += 1 # move window forward
    
    return result