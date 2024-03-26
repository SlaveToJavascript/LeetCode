# 1825. Finding MK Average
# https://leetcode.com/problems/finding-mk-average/description/
# HARD
# Tags: queuelc, heaplc, designlc, #1825

# GIVEN:
    # 2 integers, m and k
    # a stream of integers

# TASKS:
    # implement a data structure that calculates the MKAverage for the stream using these steps:
        # 1. If no. of elements in the stream is less than m, MKAverage = -1
            # Otherwise, copy the last m elements of the stream to a separate container
        # 2. Remove the smallest k elements and the largest k elements from the container
        # 3. Calculate the average value for the rest of the elements rounded down to the nearest integer
    # Implement the MKAverage class:
        # MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
        # addElement(int num) Inserts a new element num into the stream.
        # calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.

# EXAMPLES:
    # Input
    # ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
    # [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
    # Output
    # [null, null, null, -1, null, 3, null, null, null, 5]

    # Explanation
    # MKAverage obj = new MKAverage(3, 1); 
    # obj.addElement(3);        // current elements are [3]
    # obj.addElement(1);        // current elements are [3,1]
    # obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
    # obj.addElement(10);       // current elements are [3,1,10]
    # obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
    #                           // After removing smallest and largest 1 element the container will be [3].
    #                           // The average of [3] equals 3/1 = 3, return 3
    # obj.addElement(5);        // current elements are [3,1,10,5]
    # obj.addElement(5);        // current elements are [3,1,10,5,5]
    # obj.addElement(5);        // current elements are [3,1,10,5,5,5]
    # obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
    #                           // After removing smallest and largest 1 element the container will be [5].
    #                           // The average of [5] equals 5/1 = 5, return 5

###########################################################################################################

# ❌ ALGORITHM 1: QUEUE + MIN AND MAX HEAP (TLE ⏰❌)
# use queue for data stream
# for a Python heap to function as both min heap and max heap:
    # MIN HEAP: first, pop out the smallest k elements from heap
    # then, negate all elements in heap (i.e. turn all x into -x) and heapify() the heap again
    # MAX HEAP: pop out the smallest k elements from heap (which are the largest elements x after you do abs(x))
    # convert all values in the heap back to +ve and calculate the average

# TIME COMPLEXITY: O(m + k log m)
    # calculateMKAverage():
        # extracting last m elements from stream: O(m)
        # heapify the m elements: O(m)
        # popping smallest k vals: each pop = O(log m), total of k pops -> O(k log m)
        # Negating min_heap: O(m-k), assuming k elements were popped
        # re-heapifying: O(m-k)
        # popping largest k vals: each pop = O(log(m-k)), total of k pops -> O(k log(m-k))
        # calculating average: sum() takes O(m-k)
        # OVERALL: O(m + k log m), from heap operations and initial heap construction (these are the dominant operations)
# SPACE COMPLEXITY: O(n)

from heapq import heapify, heappop

class MKAverage(object):
    def __init__(self, m, k):
        self.stream = []
        self.m = m
        self.k = k

    def addElement(self, num):
        self.stream.append(num)

    def calculateMKAverage(self):
        if len(self.stream) < self.m:
            return -1

        min_heap = self.stream[-self.m:] # last m elements of stream
        heapify(min_heap)
        
        # pop out smallest k values
        for _ in range(self.k):
            heappop(min_heap)
        
        # convert to -ves
        min_heap = [-i for i in min_heap]
        heapify(min_heap) # need to re-heapify to reorder the negated min_heap array
        
        # pop out largest k values (after converted to +ve)
        for _ in range(self.k):
            heappop(min_heap)
        
        # technically, you don't need to manually convert min_heap back into positive numbers, since you can just do abs(sum(min_heap)) as per below line, which would still get you the correct sum
            
        return abs(sum(min_heap)) // len(min_heap)
    
#==========================================================================================================

# ✅ ALGORITHM 2: QUEUE + SORTEDLIST
# use queue for data stream
# use SortedList to keep container always sorted in order
# for every num added to data stream, if length of stream > m after num is added, remove the old element(s) from stream and container so that the size of stream and container is always at most m
# even though the calculation of remaining elements in container after removing k smallest and k largest elements is not optimal, the code still works and passes in time
    
# TIME COMPLEXITY: O(m-2k)
    # push and pop into deque = O(1)
    # sorted list insertion and deletion = O(log m)
    # biggest bottleneck: calculation of sum, which is O(m-2k)
# SPACE COMPLEXITY: O(m)
    # for SortedList
    # for deque
    
from sortedcontainers import SortedList
from collections import deque

class MKAverage(object):
    def __init__(self, m, k):
        self.stream = deque()
        self.container = SortedList() # container of last m elements from data stream
        self.m = m
        self.k = k

    def addElement(self, num):
        if len(self.container) >= self.m: # if there are more than m elements after adding num, remove the 1st element from stream and container so there'll be m elements after the new element is added
            discarded_num = self.stream.popleft()
            self.container.discard(discarded_num)
        
        # add num to stream and container
        self.stream.append(num)
        self.container.add(num)

    def calculateMKAverage(self):
        if len(self.stream) < self.m:
            return -1
        
        leftover = self.container[self.k:-self.k] # leftover is the container array after removing k smallest and k largest elements
        return sum(leftover) // len(leftover)