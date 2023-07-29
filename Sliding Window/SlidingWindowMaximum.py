# https://leetcode.com/problems/sliding-window-maximum/description/
# HARD
# Tags: queuelc, slidingwindowlc, heaplc, #239

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

# ✅ ALGORITHM 2: QUEUE
# Create a queue which will always hold the biggest number in any sliding window
# for-loop iterates over the 1st sliding window (i.e. 1st k elements from index 0 to k-1):
    # while q is not empty and current element nums[i] is greater than/equal to the last element in q, pop the last element from q
    # append the current element's index to q
# after the loop, q will have 1 element which is the index of the biggest no. in 1st sliding window
    # -> add this element in q to results array
# for-loop with i iterates over remaining elements from index k to n-1:
    # if the element of q (i.e. index of max no. in prev window) is = i-k, pop this no. from q since it represents the 1st no. in our prev window, which is not in current window
    # while q is not empty and current element nums[i] is greater than/equal to the last element in q, pop the last element from q
    # append the current element's index to q
    # add the 1st element in q to results array, since this is the max no. in the current window

# TIME COMPLEXITY: O(n)
    # each element can only be added to the queue once -> queue is limited to n pushes
    # Every iteration of the while loop uses 1 pop -> while loop will not iterate more than n times in total, across all iterations of the for-loop
# SPACE COMPLEXITY: O(k)
    # max possible length of queue = k

def maxSlidingWindow(nums, k):
    result = []
    
    q = []
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]: # if current number >= last element in q,
            q.pop() # remove last element in q
        q.append(i) # add index of current element to q
    
    # at this point, the 1st element in q is the index of the biggest number in the 1st sliding window
    result.append(nums[q[0]])

    for i in range(k, len(nums)):
        if q and q[0] == i-k:
            q.pop(0) # remove this element from q as it represents the 1st no. in the prev sliding window
        while q and nums[i] >= nums[q[-1]]: # if current number >= last element in q,
            q.pop() # remove last element in q
        q.append(i) # add index of current element to q
        result.append(nums[q[0]]) # 1st element in q is the index of the biggest no. in this window
    
    return result