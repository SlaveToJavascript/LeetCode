# 563. Binary Tree Tilt
# https://leetcode.com/problems/binary-tree-tilt/description/
# EASY
# Tags: binarytreelc, dfslc, #563

# GIVEN:
    # root of a binary tree

# TASK:
    # return the sum of every tree node's tilt
        # tilt of a tree node = absolute difference between the sum of all left subtree node values and all right subtree node values
        # If a node does not have a left child, then the sum of the left subtree node values is treated as 0
        # The rule is similar if the node does not have a right child

# EXAMPLES:
    # Input: root = [1,2,3]
    # Output: 1
    # Explanation: 
    # Tilt of node 2 : |0-0| = 0 (no children)
    # Tilt of node 3 : |0-0| = 0 (no children)
    # Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
    # Sum of every tilt : 0 + 0 + 1 = 1

    # Input: root = [4,2,9,3,5,null,7]
    # Output: 15
    # Explanation: 
    # Tilt of node 3 : |0-0| = 0 (no children)
    # Tilt of node 5 : |0-0| = 0 (no children)
    # Tilt of node 7 : |0-0| = 0 (no children)
    # Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
    # Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
    # Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
    # Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

    # Input: root = [21,7,14,1,1,2,2,3,3]
    # Output: 9

###########################################################################################################

# ✅ ALGORITHM: POSTORDER TRAVERSAL
# postorder traversal:
    # 1. calculate sum of all nodes in left subtree
    # 2. calculate sum of all nodes in right subtree
    # 3. use these sums to calculate tilt of current node, i.e. abs(sum of left subtree - sum of right subtree)
# also accumulate the total tilt during this traversal

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(h)
    # h = height of tree

def findTilt(root):
    total_tilt = 0

    def getSum(node): # postorder traversal
        nonlocal total_tilt

        if not node:
            return 0
        
        left_sum = getSum(node.left) # recursively get sum of all left subtree nodes
        right_sum = getSum(node.right) # recursively get sum of all right subtree nodes

        tilt = abs(left_sum - right_sum) # calculate tilt of current node
        total_tilt += tilt # accumulate total tilt of all nodes

        return left_sum + right_sum + node.val # return sum of all nodes in subtree
    
    getSum(root)
    return total_tilt