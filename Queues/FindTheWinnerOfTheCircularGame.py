# 1823. Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# MEDIUM
# Tags: queuelc, #1823

# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.
# The rules of the game are as follows:
    # 1. Start at the 1st friend.
    # 2. Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
    # 3. The last friend you counted leaves the circle and loses the game.
    # 4. If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
    # 5. Else, the last friend in the circle wins the game.
# Given the number of friends, n, and an integer k, return the winner of the game.

# EXAMPLES:
    # Input: n = 5, k = 2
    # Output: 3
    # Explanation: Here are the steps of the game:
    # 1) Start at friend 1.
    # 2) Count 2 friends clockwise, which are friends 1 and 2.
    # 3) Friend 2 leaves the circle. Next start is friend 3.
    # 4) Count 2 friends clockwise, which are friends 3 and 4.
    # 5) Friend 4 leaves the circle. Next start is friend 5.
    # 6) Count 2 friends clockwise, which are friends 5 and 1.
    # 7) Friend 1 leaves the circle. Next start is friend 3.
    # 8) Count 2 friends clockwise, which are friends 3 and 5.
    # 9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

    # Input: n = 6, k = 5
    # Output: 1
    # Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

###########################################################################################################

# ✅ ALGORITHM 1: SIMULATION WITH ARRAY
# Initialize a list of size n, representing n friends labeled from 1 to n
# use curr_index to represent the index we're at in the list
# while there's more than 1 friend in the list, keep eliminating a friend
    # index of friend to be eliminated each time = (curr_idx+k) % len(friends)
# return the last remaining friend in the array

# TIME COMPLEXITY: O(n^2)
    # worst case TC of pop() is O(n), if pop() shifts all subsequent elements
    # while loop is O(n)
    # -> overall TC = O(n^2)
# SPACE COMPLEXITY: O(n)
    # for the friends list

def findTheWinner(n, k):
    circle = [i for i in range(1, n+1)]
    curr_idx = 0 # start from the 1st index
    k -= 1 # since k times supposedly includes the current friend we're on, use k-1 instead to track the no. of moves to make to reach the friend to be eliminated
    while len(circle) > 1:
        curr_idx = (curr_idx+k) % len(circle) # this ensures we land on the friend to be eliminated (in case k > length of array)
        circle.pop(curr_idx)
    
    return circle[0]

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: SIMULATION WITH QUEUE
# Initialize a queue of size n, representing n friends labeled from 1 to n
# while there's more than 1 friend in the queue, shift the 1st element in the queue from front to back for k times, so that the last element will become the friend to be removed
# when there's 1 element left in the queue, return it

# TIME COMPLEXITY: O(n*k)
    # while loop takes O(n)
    # inner for-loop takes O(k)
# SPACE COMPLEXITY: O(n)
    # for the queue

from collections import deque

def findTheWinner(n, k):
    friends = deque(range(1, n+1))
    while len(friends) > 1:
        for _ in range(k):
            friends.append(friends.popleft()) # pop from the left, insert into the right
        friends.pop() # pop the last element, which is the friend to be eliminated
    
    return friends[0]

#==========================================================================================================

# ✅ ALGORITHM 3: RECURSION