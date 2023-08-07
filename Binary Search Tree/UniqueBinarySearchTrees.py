# https://leetcode.com/problems/unique-binary-search-trees/description/
# MEDIUM
# Tags: bstlc, #96

# GIVEN:
    # an integer n

# TASK:
    # return the no. of structurally unique BSTs which has exactly n nodes of unique values from 1 to n

# EXAMPLES:
    # Input: n = 3
    # Output: 5

    # Input: n = 1
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING
# Create dp array numTree where numTree[i] is the no. of unique BSTs that can be formed with n nodes of values from 1-n
# numTree[i] = no. of unique left subtrees * no. of unique right subtrees
    # use multiply since we're trying to get the total no. of combinations
# e.g. if n = 5 and root node = 2:
    # no. of unique left subtrees = numTree[1] (since 1 is in the left subtree of node 2)
    # no. of unique right subtrees = numTree[3] (since nodes 3, 4, 5 are in the right subtree of node 2)
# base cases: numsTrees[0] = numTree[1] = 1
    # there can only be 1 subtree each where there are 1 node and 0 nodes
# EXAMPLE:
    # numTree[4] = numTree[0] * numTree[3] +
                        # if root node = 1
                #  numTree[1] * numTree[2] +
                        # if root node = 2
                #  numTree[2] * numTree[1] +
                        # if root node = 3
                #  numTree[3] * numTree[1]
                        # if root node = 4

# TIME COMPLEXITY: O(n^2)
    # n is the no. of nodes in the tree
    # for each node, we iterate through all the nodes before it and all the nodes after it to calculate the no. of unique BSTs that can be formed with the nodes before and after it
# SPACE COMPLEXITY: O(n)
    # n is the no. of nodes in the tree
    # we use an array of size n+1 to store the no. of unique BSTs that can be formed with n nodes

def numTrees(n):
    numTree = [1] * (n+1) # the +1 is for the case numTree[0]
    # numTree[0] = numTree[1] = 1 # base cases which we are already in place
    
    for i in range(2, len(numTree)): # numTree[i] = no. of unique BSTs that can be formed with i nodes of values from 1-i
        total_num_trees = 0 # total_num_trees is the value of the current numTrees[n]
        
        for root in range(1, i+1): # imagine each node from 1 up till current node as root node
            left_num_nodes = root-1 # left_num_nodes is the no. of nodes in the left subtree of root
            right_num_nodes = i-root # right_num_nodes is the no. of nodes in the right subtree of root
            total_num_trees += numTree[left_num_nodes] * numTree[right_num_nodes] # total no. of unique BSTs that can be formed with i nodes = no. of unique left subtrees * no. of unique right subtrees
        
        numTree[i] = total_num_trees # cache this value
    
    return numTree[n]