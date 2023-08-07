# https://leetcode.com/problems/delete-node-in-a-bst
# MEDIUM
# Tags: bstlc, #450

# GIVEN:
    # a root node of a BST
    # an integer, key

# TASK:
    # delete the node with the given key in the BST
    # return the root node of the BST after deletion

# EXAMPLES:
    # Input: root = [5,3,6,2,4,null,7], key = 3
    # Output: [5,4,6,2,null,null,7]
    # Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
    # One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
    # Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

    # Input: root = [5,3,6,2,4,null,7], key = 0
    # Output: [5,3,6,2,4,null,7]
    # Explanation: The tree does not contain a node with value = 0.

    # Input: root = [], key = 0
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE
# 3 SITUATIONS: (1) target node (to be deleted) is leaf node, (2) target node has 1 child, (3) target node has 2 children
# 1) If target node to be deleted is a leaf node, set target node's parent's left/right child to null
# 2) If target node has 1 child, target node's parent will adopt target node's child
    # the following code addresses the above 2 situations at the same time:
        # if target has left child: return right child to parent (if target has no right child, null will be returned to parent)
        # if target has right child: return left child to parent (if target has no left child, null will be returned to parent)
# 3) if target node has 2 children
    # replace target node with the smallest value from either its left subtree or its right subtree
    # run the deleteNode() function recursively on target's left/right subtree (whichever subtree the smallest value was taken from), but now the target node to be deleted is the node that replaced the original target node that was deleted

# TIME COMPLEXITY: O(h)
    # h is the height of the tree
    # in the worst case, the height of the tree is O(n) (i.e. the tree is skewed)
    # in the best case, the height of the tree is O(logn) (i.e. the tree is balanced)

def deleteNode(self, root, key):
    if not root: return

    if key < root.val: # find key in left subtree
        root.left = self.deleteNode(root.left, key)
    elif key > root.val: # find key in right subtree
        root.right = self.deleteNode(root.right, key)
    
    else: # if current node is target node to be deleted
        # (1) if target node is leaf node and (2) if target node has 1 child
        if not root.left: # if target node has no left child
            return root.right # return right child to parent (if target has no right child, null will be returned to parent)
        elif not root.right: # if target node has no right child
            return root.left # return left child to parent (if target has no left child, null will be returned to parent)
        
        # (3) if target node has 2 children, choose a replacement node for the target node in 1 of its subtrees
        # Either:
            # Choose minimum node val (i.e. the leftmost node) from right subtree, OR
            # Choose maximum node val (i.e. the rightmost node) from left subtree
        # In the below example, we pick the leftmost node from right subtree
        curr = root.right
        while curr.left:
            curr = curr.left # to find node with min val, keep going to the leftmost node
        root.val = curr.val # replace target node's val with smallest right subtree node val
        root.right = self.deleteNode(root.right, curr.val) # recursively delete that smallest right subtree node val from right subtree
    
    return root