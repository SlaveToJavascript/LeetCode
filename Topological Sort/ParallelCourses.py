# 1136. Parallel Courses
# https://leetcode.com/problems/parallel-courses/description/ (premium) OR https://www.lintcode.com/problem/3673/ (free)
# MEDIUM
# Tags: topsortlc, topologicalsortlc, toposortlc, bfslc, queuelc, #1136

# GIVEN:
    # an integer, n
        # indicates that there are n courses labeled from 1 to n
    # an array, relations
        # relations[i] = [prevCourse_i, nextCourse_i], representing a prerequisite relationship between prevCourse_i and nextCourse_i course
            # prevCourse_i has to be taken before course nextCourse_i

# TASK:
    # In 1 semester, you can take any no. of courses as long as you have taken all the prerequisites in the previous semester for those courses
    # Return the minimum no. of semesters needed to take all courses
    # If there is no way to take all the courses, return -1

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

# ✅✅✅ ALGORITHM 1: BFS, TOPOLOGICAL SORT
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
    
    # fill up adjList and indegree
    for a, b in relations:
        adjList[a].add(b)
        indegree[b] += 1

    semesters = 0 # return value

    q = deque([i for i in range(1, n+1) if indegree[i] == 0]) # Add nodes with in-degree 0 to the queue as these are courses that have no prerequisites (and can be taken in the 1st semester)
    completed_courses = 0

    while q:
        semesters += 1

        for _ in range(len(q)): # iterate over the courses that can be completed this semester
            course = q.popleft()
            completed_courses += 1

            for dependent in adjList[course]: # visit all courses (dependents) that have current course as prerequisite
                indegree[dependent] -= 1
                if indegree[dependent] == 0: # this means all of dependent's prerequisite courses are completed -> we are now able to complete dependent course -> add it to queue
                    # NOTE: we need to do the above check so that courses are only added to the queue when all its prerequisite courses are completed, i.e. its indegree = 0
                    q.append(dependent)
    
    return semesters if completed_courses == n else -1 # If not all courses are completed, it means there's a cycle

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: DFS, TOPOLOGICAL SORT (LONGEST PATH) with memoization
# INTUITION: we need to find the LONGEST PATH from a node to a leaf node -> this ensures that all prerequisites are completed before we can complete the course
# we should also return -1 if there are any cycles

# TIME COMPLEXITY: O(r+n)
    # r = no. of relations (edges)
    # n = no. of courses (nodes)
    # DFS function is called once for each course to compute the longest path from that course, but due to memoization, each course is fully explored only once

def minimumSemesters(n, relations):
    adjList = defaultdict(set) # key: course -> value: set of dependents of course
    for a, b in relations:
        adjList[a].add(b)

    visited = set()
    longest_paths_memo = {} # stores the longest path to reach each course
        # format is course : length of longest path to course

    def dfs(course): # dfs() function returns the longest path length from a given course to any of its end courses (i.e. courses with no further prerequisites)
        if course in visited:
            return -1 # cycle detected
        if course in longest_paths_memo:
            return longest_paths_memo[course]
        
        visited.add(course)
        curr_longest_path = 1 # a course on its own is a path of length 1
        
        for next_course in adjList[course]:
            path_len = dfs(next_course) # recursively calls itself to explore further dependencies and compute the longest path to next_course
            if path_len == -1:
                return -1
            curr_longest_path = max(curr_longest_path, 1 + path_len)
        
        visited.remove(course) # This allows the course to be revisited in different DFS paths without incorrectly detecting cycles
        longest_paths_memo[course] = curr_longest_path
        return curr_longest_path

    max_path_len = 0
    for course in range(1, n+1):
        length = dfs(course)
        if length == -1:
            return -1
        max_path_len = max(max_path_len, length)

    return max_path_len



# NOTE: the last for loop allows the algorithm to compare path lengths found starting from different courses
    # needed because the longest path (which determines the answer to the problem) could originate from any course