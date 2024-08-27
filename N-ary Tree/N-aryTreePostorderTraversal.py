# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# EASY
# Tags: treelc, narytreelc, nary, dfslc, #590

# GIVEN:
    # root of an n-ary tree

# TASK:
    # return the postorder traversal of its nodes' values
        # Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# EXAMPLES:
    # Input: root = [1,null,3,2,4,null,5,6]
    # Output: [5,6,3,2,4,1]

    # Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    # Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# ! MAIN IDEA: visit all children of a node from left to right -> after all children are visited, then visit the node itself

# TIME COMPLEXITY: O(n)
    # visits each node once
# SPACE COMPLEXITY: O(n)
    # max. depth of recursion call stack = n (for skewed trees) or O(h) for balanced trees

def postorder(root):
    result = []

    def dfs(node):
        nonlocal result

        if not node:
            return 
        
        for child in node.children:
            dfs(child)
        
        result.append(node.val)
    
    dfs(root)
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS (STACK)
# 1. Push root into stack
# 2. While stack is not empty, pop node from stack (LIFO) to process
# 3. Add popped node to stack
# 4. For each of node's children, add to stack
    # NOTE: since node's children are appended to STACK from left to right, when they get popped out later it would be from right to left, and at the last step we reverse the result array so the ordering would be node -> left child -> right child
# 5. Reverse array after while-loop ends

# TIME COMPLEXITY: O(n)
    # visits each node once
# SPACE COMPLEXITY: O(n)
    # for the stack

def postorder(root):
    result = []
    if not root:
        return result

    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        for child in node.children:
            stack.append(child)

    result.reverse()
    return result