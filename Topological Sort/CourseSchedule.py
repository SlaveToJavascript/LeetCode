# https://leetcode.com/problems/course-schedule/description/
# MEDIUM
# Tags: graphlc, topologicalsortlc, toposortlc, topsortlc, dfslc, backtracklc, backtrackinglc, #207

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1
# You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first if you want to take course a_i
    # e.g. the pair [0, 1] indicates that to take course 0 you have to first take course 1
# TODO: Return true if you can finish all courses
    # Otherwise, return false

# EXAMPLES:
    # Input: numCourses = 2, prerequisites = [[1,0]]
    # Output: true
    # Explanation: There are a total of 2 courses to take. 
    # To take course 1 you should have finished course 0. So it is possible.

    # Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    # Output: false
    # Explanation: There are a total of 2 courses to take. 
    # To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
    # https://www.youtube.com/watch?v=EgI5nU9etnU
# Create adjacency list of each course and its prerequisites
# If a course doesn't have any prerequisites, it can definitely be completed
    # so a base case is: if prerequisites of a course is empty, return True (as this course can be completed)
# If a course has prerequisites, we have to check if all its prerequisites can be completed
    # do dfs on every prerequisite of this course to check if course can be completed
# if all prerequisites can be completed, we know this course can be completed
    # remove course from visited set (backtracking) to explore other paths, preventing the incorrect identification of a cycle for those paths
    # since we know this course can be completed, we can empty out its prerequisites set
        # so that in the next recursions where course is passed, the base case will pick up that it's a course that can definitely be completed and return True immediately (instead of having to check its prereqs all over again)

# TIME COMPLEXITY: O(c+p)
    # c = no. of course
    # p = no. of prerequisites given
    # dfs function handles each node once, which takes O(c) time in total
        # From each node, we iterate over all the outgoing edges, which further takes O(p) time to iterate over all the edges as there are a total of p edges
# SPACE COMPLEXITY: O(c+p)
    # for the hashmap, since each course and prerequisite is stored

from collections import defaultdict

def canFinish(numCourses, prerequisites):
    # create adjacency list of: course -> {set of prerequisites}
    prereqsList = defaultdict(set)
    for course, prereq in prerequisites:
        prereqsList[course].add(prereq)
    
    visited = set()

    def dfs(course):
        if course in visited: # this means loop exists -> course cannot be completed
            return False
        if not prereqsList[course]: # if course has no prereqs, it can definitely be completed
            return True
        
        visited.add(course)
        for prereq in prereqsList[course]: # for each prerequisite of current course,
            if not dfs(prereq): # if we find 1 prerequisite that can't be completed, then the current course cannot be completed
                return False
        
        # if we reached this point, it means course can be completed
        visited.remove(course) # since we finished checking whether current course can be completed, we remove it from visited
            # *** NOTE: see below for examples of why this line is needed
        
        prereqsList[course] = set() # since we know course can definitely be completed, we can empty its prerequisites set so that in the next recursions where course is passed, the base case will pick up that it's a course that can definitely be completed and return True immediately (instead of having to check its prereqs all over again)
        
        return True # since we know course can be completed

    for course in range(numCourses):
        if not dfs(course): # if course cannot be completed,
            return False
    
    return True # if we reached this point, it means all courses can be completed



# *** NOTE: WHY DO WE NEED "visited.remove(course)"?
    # Example scenario: 
        # Imagine courses A and B both require course C as a prereq (i.e. A -> C and B -> C)
        # When exploring A's prereqs, C is added to visited
        # After C (and hence A) is confirmed to be completable, we backtrack, removing C from visited
        # Later, when exploring B's prereqs, we encounter C again
            # *** If C were not removed from visited after exploring A's prerequisites, the algorithm would incorrectly identify a cycle when there is none, leading to a false conclusion that courses cannot be completed