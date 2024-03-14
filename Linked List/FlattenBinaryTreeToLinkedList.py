# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description
# MEDIUM
# Tags: binarytreelc, linkedlistlc, dfslc, postorderlc, #114

# GIVEN:
    # the root of a binary tree

# TASK:
    # flatten the tree into a "linked list"
        # "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null
        # "linked list" should be in the same order as a preorder traversal of the binary tree

# EXAMPLES:
    # Input: root = [1,2,5,3,4,null,6]
    # Output: [1,null,2,null,3,null,4,null,5,null,6]

    # Input: root = []
    # Output: []

    # Input: root = [0]
    # Output: [0]

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
    # https://www.youtube.com/watch?v=rKnD7rLT0lI
# Recursively flatten each subtree by moving the root in the flattened left subtree to the right of the parent node of this root
# right subtrees are already flattened since the LL all points to the right
        #     1
        #    / \
        #   2   5
        #  / \   \
        # 3   4   6
    # e.g. first, root = 2
        # first flatten each left subtree
            # left child of left subtree (3) is 1 node on its own -> already flattened
        # make 4 (head of flattened root.right) become 3's (tail of flattened left subtree's) right child
            # 3 *-> 4
        # move 3 (head of flattened root.left) to become 2's (root's) right pointer node
            # 2 *-> 3 -> 4
        # set 2's (root's) left pointer to null
            # 2 (left) *-> null
    # now, root = 1, left subtree (2 -> 3 -> 4) is flattened
        # make 4.right -> 5 (root's right child)
            # 2 -> 3 -> 4 *-> 5 -> 6
        # after connecting flattened left and right subtrees, connect 2 (head of connected component) to become 1's (root's) right child
            # 1 *-> 2 -> 3 -> 4 -> 5 -> 6
        # set 1's (root's) left pointer to null
            # 1 (left) *-> null
# Once we have flattened the entire left subtree, return the tail of the flattened left subtree so it can connect tail.right to the head of the right subtree
    # e.g. 2 -> 3 -> 4 *-> 5 -> 6

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # average case: O(h)
    # worst case: O(n) when h=n

def flatten(root):
    def dfs(root): # dfs(root) flattens tree/subtree from root and returns LL tail
        if not root: 
            return

        left_tail = dfs(root.left) # dfs() function returns the LL tail of the flattened left subtree here
        right_tail = dfs(root.right) # we will get the LL tail of the flattened right subtree here

        # if left subtree is not empty, we have to flatten it
        if root.left: # e.g. left tail = 4
            left_tail.right = root.right # make 4.right -> 5 (root's right child), i.e. connects flattened left subtree with right subtree
            root.right = root.left # make 2.right (root.right) -> 3 (head of flattened root.left)
            root.left = None # set root's left pointer to null

        # right_tail is the tail of the entire LL
        # if right_tail is null, left_tail is tail of LL
        # if both left_tail and right_tail are null, root is tail of LL
        tail_LL = right_tail or left_tail or root
        return tail_LL
    
    dfs(root)



# *** WHY POSTORDER TRAVERSAL IN dfs() FUNCTION?
    # left subtree first:
        # Processing left subtree before right subtree lets us flatten the left subtree, making it ready to be attached onto by the right subtree
    # right subtree next:
        # processing right subtree next flattens the right subtree, making it ready to be attached to the end of the flattened chain that starts from root's left child
    # parent node last:
        # parent node reassigns its child pointers, attaching the flattened left subtree to its right pointer and ensuring the flattened right subtree follows it
        # NOTE: this step is only possible if both subtrees are already processed, which is why parent node is handled last!