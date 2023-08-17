# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description
# EASY
# Tags: bstlc, #108

# GIVEN:
    # an integer array, nums, where the elements are sorted in ascending order

# TASK:
    # convert it to a height-balanced binary search tree

# EXAMPLES:
    # Input: nums = [-10,-3,0,5,9]
    # Output: [0,-3,9,-10,null,5]
    # Explanation: [0,-10,5,null,-3,null,9] is also accepted:

    # Input: nums = [1,3]
    # Output: [3,1]
    # Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE
# The element in the middle of every array/subarray should be the parent of a BST
    # elements on the left are all smaller, elements on the right are all greater
# the buildTree() function creates a parent node using the middle element of an array, then sets its left child to the return value of buildTree(left_subarray) – i.e. parent's left subtree, and sets its right child to the return value of the buildTree(right_subarray) – i.e. parent's right subtree

# TIME COMPLEXITY: O(n)
    # we visit each node one
# SPACE COMPLEXITY: O(log n)
    # recursion stack requires O(log n) space as BST is height balanced

def sortedArrayToBST(nums):
    def buildTree(arr): # builds and returns BST constructed from elements in arr
        if not arr: # if arr is empty
            return
        if len(arr) == 1: # if arr has 1 element, create node from the element
            return TreeNode(arr[0])
        
        mid = len(arr) // 2 # index of the middle element in arr
        parent = TreeNode(arr[mid])
        parent.left = buildTree(arr[:mid]) # left subarray
        parent.right = buildTree(arr[mid+1:]) # right subarray
        
        return parent
    
    return buildTree(nums)