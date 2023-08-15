# https://leetcode.com/problems/total-cost-to-hire-k-workers/description
# MEDIUM
# Tags: heaplc, minheaplc, twopointerslc, #2462

# GIVEN:
    # integer array costs
        # costs[i] is the cost of hiring the ith worker
    # 2 integers, k and candidates

# TASK:
    # We want to hire exactly k workers according to the following rules:
        # You will run k sessions and hire exactly 1 worker in each session
        # In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers
            # Break the tie by the smallest index.
                # e.g. if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
                # In the 2nd hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]
        # If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them
            # Break the tie by the smallest index
        # A worker can only be chosen once
    # TODO: Return the total cost to hire exactly k workers

# EXAMPLES:
    # Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
    # Output: 11
    # Explanation: We hire 3 workers in total. The total cost is initially 0.
    # - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
    # - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
    # - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
    # The total hiring cost is 11.

    # Input: costs = [1,2,4,1], k = 3, candidates = 3
    # Output: 4
    # Explanation: We hire 3 workers in total. The total cost is initially 0.
    # - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
    # - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
    # - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
    # The total hiring cost is 4.

###########################################################################################################

# ✅ ALGORITHM 1: TWO MIN HEAPS + TWO POINTERS
# Create 1 min heap for the first candidates elements and 1 min heap for the last candidates elements in costs array
# Also create 2 pointers for costs array – 1 that points to the element after the 1st k elements, 1 that points to the element before the last k elements
# If the smaller element is from the 1st heap, pop from the 1st heap and add it to total cost
    # if the pointer for element after 1st heap is less than/equals to pointer for element before 2nd heap, add element after 1st heap to 1st heap
# else if the smaller element is from the 2nd heap, pop from the 2nd heap and add it to total cost
    # if the pointer for element before 2nd heap is greater than/equals to pointer for element after 1st heap, add element before 2nd heap to 2nd heap
# return total cost of popped elements

# TIME COMPLEXITY: O(c + k log c)
    # c = candidates
    # heapify() takes O(c) time (since length of heap is at most c)
    # for each iteration of k, push operation takes O(log c) time -> O(k log c)
# SPACE COMPLEXITY: O(c)
    # 2 priority queues, each of c length

from heapq import heapify, heappop, heappush

def totalCost(costs, k, candidates):
    total_cost = 0 # return value

    # create 1st minheap for the 1st candidates elements
    left_heap = costs[:candidates]
    heapify(left_heap)

    # create 2nd minheap for the last candidates elements or remaining elements
    right_heap = costs[max(candidates, len(costs) - candidates):] # if there are less than candidates elements left after the 1st min heap, the 2nd minheap will take the remaining elements left
    heapify(right_heap)

    # create 2 pointers for costs array: 1 for the element after the left heap, 1 for the element before the right heap
    after_left = candidates
    before_right = len(costs)-candidates-1

    for _ in range(k):
        if not right_heap or left_heap and left_heap[0] <= right_heap[0]:
            # NOTE: "not right_heap" and "left_heap" are checks that short-circuit the if-statement, which you need to do before indexing because otherwise you'll be indexing into an empty heap
                # "not right_heap": If right_heap is empty (True), you are guaranteed that you should short-circuit the rest of the if-statement and go into the if statement to pop/push with left_heap
                # "left_heap": If you've reached here, right_heap is not empty. What's the next thing you need to do? It's to check that you have left_heap that you can compare against:
                    # if no (i.e. left_heap is empty), short-circuit the rest of the if-statement and move to the else statement to pop/push with right_heap
                    # if yes (i.e. left_heap is not empty), you are ready to move on to check if left_heap[0] <= right_heap[0]
            total_cost += heappop(left_heap) # add smallest element in left_heap to total cost
            if after_left <= before_right: # if the pointers do not cross each other,
                heappush(left_heap, costs[after_left]) # push the element after left_heap to left_heap
                after_left += 1 # move the pointer for element after left heap forward
        else:
            total_cost += heappop(right_heap) # add smallest element in right_heap to total cost
            if after_left <= before_right: # if the pointers do not cross each other,
                heappush(right_heap, costs[before_right]) # push element before right_heap to right_heap
                before_right -= 1 # move the pointer for element before right heap to the left
    
    return total_cost

#==========================================================================================================

# ✅ ALGORITHM 2: ONE MIN HEAP + TWO POINTERS
# Instead of creating 1 min heap for left candidates elements and another min heap for right candidates elements, we can just use 1 minheap for both, but keep track of whether an element is from left candidates elements or right candidates elements
    # we can track this by pushing its position (left or right) into heap together with element itself
# Similar to above, use 1 pointer to point to the element after left candidates elements, and another pointer to point to the element before the last candidates elements
# If the left and right pointers cross each other, we don't need to add new elements to the heap as all elements would be in heap at this point

# TIME COMPLEXITY: O((k + c) log c)
    # c = candidates
    # when pushing costs elements into heap at the beginning, we are pushing an element into heap for c times for each left and right -> O(c log c)
    # for each iteration of k, push operation takes O(log c) time -> O(k log c)
    # overall TC = O(c log c) + O(k log c) = O((k+c) log c)
# SPACE COMPLEXITY: O(c)
    # priority queue of 2c length

from heapq import heapify, heappop, heappush

def totalCost(costs, k, candidates):
    heap = []

    # push 1st candidates elements into heap
    c = 0
    while c < candidates:
        heappush(heap, (costs[c], 1)) # for elements from 1st candidates elements, push 1
        c += 1
    
    # push last candidates elements into heap
    c = len(costs)-1
    while c >= max(len(costs)-candidates, candidates):
        heappush(heap, (costs[c], 2)) # for elements from last candidates elements, push 2
        c -= 1
    
    # 2 pointers: 1 for element after 1st candidates elements, 1 for element before last candidates elements
    left, right = candidates, len(costs)-candidates-1
    total_cost = 0 # return value

    for _ in range(k):
        cost, pos = heappop(heap) # smallest from heap
        total_cost += cost

        if left <= right:
            if pos == 1: # cost is from 1st k elements
                heappush(heap, (costs[left], 1)) # push element at left pointer into heap
                left += 1
            else: # cost is from last k elements
                heappush(heap, (costs[right], 2)) # push element at right pointer into heap
                right -= 1
        
    return total_cost