# https://leetcode.com/problems/course-schedule-ii
# MEDIUM
# Tags: graphlc, topologicalsortlc, topsortlc, toposortlc, dfslc, #210

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1
# You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first if you want to take course a_i
    # e.g. the pair [0, 1] indicates that to take course 0 you have to first take course 1
# TODO: Return the ordering of courses you should take to finish all courses
    # If there are many valid answers, return any of them
    # If it is impossible to finish all courses, return an empty array

# EXAMPLES:
    # Input: numCourses = 2, prerequisites = [[1,0]]
    # Output: [0,1]
    # Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

    # Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    # Output: [0,2,1,3]
    # Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    # So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

    # Input: numCourses = 1, prerequisites = []
    # Output: [0]

###########################################################################################################

# ✅ ALGORITHM: TOPOLOGICAL SORT
    # https://www.youtube.com/watch?v=Akt3glAwyfY
# A course has 3 possible states:
    # VISITED: course has been added to result
        # we don't ever have to visit it again
    # VISITING: course not added to result, but added to visited set
        # this means course has been visited in the current path of prerequisites
    # UNVISITED: course not added to result or visited set
        # visited is the current dfs path we're tracing to find the sequence of courses to take
# Create adjacency list of each course and its prerequisites

# TIME COMPLEXITY: O(c+p)
    # c = no. of course
    # p = no. of prerequisites given
    # dfs function handles each node once, which takes O(c) time in total
        # From each node, we iterate over all the outgoing edges, which further takes O(p) time to iterate over all the edges as there are a total of p edges
# SPACE COMPLEXITY: O(c+p)
    # for the hashmap, since each course and prerequisite is stored

from collections import defaultdict

def findOrder(numCourses, prerequisites):
    # create adjacency list of: course -> {set of prerequisites}
    prereqsList = defaultdict(set)
    for course, prereq in prerequisites:
        prereqsList[course].add(prereq)
    
    result = []

    visited = set() # visited is the current dfs path we're tracing to find the sequence of courses to take
        # it also serves as cycle detection

    def dfs(course):
        if course in visited: # this means there is a cycle as we already visited course in this path
            return False
        if course in result: # course has already been added to return result -> we don't need to visit it again
            return True
        
        visited.add(course)

        for prereq in prereqsList[course]: # for each prerequisite of current course,
            if dfs(prereq) == False: # if False is returned, we know there is a cycle as the base case returns False if any of current course's prereqs is in visited
                return False
        
        visited.remove(course) # remove course from visited as it's no longer along the path we're tracing
        result.append(course) # can add course to result since we went through all its prerequisites and added the prerequisites of those prerequisites to result as well
        
        return True
    
    for course in range(numCourses):
        if dfs(course) == False: # if False is returned, we know there is a cycle as the base case returns False if course is in visited -> we cannot possibly finish all courses since there is a cycle
            return []
        
    return result