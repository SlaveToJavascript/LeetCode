# https://leetcode.com/problems/unique-binary-search-trees-ii
# MEDIUM
# Tags: bstlc, #95

# GIVEN:
    # an integer n

# TASK:
    # return all structurally unique BSTs which have exactly n nodes of unique values from 1 to n

# EXAMPLES:
    # Input: n = 3
    # Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

    # Input: n = 1
    # Output: [[1]]

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING
# Create helper function generate(left, right), where left = left boundary (e.g. 1) and right = right boundary (e.g. n)
# generate(left, right) returns a list of all possible unique BSTs that can be formed with nodes of values from left to right
# iterate from left to right, using each current num of the iteration as the root
    # left subtrees of this root are returned by generate(left, root-1)
    # right subtrees of this root are returned by generate(root+1, right)
    # we can do a nested for loop of all the left and right subtrees of this root so we can get all combinations of the left and right subtrees
    # for each combination, create a root node with left and right children = left and right subtrees
    # append each unique tree generated to the result array

# TIME COMPLEXITY: G(n) = O(4^n / n^1.5)
    # The number of unique BSTs that can be formed with n nodes is G(n) where G(n) is the nth Catalan number

def generateTrees(n):
    def generate(left, right): # left and right are the boundaries of our range (the subproblem is defined by a range of numbers)
        if left == right: # i.e. we have a single node (n = 1)
            return [TreeNode(left)] # only a single TreeNode will be returned
        if left > right: # (this will only make sense later, when we do generate(left, root-1): if root = left, it will become left > right)
            return [None] # there are no nodes in this subtree, but we have to put a null node in it so we can iterate throught left_subtrees list later
        
        result = []

        for root in range(left, right+1):
            left_subtrees = generate(left, root-1) # generate all possible left subtrees
            right_subtrees = generate(root+1, right) # generate all possible right subtrees

            # since we want every combination of left subtrees and right subtrees, which are both returned by generate() function, we can use a nested for loop to generate all combinations
            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root_node = TreeNode(root, left_tree, right_tree)
                    result.append(root_node)
        
        return result
    
    return generate(1, n)