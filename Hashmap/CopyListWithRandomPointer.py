# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# MEDIUM
# Tags: linkedlistlc, doublylinkedlist, hashmaplc, #138

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null
# Construct a deep copy of the list
    # The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node
    # Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state
    # None of the pointers in the new list should point to nodes in the original list
    # e.g. if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y
# TODO: Return the head of the copied linked list

# EXAMPLES:
    # Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    # Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

    # Input: head = [[1,1],[2,1]]
    # Output: [[1,1],[2,1]]

    # Input: head = [[3,null],[3,0],[3,null]]
    # Output: [[3,null],[3,0],[3,null]]

###########################################################################################################

# ✅ ALGORITHM: HASHMAP OF ORIGINAL NODES MAPPED TO NEW CLONED NODES
# Iterate through each node in LL, and for each node, create a clone of that node and add the original node and new node to hashmap (key = original node, value = new node)
# Iterate original LL again and for each original node in LL, get the cloned node of that original node and assign its next and random pointers to the cloned version of the next and random nodes respectively
# return the head of the original node

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for the hashmap

def copyRandomList(head):
    old_new = {None: None} # hashmap of original nodes mapped to new cloned nodes
        # initialize with None: None so null nodes in original LL can be mapped to null nodes too
    curr = head
    while curr:
        new = Node(curr.val) # create a clone of original node
        old_new[curr] = new # add original and new nodes to hashmap
        curr = curr.next
    
    curr = head
    new_head = old_new[curr]
    while curr:
        new = old_new[curr]
        new.next = old_new[curr.next] # assign cloned node's next node as the original node's next node's clone
        new.random = old_new[curr.random] # assign cloned node's random node as the original node's random node's clone
        curr = curr.next
    
    return new_head

#==========================================================================================================

# ✅ ALGORITHM: RECURSIVE + HASHMAP
# create clone(node) function that adds original node : cloned node pairs to hashmap and returns the cloned node
# recursively assign cloned node's next and random nodes as the respective clones of the original node's next and random nodes

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def copyRandomList(head):
    old_new = {}
    
    def clone(node):
        if not node: # if node is null,
            return # return null
        
        if node in old_new: # if original node in hashmap
            return old_new[node] # return the clone of the original node from hashmap
        
        new_node = Node(node.val) # clone the original node
        old_new[node] = new_node # add original node and its clone to hashmap

        new_node.next = clone(node.next) # assign cloned node's next node, which is the clone of the original node's next node
        new_node.random = clone(node.random) # assign cloned node's random node, which is the clone of the original node's random node

        return new_node # return the cloned node
    
    return clone(head)