# 2331. Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# EASY
# Tags: binarytreelc, dfslc, #2331

# GIVEN:
    # root of a full binary tree with the following properties:
        # Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True
        # Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND
    # The evaluation of a node is as follows:
        # If the node is a leaf node, the evaluation is the value of the node, i.e. True or False
        # Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations

# TASK:
    # Return the boolean result of evaluating the root node.
    # NOTE:
        # A full binary tree is a binary tree where each node has either 0 or 2 children

# EXAMPLES:
    # Input: root = [2,1,3,null,null,0,1]
    # Output: true
    # Explanation: The above diagram illustrates the evaluation process.
    # The AND node evaluates to False AND True = False.
    # The OR node evaluates to True OR False = True.
    # The root node evaluates to True, so we return true.

    # Input: root = [0]
    # Output: false
    # Explanation: The root node is a leaf node and it evaluates to false, so we return false.

###########################################################################################################

# ✅ ALGORITHM: DFS
# at leaf nodes, just return True or False
# for non-leaf nodes, evaluate left and right subtrees, and apply the boolean operation of its value with the subtrees' evaluations

# TIME COMPLEXITY: O(n)
    # we visit each node once
# SPACE COMPLEXITY: O(n)
    # recursion call stack

def evaluateTree(root):
    if not root.left and not root.right: # if root is a leaf node
        return bool(root.val) # return True if root.val is 1, False if root.val is 0
    
    # evaluate left and right subtrees
    left_bool = evaluateTree(root.left)
    right_bool = evaluateTree(root.right)
    
    if root.val == 2:
        return left_bool or right_bool
    elif root.val == 3:
        return left_bool and right_bool