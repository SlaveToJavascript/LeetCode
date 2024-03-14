# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
# MEDIUM
# Tags: binarytreelc, linkedlistlc, bfslc, #117

# GIVEN:
    # a binary tree root

# TASK:
    # Populate each next pointer to point to its next right node
        # If there is no next right node, the next pointer should be set to NULL
    # Initially, all next pointers are set to NULL

# EXAMPLES:
    # Input: root = [1,2,3,4,5,null,7]
    # Output: [1,#,2,3,#,4,5,7,#]
    # Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

    # Input: root = []
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: BFS
# use a prev pointer that points to the previous node of every node in the same level
# for every node popped, point prev.next pointer to this popped node

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# TIME COMPLEXITY: O(n)
    # since we process each node exactly once
# SPACE COMPLEXITY: O(n)

def connect(root):
    if not root: 
        return # handles edge case where root = None
    
    q = [root]
    while q:
        prev = None # before the start of every level, initialize prev node to None
        for _ in range(len(q)):
            node = q.pop(0)
            if prev: # if prev is not None,
                prev.next = node # set prev's next pointer to current node
            prev = node # update prev to current node before proceeeding to next iteration of for-loop
            
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
    
    return root