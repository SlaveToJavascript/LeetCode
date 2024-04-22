# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# MEDIUM
# Tags: bfslc, binarytreelc, #515

# GIVEN:
    # the root of a binary tree

# TASK:
    # return an array of the largest value in each row of the tree

# EXAMPLES:
    # Input: root = [1,3,2,5,3,null,9]
    # Output: [1,3,9]

    # Input: root = [1,2,3]
    # Output: [1,3]

###########################################################################################################

# ✅ ALGORITHM 1: ITERATIVE BFS
# Use BFS (queue) to iterate each level of the binary tree to get the max value at each level
# after finishing the iteration for each level, add the max value into a result array

# TIME COMPLEXITY: O(n)
    # we visit each node once
# SPACE COMPLEXITY: O(n)
    # we store each node in the queue once

def largestValues(root):
    if not root:
        return []
        
    q = [root]
    result = []

    while q:
        max_val = float('-inf') # before each for-loop iteration, initialize max value to the smallest possible number

        for _ in range(len(q)): # each iteration of this for-loop iterates within the current level
            node = q.pop(0)
            max_val = max(max_val, node.val) # check if current node val is largest in this level
            
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
        
        # at this point (i.e. after every for-loop iteration), q contains only elements from NEXT level
            # all elements from current level have been popped out in the for-loop
        result.append(max_val)
    
    return result