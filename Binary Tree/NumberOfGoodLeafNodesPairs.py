# 1530. Number of Good Leaf Nodes Pairs
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
# MEDIUM
# Tags: binarytreelc, #dfslc, #1530

# GIVEN:
    # the root of a binary tree
    #  an integer distance

# TASK:
    # Return the number of good leaf node pairs in the tree
        # A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance

# EXAMPLES:
    # Input: root = [1,2,3,null,4], distance = 3
    # Output: 1
    # Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

    # Input: root = [1,2,3,4,5,6,7], distance = 3
    # Output: 2
    # Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

    # Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
    # Output: 1
    # Explanation: The only good pair is [2,5].

###########################################################################################################

# ✅ ALGORITHM: DFS
    # https://www.youtube.com/watch?v=HhqyIYaBZgQ&t=171s
# INTUITION:
    # dfs() function returns list
        # list contains distances of the leaf node(s) (if any) from the current node
        # e.g. if list = [1,3], it means there are 2 leaf nodes under this subtree and the distance from current node to these 2 leaf nodes are 1 and 3
    # postorder DFS

# TIME COMPLEXITY: O(n^2)
    # dfs() takes O(n)
    # checking each pair of nodes -> O(n^2) in the worst case (if tree is highly unbalanced)
# SPACE COMPLEXITY: O(n)
    # n = no. of nodes in tree

def countPairs(root, distance):
    result = 0 # no. of pairs of leaves whose distance <= distance
    
    def dfs(node):
        # return value: list contains distances of the leaf node(s) (if any) from the current node
        if not node:
            return []
        if not node.left and not node.right:
            return [1] # leaf node; distance from leaf node to parent node is 1
        
        # get distances of leaves in left and right subtrees
        left_list = dfs(node.left)
        right_list = dfs(node.right)
        result += sum(l+r <= distance for l in left_list for r in right_list) # counts the no. of valid leaf node pairs between the left and right subtrees of the current node
        return [1+item for item in left_list+right_list] # concatenate the 2 lists; add 1 to each element to account for distance from the CURRENT node
    
    dfs(root)
    return result