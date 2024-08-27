# 1490. Clone N-ary Tree
# https://leetcode.com/problems/clone-n-ary-tree/
# MEDIUM
# Tags: nary, hashmaplc, treelc, narytreelc, dfslc, premiumlc, #1490

# GIVEN:
    # root of an N-ary tree
    # Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.
        # class Node {
        #     public int val;
        #     public List<Node> children;
        # }
        # Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples)

# TASK:
    # return a deep copy (clone) of the tree

# EXAMPLES:
    # Input: root = [1,null,3,2,4,null,5,6]
    # Output: [1,null,3,2,4,null,5,6]

    # Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    # Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

###########################################################################################################

# ✅ ALGORITHM 1A: RECURSIVE DFS (HASHMAP OF ORIGINAL NODES MAPPED TO CLONED NODES)
# ! MAIN IDEA: CREATE A HASHMAP OF ORIGINAL NODES MAPPED TO CLONED NODES
    # helper function returns cloned node if the original node is in hashmap, otherwise adds cloned node to hashmap

# TIME COMPLEXITY: O(n)
    # We visit each node once
# SPACE COMPLEXITY: O(n)
    # for hashmap

def cloneTree(root):
    hashmap = {} # original : clone
    
    def clone_tree(node):
        if not node:
            return
        if node in hashmap:
            return hashmap[node]
        
        clone = Node(node.val)
        hashmap[node] = clone
        for child in node.children:
            clone.children.append(clone_tree(child))
        
        return clone
    
    return clone_tree(root)

#==========================================================================================================

# ✅✅✅ ALGORITHM 1B: RECURSIVE DFS (NO HASHMAP)
# we can iterate over children node and return cloned node without using hashmap
    # NOTE: we don't need hashmap/visited set because N-ary tree is acyclic (a node cannot be revisited once processed during traversal) unlike graphs

# TIME COMPLEXITY: O(n)
    # We visit each node once
# SPACE COMPLEXITY: O(n)
    # recursion call stack

def cloneTree(root):
    if not root:
        return
    
    clone = Node(root.val)
    for child in root.children:
        clone.children.append(cloneTree(child))
    
    return clone