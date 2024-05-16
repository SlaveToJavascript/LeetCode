# 270. Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/
# EASY
# Tags: bstlc, premiumlc, #270

# GIVEN:
    # root of a binary search tree
    # a target value

# TASK:
    # return the value in the BST that is closest to the target
    # If there are multiple answers, print the smallest

# EXAMPLES:
    # Input: root = [4,2,5,1,3], target = 3.714286
    # Output: 4

    # Input: root = [1], target = 4.428571
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: COMPARE CURRENT VS MIN. DIFF
# traverse the tree using a while-loop
# closest = node.val with smallest difference from target
# at each node, if difference between node.val and target is smaller than min_diff (i.e. difference between closest and min_diff), update min_diff and closest
# go to the left or right child of root depending on which side is closer to target

# TIME COMPLEXITY: O(h)
    # worst case: O(n) if h = n
# SPACE COMPLEXITY: O(1)

def closestValue(root, target):
    closest = root.val # return value ; node.val with smallest difference from target ; initialize to root

    while root:
        min_diff = abs(target - closest)
        curr_diff = abs(target - root.val)

        if curr_diff < min_diff or (curr_diff == min_diff and root.val < closest):
            closest = root.val
        
        root = root.left if target < root.val else root.right
    
    return closest