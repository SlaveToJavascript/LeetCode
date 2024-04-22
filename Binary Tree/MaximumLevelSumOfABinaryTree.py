# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
# MEDIUM
# Tags: binarytreelc, bfslc, #1161

# GIVEN:
    # the root of a binary tree

# TASK:
    # Return the smallest level x such that the sum of the values of nodes at level x is maximal within the tree
    # NOTE: the level of its root is 1, the level of its children is 2, and so on

# EXAMPLES:
    # Input: root = [1,7,0,7,-8,null,null]
    # Output: 2
    # Explanation: 
    # Level 1 sum = 1.
    # Level 2 sum = 7 + 0 = 7.
    # Level 3 sum = 7 + -8 = -1.
    # So we return the level with the maximum sum which is level 2.

    # Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
    # Output: 2

###########################################################################################################

# ✅ ALGORITHM 1: BFS (O(2n) space complexity)
# Create array to keep track of the sums of each level of the tree
# Do BFS on tree to get the sum of all nodes on each level and add the sum to the array
# Get the maximum value of the array and return the index + 1 of the maximum value in the array

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(2n)
    # O(n) for queue + O(n) for sums array

def maxLevelSum(root):
    sums = [] # where we track the sums of each level of the tree

    q = [root]
    while q:
        curr_level_sum = 0 # this will track the sum of the current level in the tree
        for _ in range(len(q)):
            node = q.pop(0)
            curr_level_sum += node.val
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
        
        # at this point (i.e. after current for-loop, q only has elements from the next level)
        sums.append(curr_level_sum)
    
    return sums.index(max(sums)) + 1

#==========================================================================================================

# ✅✅✅ ALGORITHM 1A: BFS (slightly optimized with O(n) space complexity)
# Instead of using extra space for a sums array to keep track of the sums of every level,
# we can simply update the maximum sum and its corresponding level while doing the BFS

# TIME COMPLEXITY: O(n)
    # BFS visits each node once
# SPACE COMPLEXITY: O(n)
    # O(n) for the queue

def maxLevelSum(root):
    max_sum, curr_level, max_sum_level = float('-inf'), 0, 0 # max_sum_level is our return value

    q = [root]
    while q:
        curr_level += 1 # curr_level keeps track of which level we are currently on
        curr_level_sum = 0 # curr_level_sum will track the sum of the current level
        
        for _ in range(len(q)):
            node = q.pop(0)
            curr_level_sum += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        # at this point, i.e. after each for-loop ends, the queue contains only nodes from the next level
        if curr_level_sum > max_sum:
            max_sum = curr_level_sum # update the max sum since current level's sum is greater than existing max sum
            max_sum_level = curr_level # update the level with the max sum since current level's sum is greater than existing max sum
        
    return max_sum_level # return the level with the max sum