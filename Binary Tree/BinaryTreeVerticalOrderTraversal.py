# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# MEDIUM
# Tags: binarytreelc, premiumlc, dfslc, bfslc, #314

# GIVEN:
    # root of a binary tree

# TASK:
    # return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column)
    # If two nodes are in the same row and column, the order should be from left to right

# EXAMPLES:
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[9],[3,15],[20],[7]]

    # Input: root = [3,9,8,4,0,1,7]
    # Output: [[4],[9],[3,0,1],[8],[7]]

    # Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
    # Output: [[4],[9,5],[3,0,1],[8,2],[7]]

###########################################################################################################

# ✅ ALGORITHM 1: RECRUSIVE DFS WITH X, Y COORDINATES
# ! MAIN IDEA: set root node as coordinates (0,0), and imagine the tree on an x-y axis
    # left children = (-1,-1) (relative to parent coords)
    # right children = (+1,-1) (relative to parent coords)
# since we want to group nodes VERTICALLY, we group nodes with the same x-axis together
# STEPS:
    # 1. Perform DFS to add each node's coords and value to an array in the format (x-coord, y-coord, node.val)
        # root's coords are (0,0), each left child's coords are (x-1,y-1) and each right child's coords are (x+1,y-1) relative to parent's coords
    # 2. After getting this list of tuples, sort it by increasing order of x-coords, then by decreasing order of y-coords
    # 3. Get all node.vals for nodes having the same x-coord, group them together in an array and add this array to the result array

# TIME COMPLEXITY: O(n log n)
    # dfs() takes O(n)
    # sorting takes O(n log n)
# SPACE COMPLEXITY: O(n)
    # for storing nodes tuples array

def verticalOrder(root):
    # root = (0,0)
    # left children = (-1,-1)
    # right children = (+1,-1)
    nodes = []
    
    # add coords of nodes
    def dfs(node, l, r):
        nonlocal nodes

        if not node:
            return 

        nodes.append((l, r, node.val)) # (left_coord, right_coord, node.val)
        if node.left:
            dfs(node.left, l-1, r-1)
        if node.right:
            dfs(node.right, l+1, r-1)
    
    dfs(root, 0, 0)
    nodes.sort(key=lambda x : (x[0], -x[1]))
    result = []
    prev_x = float('-inf') # initialize to any random value
    for x, y, val in nodes:
        if x != prev_x: # if current node and previous node do not have the same x-coords,
            result.append([val]) # create a new nested array within result array for current node
            prev_x = x # update x-coord
        else: # if current node and previous node have the same x-coords,
            result[-1].append(val) # add current node to the nested array of the previous node as they should be grouped together
    
    return result

#==========================================================================================================

# ✅✅ ALGORITHM 2: BFS
# ! MAIN IDEA: set root node as coordinates (0,0), and imagine the tree on an x-y axis
    # left children = (-1,-1) (relative to parent coords)
    # right children = (+1,-1) (relative to parent coords)
# since we want to group nodes VERTICALLY, we use a hashmap where each key is an x-coord, and we group nodes with the same x-coord together in an array (under the same key)
# With BFS traversal, we naturally can guarantee the vertical order of the visits, i.e. the nodes at higher y-levels would get visited before the ones at lower levels
# once we get the hashmap, sort it by the keys and return the values of the hashmap

# TIME COMPLEXITY: O(n log n)
    # BFS takes O(n) since we visit each node once
    # sorting hashmap by keys takes O(n log n)
# SPACE COMPLEXITY: O(n)
    # hashmap takes at most O(n)
    # queue takes at most O(n)

from collections import deque, defaultdict

def verticalOrder(root):
    if not root:
        return []
        
    q = deque([(0, root)]) # q = [ (x-coord, node), (x-coord2, node2), ...]
    hashmap = defaultdict(list) # hashmap = { x-coord -> [list of node.vals with this x-coord] }

    while q:
        x, node = q.popleft()
        hashmap[x].append(node.val)

        if node.left:
            q.append([x-1, node.left])
        if node.right:
            q.append([x+1, node.right])
    
    hashmap = dict(sorted(hashmap.items())) # sort hashmap by keys in increasing order (since we are sorting nodes by their x-coords from left to right)
    return hashmap.values()