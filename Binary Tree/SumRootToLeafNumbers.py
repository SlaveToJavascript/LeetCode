# https://leetcode.com/problems/sum-root-to-leaf-numbers/description
# MEDIUM
# Tags: binarytreelc, dfslc, #129

# GIVEN:
    # the root of a binary tree containing digits from 0 to 9 only
    # Each root-to-leaf path in the tree represents a number.
        # e.g. the root-to-leaf path 1 -> 2 -> 3 represents the number 123

# TASK:
    # Return the total sum of all root-to-leaf numbers

# EXAMPLES:
    # Input: root = [1,2,3]
    # Output: 25
    # Explanation:
    # The root-to-leaf path 1->2 represents the number 12.
    # The root-to-leaf path 1->3 represents the number 13.
    # Therefore, sum = 12 + 13 = 25.

    # Input: root = [4,9,0,5,1]
    # Output: 1026
    # Explanation:
    # The root-to-leaf path 4->9->5 represents the number 495.
    # The root-to-leaf path 4->9->1 represents the number 491.
    # The root-to-leaf path 4->0 represents the number 40.
    # Therefore, sum = 495 + 491 + 40 = 1026.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# Use result array to track the root-to-leaf numbers, then return the sum of the numbers eventually

# TIME COMPLEXITY: O(n), n = no. of nodes
# SPACE COMPLEXITY: O(n), n = no. of nodes

def sumNumbers(root):
    result = []

    def dfs(node, string): # string is the integer string of the number represented from root to node
        if not node:
            return
        
        string += str(node.val)
        if not node.left and not node.right: # if node is leaf
            result.append(int(string)) # add current root-to-leaf number to result array
        
        if node.left: 
            dfs(node.left, string)
        if node.right: 
            dfs(node.right, string)
    
    dfs(root, "")
    return sum(result) # return sum of all numbers in result array