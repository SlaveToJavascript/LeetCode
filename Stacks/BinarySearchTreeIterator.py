# https://leetcode.com/problems/binary-search-tree-iterator/description/
# MEDIUM
# Tags: bstlc, binarytreelc, stacklc, designlc, #173

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
    # BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor
        # The pointer should be initialized to a non-existent number smaller than any element in the BST.
    # hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    # next() Moves the pointer to the right, then returns the number at the pointer.
        # Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

# EXAMPLES:
    # Input
    # ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    # [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    # Output
    # [null, 3, 7, true, 9, true, 15, true, 20, false]

    # Explanation
    # BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
    # bSTIterator.next();    // return 3
    # bSTIterator.next();    // return 7
    # bSTIterator.hasNext(); // return True
    # bSTIterator.next();    // return 9
    # bSTIterator.hasNext(); // return True
    # bSTIterator.next();    // return 15
    # bSTIterator.hasNext(); // return True
    # bSTIterator.next();    // return 20
    # bSTIterator.hasNext(); // return False

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS

# TIME COMPLEXITY: O(n) for constructor method, O(1) for next() and hasNext()
# SPACE COMPLEXITY: O(n)
    # for self.nodes array

class BSTIterator(object):
    def __init__(self, root):
        self.iterator = -1 # pointer initialized to a non-existent number smaller than any element in BST
        
        def inorder(root): # recursive inorder traversal function that returns an array of nodes in inorder traversal
            if not root:
                return []

            return inorder(root.left) + [root] + inorder(root.right)
        
        self.nodes = inorder(root) # nodes of the BST in inorder traversal sequence

    def next(self):
        self.iterator += 1
        return self.nodes[self.iterator].val

    def hasNext(self):
        return self.iterator < len(self.nodes)-1 # if iterator is not at the last element in self.nodes array, return True
    
#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS WITH STACK
# Go as far left as possible and add each node encountered along the way to the stack
# When next() is called, pop the top node from the stack and return its value
    # If the popped node has a right child, go as far left as possible from that right child and add each node encountered to the stack
# When hasNext() is called, return True if the stack is not empty, False otherwise

# TIME COMPLEXITY: O(n) for constructor method, O(1) average for next() and hasNext()
# SPACE COMPLEXITY: O(h)
    # max length of stack = h

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        # Go as far left as possible and add each node encountered along the way to the stack
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop() # node to be returned
        curr = node.right
        while curr: # if popped node has a right child,
            self.stack.append(curr) # go as far left as possible from that right child and add each node encountered to the stack
            curr = curr.left
        return node.val

    def hasNext(self):
        return len(self.stack) > 0 # if length of stack > 0, there are still nodes to traverse/visit