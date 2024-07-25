# 250. Count Univalue Subtrees
# https://leetcode.com/problems/count-univalue-subtrees/description/
# MEDIUM
# Tags: binarytreelc, dfslc, premiumlc, #250

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the number of uni-value subtrees
    # A uni-value subtree means all nodes of the subtree have the same value

# EXAMPLES:
    # Input: root = [5,1,5,5,5,null,5]
    # Output: 4

    # Input: root = []
    # Output: 0

    # Input: root = [5,5,5,5,5,null,5]
    # Output: 6

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS (POSTORDER)
# Given a node in our tree, we know that it is a uni-value subtree if it meets the following criteria:
    # 1. The children (if any) are also uni-value subtrees
    # 2. The children (if any) have the same value as node
# NOTE: leaf nodes are automatically uni-value subtrees
# the function dfs(node) returns True if the subtree rooted at node is a uni-value subtree
    # base case: return True if node is None, since an empty tree is a uni-value subtree
    # using postorder traversal, recursively check if left and right subtrees are uni-value subtrees
    # if yes, check if the children have the same value as node
        # else, return False

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def countUnivalSubtrees(self, root):
    self.result = 0

    def dfs(node):
        if not node:
            return True # empty tree is a uni-value subtree
        
        # postorder traversal
        is_left_subtree_unival = dfs(node.left)
        is_right_subtree_unival = dfs(node.right)

        if is_left_subtree_unival and is_right_subtree_unival: # if both children are uni-value subtrees,
            if node.left and node.left.val != node.val:
                return False # if left child doesn't have the same value as node, return False
            if node.right and node.right.val != node.val:
                return False # if right child doesn't have the same value as node, return False
            
            self.result += 1 # if False is not returned, it means the current node is a uni-value subtree
            return True
        
        return False
    
    dfs(root)
    return self.result