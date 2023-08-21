# https://www.lintcode.com/problem/3673/
# MEDIUM
# Tags: topsortlc, topologicalsortlc, toposortlc, bfslc, queuelc, #1136

# There are n courses numbered 1 to n
# There is also a 2D array, relations
    # Inside each nested array contains 2 courses
        # The 1st course is a pre-requisite for the 2nd course
        # That is, you must learn the 1st course in the array before learning the 2nd course in the array
# You may study any number of courses in a semester, provided you have completed all prerequisites for that course in the previous semester
# TODO: Return minimum semester of full coursework, or -1 if full coursework cannot be completed

# EXAMPLES:
    # Input: n = 4, relations = [[1,2],[2,3],[2,4]]
    # Output: 3
    # Explanation:
        # Semester 1: Study 1
        # Semester 2: Study 2
        # Semester 3: Study 3, 4

    # Input: n = 4, relations = [[1,2],[2,3],[2,4],[3,4]]
    # Output: 4
    # Explanation:
        # Semester 1: Study 1
        # Semester 2: Study 2
        # Semester 3: Study 3
        # Semester 4: Study 4

    # Input: n = 2, relations = [[1,2],[2,1]]
    # Output: -1
    # Explanation: To take course 2 you should have finished course 1, and to take course 1 you should also have finished course 2. So it is impossible

###########################################################################################################

# ✅ ALGORITHM: TOPOLOGICAL SORT (BFS, QUEUE)
# Create adjacency list to represent the graph
# Create an in-degree list to represent the number of prerequisites for each course
    # indegree[i] = no. of prerequisites for course i
# Add nodes with in-degree 0 to the queue
    # These represent courses that have no prerequisites and can be taken in the first semester
# Process the queue:
    # For each course, visit its dependents
        # dependents of course i are courses that have course i as a prerequisite
    # Decrease the in-degree for each dependent
    # If a dependent's in-degree becomes 0, it means all its prerequisites are completed and can be added to the queue
# Repeat the processing of queue until all nodes are processed

# TIME COMPLEXITY: O(r+n)
    # r = no. of relations (edges)
    # n = no. of courses (nodes)
    # building indegree and adjList: O(r)
    # BFS traversal: Each course is processed exactly once and each relation is also considered exactly once -> O(r+c)
# SPACE COMPLEXITY: O(r+n)
    # indegree: O(n)
    # adjList: O(r+n) in the worst case

from collections import defaultdict, deque

def minimumSemesters(n, relations):
    indegree = [0] * (n+1) # n+1 bc courses are from 1 to n (both inclusive)
        # indegree[i] = no. of prerequisites for course i
            # i.e. we need to complete these prerequisites before we can complete course i
    adjList = defaultdict(set) # key: course -> value: set of dependents of course
    semesters = 0 # return value

    # fill up adjList and indegree
    for a, b in relations:
        adjList[a].add(b)
        indegree[b] += 1

    q = deque([i for i in range(1, n+1) if indegree[i] == 0]) # Add nodes with in-degree 0 to the queue
    completed_courses = 0

    while q:
        semesters += 1

        for _ in range(len(q)): # iterate over the courses that can be completed this semester
            course = q.popleft()
            completed_courses += 1

            for dependent in adjList[course]: # visit all courses that have current course as prerequisite
                indegree[dependent] -= 1
                if indegree[dependent] == 0: # this means all of dependent's prerequisite courses are completed -> we are now able to complete dependent course -> add it to queue
                    q.append(dependent)
    
    return semesters if completed_courses == n else -1 # If not all courses are completed, it means there's a cycle