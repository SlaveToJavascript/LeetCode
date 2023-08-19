# https://leetcode.com/problems/find-median-from-data-stream/
# HARD
# Tags: heaplc, designlc, #295

# The median is the middle value in a sorted integer list
# If the size of the list is even, there is no middle value, and the median is the mean of the 2 middle values
    # e.g. for arr = [2,3,4], the median is 3.
    # e.g. for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# TODO: Implement the MedianFinder class:
    # MedianFinder() initializes the MedianFinder object
    # addNum(num) adds the integer, num, from the data stream to the data structure
    # findMedian() returns the median of all elements so far

# EXAMPLES:
    # Input
    # ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    # [[], [1], [2], [], [3], []]
    # Output
    # [null, null, null, 1.5, null, 2.0]

    # Explanation
    # MedianFinder medianFinder = new MedianFinder();
    # medianFinder.addNum(1);    // arr = [1]
    # medianFinder.addNum(2);    // arr = [1, 2]
    # medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    # medianFinder.addNum(3);    // arr[1, 2, 3]
    # medianFinder.findMedian(); // return 2.0

###########################################################################################################

# ✅ ALGORITHM 1: 2 HEAPS (MIN HEAP AND MAX HEAP)
# __init__():
    # Use 2 heaps: smallHeap for smallest numbers, and bigHeap for biggest numbers
        # These 2 heaps should have either the same length or lengths differing by 1

# addNum():
    # 1) By default, add all elements to the min-heap (bigHeap)
    # 2) Ensure every number in bigHeap is bigger than every element in smallHeap - if smallest val in bigHeap < largest val in smallHeap, push smallest val in bigHeap to smallHeap
    # 3A) if len(bigHeap) > len(smallHeap) by 2 or more, pop smallest element from bigHeap and push it into smallHeap
    # 3B) inversely, if len(smallHeap) > len(bigHeap) by 2 or more, pop biggest element from smallHeap and push it into bigHeap

# findMedian():
    # If both heaps are the same length, return the average of the 2 middle elements
        # both heaps same length means there's an even no. of numbers
    # Else, pop and return the number from the heap that has the greater length

# TIME COMPLEXITY: O(log n) for addNum() and findMedian()
    # NOTE: findMedian() uses O(1) time since getting the min/max from min-heap/max-heap requires O(1)
# SPACE COMPLEXITY: O(n)
    # O(n) for smallHeap + O(n) for bigHeap = O(2n) ≈ O(n)

import heapq

class MedianFinder(object):

    def __init__(self):
        self.smallHeap = [] # max-heap
        self.bigHeap = [] # min-heap

    def addNum(self, num):
        heapq.heappush(self.bigHeap, num) # by default, add all new numbers to bigHeap
        
        if self.smallHeap and self.bigHeap and self.bigHeap[0] < self.smallHeap[0]: # if smallest value in bigHeap < largest value in smallHeap
            heapq.heappush(self.smallHeap, -heapq.heappop(self.bigHeap)) # push smallest value in bigHeap to smallHeap
        
        # UNEVEN SIZE?
        # if length of bigHeap > length of smallHeap by 2 or more,
        if len(self.bigHeap) - len(self.smallHeap) > 1:
            heapq.heappush(self.smallHeap, -heapq.heappop(self.bigHeap))
        # if length of smallHeap > length of bigHeap by 2 or more,
        elif len(self.smallHeap) - len(self.bigHeap) > 1:
            heapq.heappush(self.bigHeap, -heapq.heappop(self.smallHeap))

    # NOTE: we mustn't use any pop operation on any heaps here, since popping removes from heaps but we might still add new numbers to heaps (i.e. run addNum() function) after running this findMedian() function!
    def findMedian(self):
        if len(self.smallHeap) == len(self.bigHeap):
            return (self.bigHeap[0] - self.smallHeap[0]) / float(2)
        elif len(self.bigHeap) > len(self.smallHeap):
            return self.bigHeap[0]
        else:
            return -self.smallHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()