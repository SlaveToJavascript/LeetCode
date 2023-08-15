# https://leetcode.com/problems/ipo/
# HARD
# Tags: heaplc, minheaplc, maxheaplc

# You can select k distinct projects from a list of projects
# capital and profits are positive integer arrays where the ith project requires capital[i] to invest and it generates profits[i] in profits
# w is the initial amount of capital you're starting with
# after the project, the profits generated will be added to your capital, and with this higher capital you can invest in more projects (until you've invested in k projects)
# TODO: Return your final maximized capital after finishing investing in k projects

###########################################################################################################

# ✅ ALGORITHM 1: MIN HEAP AND MAX HEAP
# Create a list of tuples containing (capital, profit) for each project
# Sort the projects list by capital required to start them
# Create a max-heap to track profits generated
# Use for-loop to loop through k (i.e. the max no. of projects we can invest in)
# Use a while-loop to add all projects we can afford to the maxheap
# If max-heap is empty, it means we cannot afford any projects -> break out of loop
# Get project with highest profit from the max-heap and add this profit to our current capital
# Return final capital

# TIME COMPLEXITY: O(n log n), n = total no. of projects
    # TC of 1 heap push = O(log n)
    # in the worst case scenario where we can afford all projects in projects array -> while loop iterates n times -> TC for pushing into heap n times = O(n log n)
    # TC of 1 heap pop = O(log n)
    # since we pop from heap k times -> TC for popping from heap k times = O(k log n)
    # OVERALL TC = O(n log n) + O(k log n) = O((n+k) log n)
        # since the maximum possible k value = n, O((n+k) log n) ≈ O((n+n) log n) = O(2n log n) ≈ O(n log n)
# SPACE COMPLEXITY: O(n)
    # for the heap with n elements

import heapq

def findMaximizedCapital(k, w, profits, capital):
    projects = [(capital[i], profits[i]) for i in range(len(profits))]
    projects.sort() # sort() auto sorts a list of tuples/arrays by their 1st element
    
    profits_maxheap = []
    for _ in range(k):
        while projects and projects[0][0] <= w: # while the 1st project in projects array can be afforded
            capital, profit = projects.pop(0)
            heapq.heappush(profits_maxheap, -profit) # we push -profit since there's no "max-heap" in heapq, so by using -ve values in a min-heap we would have achieved the same function as using +ve values in a max-heap

        if not profits_maxheap: # if max-heap is empty,
            break # we cannot afford any projects

        w -= heapq.heappop(profits_maxheap) # add greatest profit from max-heap to capital
            # since we added -ve profits to max-heap earlier we use -= instead of += here since +ve minus -ve = +ve plus +ve
    
    return w # w is our final capital + profits amount after investing in k projects