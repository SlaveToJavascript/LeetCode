# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# MEDIUM
# Tags: binarytreelc, bfslc, #958

# GIVEN:
    # the root of a binary tree

# TASK:
    # determine if it is a complete binary tree
    # NOTE: In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible
        # It can have between 1 and 2h nodes inclusive at the last level h
        # e.g. this is a complete binary tree:
            #      1
            #    /   \
            #   2     3
            #  / \    /
            # 4   5  6
        # This is not a complete binary tree:
            #     1
            #    / \
            #   2   3
            #  / \   \
            # 4   5   7

# EXAMPLES:
    # Input: root = [1,2,3,4,5,6]
    # Output: true
    # Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

    # Input: root = [1,2,3,4,5,null,7]
    # Output: false
    # Explanation: The node with value 7 isn't as far left as possible.

###########################################################################################################

# ✅ ALGORITHM 1: BFS
# MAIN IDEA: for a complete binary tree, since all nodes in the last level are as far left as possible,
    # while traversing the binary tree level-by-level, once the 1st null node is encountered, all nodes encountered afterwards must be null
    # if any nodes encountered after the 1st null node is non-null, this is not a complete binary tree -> return False

# TIME COMPLEXITY: O(n)
    # we traverse the entire tree
# SPACE COMPLEXITY: O(n)
    # we store the entire tree in a queue

def isCompleteTree(root):
    q = [root]
    reached_null = False # becomes True once we've reached our 1st null node
    
    while q:
        node = q.pop(0)
        
        if not node: # if current node is not null,
            reached_null = True # we have reached the 1st null node
        else: # if node is not null,
            if reached_null: # but we've already previously reached the 1st null node,
                return False # this is not a complete binary tree -> return False
            q.append(node.left)
            q.append(node.right)
    
    return True