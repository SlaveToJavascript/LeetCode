# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# MEDIUM
# Tags: heaplc, maxheaplc, #215

# GIVEN:
    # an integer array, nums
    # an integer, k

# TASK:
    # return the kth largest element in the array

# EXAMPLES:
    # Input: nums = [3,2,1,5,6,4], k = 2
    # Output: 5

    # Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    # Output: 4

###########################################################################################################

# ✅ ALGORITHM 1: MAX-HEAP
# Create a max heap by converting all numbers in nums to a negative number
# Pop from the max heap k times, the last number popped is the 2nd largest

# TIME COMPLEXITY: O(n + klogn)
    # O(n) to convert all numbers in nums to negative
    # O(n) to create the max heap
    # O(klogn) to pop from the max heap k times
    # O(n + n + klogn) = O(n + k log n)
# SPACE COMPLEXITY: O(n) for the max heap

from heapq import heapify, heappop

def findKthLargest(nums, k):
    nums = [-num for num in nums] # since nums should be max heap, we use the negative values of nums

    heapify(nums)
    
    while k > 0: # pop k largest numbers from max heap
        num = -heappop(nums)
        k -= 1
    
    return num

#==========================================================================================================

# ✅ ALGORITHM 2: MIN-HEAP
# Create min heap
# Push all elements in nums into the min heap 1 by 1, but at the same time, pop smallest nums from heap whenever size of min heap > k
# After finish popping, the min heap will contain the k largest elements in nums
    # the 1st element in the min heap (smallest) is the kth largest element in nums

# TIME COMPLEXITY: O(n log k)
    # heap has a max length of k -> each push operation is O(log k)
    # We iterate n times, with up to log k time at each iteration -> overall TC = O(n log k)
# SPACE COMPLEXITY: O(k) 
    # for the min heap

from heapq import heappush, heappop

def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
        
        if len(min_heap) > k:
            heappop(min_heap)
    
    return heappop(min_heap)

#==========================================================================================================

# ✅ ALGORITHM 3: QUICK SELECT
