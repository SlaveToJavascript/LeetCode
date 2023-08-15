# https://leetcode.com/problems/task-scheduler/description/
# MEDIUM
# Tags: heaplc, hashmaplc, intervalslc, #621

# GIVEN:
    # a characters array, tasks, representing the tasks a CPU needs to do, where each letter represents a different task
        # Tasks could be done in any order
        # Each task is done in one unit of time
        # For each unit of time, the CPU could complete either one task or just be idle
    # a non-negative integer, n, that represents the cooldown period between 2 same tasks (the same letter in the array)
        # there must be at least n units of time between any 2 same tasks

# TASK:
    # Return the least number of units of times that the CPU will take to finish all the given tasks

# EXAMPLES:
    # Input: tasks = ["A","A","A","B","B","B"], n = 2
    # Output: 8
    # Explanation: 
    # A -> B -> idle -> A -> B -> idle -> A -> B
    # There is at least 2 units of time between any two same tasks.

    # Input: tasks = ["A","A","A","B","B","B"], n = 0
    # Output: 6
    # Explanation: On this case any permutation of size 6 would work since n = 0.
    # ["A","A","A","B","B","B"]
    # ["A","B","A","B","A","B"]
    # ["B","B","B","A","A","A"]
    # ...
    # And so on.

    # Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    # Output: 16
    # Explanation: 
    # One possible solution is
    # A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

###########################################################################################################

# ✅ ALGORITHM 1: MAX HEAP + QUEUE
# Create a hashmap where key = task and value = frequency of task
# Using hashmap, create a max-heap of frequencies of each task
# Create a queue for tasks in progress
    # each queue[i] = [ freq_of_task, time_when_task_can_continue ]
    # freq_of_task are basically the hashmap values
    # time_when_task_can_continue = the unit time when current task can be continued again after its cooling period (if any), i.e. this is the time when we can add this task to maxHeap

# TIME COMPLEXITY: O(n * k)
    # n = len(tasks)
    # k = idle time
    # on average, TC = O(n) since we just have to go through every single task
    # but in the worst case, we only have 1 type of task (e.g. tasks = [A, A, A, ...]) -> complexity = O(n * idle time for each task)
# SPACE COMPLEXITY: O(n)
    # O(n) for the heap with n elements
    # + O(n) for the queue

from collections import Counter
import heapq

def leastInterval(tasks, n):
    hm = Counter(tasks) # hashmap of { task : frequency of task }
    freq_maxHeap = [-freq for freq in hm.values()] # create max-heap of frequencies of every task
    heapq.heapify(freq_maxHeap)

    time = 0 # use this to track current time
    q = [] # each queue[i] = [ freq_of_task, time_for_task_to_continue ]

    while freq_maxHeap or q: # as long as 1 of these aren't empty, it means there are more tasks to process
        time += 1 # at each loop iteration, 1 task is processed (takes 1 unit of time)

        if freq_maxHeap:
            freq = -heapq.heappop(freq_maxHeap) - 1 # current task's remaining frequency -1 as we just popped the current task from max-heap, i.e. we just processed this task -> remaining frequency of this task -= 1
            if freq > 0: # resulting freq > 0 means we have to come back to this task again later
                q.append([freq, time + n]) # time+n = the time when this task will be available for processing again, i.e. this is the time when we can add this task to maxHeap
            
        if q and q[0][1] == time: # if the available time for the 1st task in the queue has reached,
            heapq.heappush(freq_maxHeap, -q.pop(0)[0]) # pop this task from queue and add it back to maxHeap
    
    return time