# https://leetcode.com/problems/lru-cache/
# MEDIUM
# Tags: hashmaplc, linkedlistlc, designlc, doublylinkedlistlc

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

# ✅ ALGORITHM 1: HASHMAP + DOUBLY LINKED LIST
# Each item in the cache will be a node within a doubly linked list with key, value, previous and next pointers
# we use doubly linked list since we need track the most and least recently used nodes respectively
    # because the order needs to be preserved and we need to reorder the MRU and LRU quickly
    # the LRU and MRU are 2 nodes of the linked list doubly connected to each other
# Every time after we get() a node or put() a node, update that node to the most recently used
# To do get() operations in O(1) time, we use a hashmap
    # hashmap must be of size = capacity
    # key = key, value = node

# TIME COMPLEXITY: O(1) for get() and put()
# SPACE COMPLEXITY: O(n)
    # cache (hashmap) = O(n)
    # doubly linked list = O(n)
    # total = ~ O(2n)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# ABOVE: since we're using nodes, we need to make another class for nodes
# we also need 2 pointers, prev and next, for the previous and next nodes, initially set to null

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # this is our hashmap; key = key, value = nodes

        # dummy nodes to track LRU and MRU nodes
        # left.next will always point to LRU; right.prev will always point to MRU
        self.left = Node(0, 0) # left = LRU
        self.right = Node(0, 0) # right = MRU
        # if we're inserting a new node, we put() it in the middle between left and right
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key]) # remove node from LL
            self.insert(self.cache[key]) # reinsert it into the right in LL (this node is now MRU)
            return self.cache[key].value
        return -1 # if key doesn't exist
    
    def put(self, key, value):
        if key in self.cache: # if key is already in cache, that means a node already exists in our list with the same key-value,
            self.remove(self.cache[key]) # so before we can insert this new key-value pair, we have to remove it from our list
        self.cache[key] = Node(key, value) # create a new node with this key-value and add it to cache
        self.insert(self.cache[key]) # insert this node into our LL (this node is now MRU)

        if len(self.cache) > self.capacity: # check if length of cache now exceeds capacity
            # evict LRU node from LL and remove it from cache
            lru = self.left.next
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
    
    # insert node at the right, just before right dummy node (MRU)
    # to add a node in between 2 nodes in a doubly LL, change the pointers
        # e.g. to add B between A <-> C, do:
            # A.next = B,
            # B.next = C,
            # C.prev = B,
            # B.prev = A
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        node.next = next
        next.prev = node
        node.prev = prev