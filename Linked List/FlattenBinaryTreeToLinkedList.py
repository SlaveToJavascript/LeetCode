# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description
# MEDIUM
# Tags: binarytreelc, linkedlistlc, dfslc, #114

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
# Recursively flatten each subtree by moving the root in the flattened left subtree to the right of the parent node of this root
# right subtrees are already flattened since the LL all points to the right
        #     1
        #    / \
        #   2   5
        #  / \   \
        # 3   4   6
    # e.g. first, root = 2
        # first flatten each left subtree
            # left subtree (3) is 1 node -> already flattened
        # move 4 (head of flattened root.right) to become 3's (tail of flattened left subtree's) right pointer node
            # 3 -> 4
        # move 3 (head of flattened root.left) to become 2's (root's) right pointer node
            # 2 *-> 3 -> 4
        # set 2's (root's) left pointer to null
            # 2 (left) -> null
    # now, root = 1, left subtree (2 -> 3 -> 4) is flattened
        # move 5 (head of flattened root.right) to become 4's (tail of flattened left subtree's) right pointer node
            # 2 -> 3 -> 4 *-> 5 -> 6
        # move 2 (head of flattened left subtree) to become 1's (root's) right pointer node
            # 1 *-> 2 -> 3 -> 4 -> 5 -> 6
        # set 1's (root's) left pointer to null
            # 1 (left) -> null
# Once we have flattened the entire left subtree, return the tail of the flattened left subtree so it can connect tail.right to the head of the right subtree
    # e.g. 2 -> 3 -> 4 *-> 5 -> 6

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # average case: O(h)
    # worst case: O(n) when h=n

def flatten(root):
    def dfs(root): # dfs(root) flattens tree/subtree from root and returns LL tail
        if not root: return

        left_tail = dfs(root.left) # since the return of the dfs() function is tail of LL, we will get the tail of the LL of the flattened left subtree here
        right_tail = dfs(root.right) # we will get the tail of the LL of the flattened right subtree here

        # if both left and right subtree empty: don't need to do anything
        # if only right subtree is empty: add left_tail to the right side
        # if only left subtree is empty: don't need to do anything since right_tail is already on the right
        if root.left:
            left_tail.right = root.right # move 4 (head of flattened root.right) to become 3's (tail of flattened left subtree's) right pointer node
            root.right = root.left # move 3 (head of flattened root.left) to become 2's (root's) right pointer node
            root.left = None # set root's left pointer to null

        # right_tail is the tail of the entire LL
        # if right_tail is null, left_tail is tail of LL
        # if both left_tail and right_tail are null, root is tail of LL
        tail_LL = right_tail or left_tail or root
        return tail_LL
    
    dfs(root)