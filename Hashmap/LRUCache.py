# https://leetcode.com/problems/lru-cache/
# MEDIUM
# Tags: hashmaplc, linkedlistlc, designlc, doublylinkedlistlc, #146

# Design a data structure that follows the constraints of a LRU cache
# Implement the LRUCache class:
    # LRUCache(capacity) initializes the LRU cache with positive integer size capacity
    # get(key) returns the value of the key if the key exists, otherwise return -1
    # put(key, value) updates the value of the key if the key exists; otherwise, adds the key-value pair to the cache
        # If the no. of keys exceeds the capacity from this operation, evict the least recently used key
# NOTE: get() and put() must each run in O(1) time complexity

# EXAMPLES:
    # Input:
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [   [2],    [1, 1], [2, 2], [1],  [3, 3], [2],  [4, 4], [1],    [3],  [4]]
    # Output:
    # [  null,     null,   null,   1,    null,  -1,    null,   -1,     3,    4]

    # Explanation:
    # LRUCache lRUCache = new LRUCache(2);
    # lRUCache.put(1, 1); // cache is {1=1}
    # lRUCache.put(2, 2); // cache is {1=1, 2=2}
    # lRUCache.get(1);    // return 1
    # lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # lRUCache.get(2);    // returns -1 (not found)
    # lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    # lRUCache.get(1);    // return -1 (not found)
    # lRUCache.get(3);    // return 3
    # lRUCache.get(4);    // return 4

###########################################################################################################

# ✅ ALGORITHM 1A: HASHMAP + DOUBLY LINKED LIST
# Each value in the cache (hashmap) will be a node within a doubly linked list with key, value, previous and next pointers
    # we need a hashmap to get() value of key in O(n) time
    # hashmap must be of size = capacity
    # key = key, value = corresponding node in doubly-LL
# we use doubly linked list since we need track the most and least recently used nodes respectively
    # because the order needs to be preserved and we need to reorder the MRU and LRU quickly
    # left = LRU, right = MRU
    # the LRU and MRU are 2 nodes of the linked list doubly connected to each other
    # if we only use singly linked list, we cannot easily get the previous node of a particular node
# Every time we get() a node or put() a node, reorder the node so that it is now on the MRU side (on the right)

# TIME COMPLEXITY: O(1) for get() and put()
# SPACE COMPLEXITY: O(n)
    # cache (hashmap) = O(n)
    # doubly linked list = O(n)
    # total = ~ O(2n)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
# ABOVE: since we're using nodes, we need to make another class for nodes
# we also need 2 pointers, prev and next, for the previous and next nodes, initially set to null

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # this is our hashmap; key = key, value = node

        # dummy nodes to track LRU and MRU nodes
            # self.LRU.next will always point to LRU node
            # self.MRU.prev will always point to MRU node
        self.LRU = Node(0, 0) # leftmost node in LL
        self.MRU = Node(0, 0) # rightmost node in LL
            # if we're inserting a new node (i.e. put()), we insert it to the left of MRU dummy node
        
        # since there are no nodes yet, connect the LRU and MRU dummy nodes to each other
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key):
        # move target node to MRU side, then return it
        if key in self.cache:
            self.remove(self.cache[key]) # remove node from LL
            self.insert(self.cache[key]) # reinsert it to the left of MRU dummy node
                # this node is now the new MRU node
            return self.cache[key].val
        
        return -1 # key is not in cache
    
    def put(self, key, value):
        if key in self.cache: # if key is already in cache, remove it from cache/LL first then add the updated key-value pair to cache/LL
            self.remove(self.cache[key]) # remove existing node with same key from cache
        
        self.cache[key] = Node(key, value) # create a new node and add it to cache
        self.insert(self.cache[key]) # insert this node into our LL to the left of MRU dummy node (this node is now MRU node)

        if len(self.cache) > self.capacity: # check if length of cache now exceeds capacity
            # evict LRU node from LL and remove it from cache
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]

    # Below 2 functions are helper functions to insert/remove from linked list (LRU/MRU)

    # remove node from from doubly linked list (LRU/MRU)
    # to remove a middle node in a doubly linked list of 3 nodes, change the pointers
        # e.g. for A <-> B <-> C, to remove B, do:
            # A.next = C,
            # C.prev = A
    def remove(self, node): # node is the middle node in the LL (which we wanna remove)
        prev, next = node.prev, node.next # first, get the prev and next nodes of the node to remove
        prev.next = next # set the next pointer of prev node to next node
        next.prev = prev # set the prev pointer of next node to prev node
    
    # insert node to the left of the dummy MRU node
        # this node is now the new MRU node
    # to add a node in between 2 nodes in a doubly LL, change the pointers
        # e.g. to add B between A <-> C, do:
            # A.next = B,
            # B.next = C,
            # C.prev = B,
            # B.prev = A
    def insert(self, node):
        prev, next = self.MRU.prev, self.MRU
        prev.next = node
        node.next = next
        next.prev = node
        node.prev = prev

#==========================================================================================================

# ✅ ALGORITHM 1B: SAME AS ABOVE BUT WITHOUT HELPER FUNCTIONS

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.LRU = Node(0, 0) # LRU dummy node (leftmost node in LL)
        self.MRU = Node(0, 0) # MRU dummy node (rightmost node in LL)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key):
        if key not in self.cache:
            return -1
        
        mru_node = self.cache[key] # target node
        
        # connect prev and next nodes to remove mru_node
        prev_node = mru_node.prev
        next_node = mru_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        # move target node to MRU side (on the right of LL)
        mru_prev = self.MRU.prev # node on the left of MRU dummy node
        # connect MRU dummy's left node to new MRU node
        mru_prev.next = mru_node
        mru_node.prev = mru_prev
        # connect new MRU node to MRU dummy node
        mru_node.next = self.MRU
        self.MRU.prev = mru_node

        return mru_node.val

    def put(self, key, value):
        if key in self.cache: # if key already exists in cache, remove key from cache/LL first then add updated key-value to cache/LL
            to_remove = self.cache[key] # node to be removed from cache/LL
            # connect the left and right nodes of node to be removed
            prev = to_remove.prev
            next = to_remove.next
            prev.next = next
            next.prev = prev
            
            # remove from cache
            del self.cache[key]
        
        # add key and value to LL
        new_node = Node(key, value) # new node to be added to cache/LL
        mru_node = self.MRU.prev # node on the left of MRU dummy node
        # connect MRU dummy node's left node with new node to be inserted
        mru_node.next = new_node
        new_node.prev = mru_node
        # connect new node to be inserted with MRU dummy node
        new_node.next = self.MRU
        self.MRU.prev = new_node
        
        # add to cache
        self.cache[key] = new_node

        # if no. of nodes in cache exceeds capacity, evict LRU node
        if len(self.cache) > self.capacity:
            to_evict = self.LRU.next # node to be removed (i.e. LRU node)
            # connect LRU dummy node and the node on the right of node to be evicted
            evict_next = to_evict.next
            self.LRU.next = evict_next
            evict_next.prev = self.LRU

            # remove evicted node from cache
            del self.cache[to_evict.key]