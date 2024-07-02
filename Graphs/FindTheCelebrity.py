# 277. Find the Celebrity
# https://leetcode.com/problems/find-the-celebrity/
# MEDIUM
# Tags: graphlc, #277

# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
# You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
# Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

# EXAMPLES:
    # Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
    # Output: 1
    # Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

    # Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
    # Output: -1
    # Explanation: There is no celebrity.

###########################################################################################################

# ✅ ALGORITHM: BRUTE FORCE
# check if each person is a celeb by checking:
    # if they know anyone (if yes, they are not celeb)
    # if anyone does not know them (if yes, they are not celeb)

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

def findCelebrity(n):
    def is_celeb(curr):
        for i in range(n):
            if i == curr:
                continue
            if knows(curr, i) or not knows(i, curr): # curr is not celeb
                return False
        return True
        
    for curr in range(n):
        if is_celeb(curr):
            return curr
    
    return -1

#==========================================================================================================

# ✅ ALGORITHM 2: LOGICAL DEDUCTION

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def findCelebrity(n):
    option = 0
    for i in range(1,n):
        if knows(option, i):
            option = i # option may be celeb
    
    for i in range(option):
        # We need to check both conditions (whether option knows them and whether they know option) because during the candidate selection process, option might have been updated multiple times based on knows relationships, and we need to ensure that option maintains the celebrity property of not knowing anyone and being known by everyone
        if not knows(i, option) or knows(option, i):
            return -1
    
    for i in range(option+1, n):
        # We only need to check if these people know option. During the candidate selection process, option is always set to the current i when option knows i, which guarantees that option will not know anyone to their right. Hence, we only need to verify if everyone after option knows option
        if not knows(i, option):
            return -1
    
    return option