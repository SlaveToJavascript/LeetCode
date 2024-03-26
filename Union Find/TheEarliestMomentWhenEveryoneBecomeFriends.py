# 1101. The Earliest Moment When Everyone Become Friends
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/
# MEDIUM
# Tags: unionfindlc, #1101

# There are n people in a social group labeled from 0 to n - 1
# You are given an array logs where logs[i] = [timestamp_i, x_i, y_i] indicates that xi and yi will be friends at the time timestamp_i
# Friendship is symmetric
    # That means if a is friends with b, then b is friends with a
# Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b

# TASK:
    # Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1

# EXAMPLES:
    # Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
    # Output: 20190301
    # Explanation: 
    # The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
    # The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
    # The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
    # The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
    # The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
    # The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.

    # Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
    # Output: 3
    # Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.

###########################################################################################################

# ✅ ALGORITHM: UNION FIND
# MAIN IDEA:
    # when p1 and p2 become friends, all of p1's friends (lets call them p3) become friends with p2's friends as well
        # -> to each of p3's friends lists, add p1's new friends (i.e. p2's friends)
# STEPS:
    # 1. Sort logs by timestamp (since we want the EARLIEST time when everyone became friends)
    # 2. build graph of each person i mapped to all its friends and itself
        # NOTE: you actually need to add yourself as a friend in order for the code to work
    # 3. iterate through logs and update graph
    # 4. Once any person's set of friends contains n friends (i.e. including that person oneself), that's when everyone became friends -> return that timestamp

# TIME: O(m log m + m*n)
    # n = no. of people
    # m = no. of logs
    # sorting logs by timestamp takes O(m log m) time
    # the 2nd for-loop iterates through m logs, and for each iteration, the union() function takes O(n) time as there are n people in the graph
# SPACE: O(m + n)
    # sorting the logs takes O(m) space, where m = no. of logs
    # graph hashmap takes O(n) space, where n = no. of people

from collections import defaultdict

def earliestAcq(logs, n):
    logs.sort(lambda x: x[0]) # sort logs by timestamp

    graph = defaultdict(set)
    for i in range(n):
        graph[i].add(i) # initialize graph hashmap by making everyone be their own friends

    for time, p1, p2 in logs:
        graph[p1] = graph[p1].union(graph[p2]) # add all of p2's friends to p1's friends set
        
        # p1's friends are now friends with p2's friends -> add p1's new friends set to the friends sets of p1's friends
        for p3 in graph[p1]: # each p3 is p1's friend
            graph[p3] = graph[p1]
        
        if len(graph[p1]) == n: # p1 is now friends with everyone -> this means everyone became friends
            return time
    
    # if we managed to reach this line, it means that it's not possible for everyone to become friends
    return -1