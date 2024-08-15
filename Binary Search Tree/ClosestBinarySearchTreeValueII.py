# 272. Closest Binary Search Tree Value II
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
# HARD
# Tags: binarytreelc, heaplc, minheaplc, maxheaplc, dfslc, alidingwindowlc, twopointerlc, premiumlc, #272

# GIVEN:
    # root of a binary search tree
    # a "target" value
    # and an integer k

# TASK:
    # return the k values in the BST that are closest to the target
    # You may return the answer in any order
    # You are guaranteed to have only one unique set of k values in the BST that are closest to the target

# EXAMPLES:
    # Input: root = [4,2,5,1,3], target = 3.714286, k = 2
    # Output: [4,3]

    # Input: root = [1], target = 0.000000, k = 1
    # Output: [1]

###########################################################################################################

# ✅ ALGORITHM 1: SORT WITH CUSTOM COMPARATOR
# obtain all values from the BST and add these values into an array
# sort the array in ascending order of the difference between the value and the target
# get the first k elements from the array and return them

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)
    # for storing the values in the array

def closestKValues(root, target, k):
    values = []

    def dfs(node):
        nonlocal values

        if not node:
            return
        
        values.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    values.sort(key=lambda x: abs(target-x)) # sort by ascending order of the difference between the value and the target
    return values[:k]

#==========================================================================================================

# ✅ ALGORITHM 2A: MIN HEAP
# traverse the BST and add the values into a min heap that orders elements based on their difference from the target
# pop the first k elements from the heap and return them

# TIME COMPLEXITY: O(n log n)
    # DFS takes O(n) time since each node is visited once
    # for each node visited in this DFS, we perform a heappush operation which takes O(log n) time
    # -> overall TC = O(n log n)
# SPACE COMPLEXITY: O(n)
    # recursion call stack takes O(n) space
    # heap takes O(n) space

from heapq import heappush, heappop

def closestKValues(root, target, k):
    min_heap = []
    
    def dfs(node):
        nonlocal min_heap

        if not node:
            return
        
        heappush(min_heap, (abs(target-node.val), node.val)) # push node's value and its difference from the target into the min-heap
        
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    result = []
    for _ in range(min(len(min_heap), k)): # adds k elements from the heap into the result OR adds all elements if len(min_heap) < k
        _, val = heappop(min_heap)
        result.append(val)
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2B: MAX HEAP
# traverse the BST and add the values into a max heap that orders elements based on their difference from the target
# when heappushing into the max heap, if length of the max-heap is greater than k, pop the element with the maximum difference from the target (this ensures that there will always be k elements in the max heap)

# TIME COMPLEXITY: O(n log k)
    # DFS takes O(n) time since each node is visited once
    # for each node visited in this DFS, we perform a heappush operation which takes O(log k) time (since there will always be k elements in the max heap)
    # -> overall TC = O(n log k)
# SPACE COMPLEXITY: O(n)
    # recursion call stack takes O(n) space
    # heap takes O(k) space
    # n >= k, so overall TC = O(n) space

def closestKValues(root, target, k):
    max_heap = []
    
    def dfs(node):
        nonlocal max_heap

        if not node:
            return
        
        heappush(max_heap, (-abs(target-node.val), node.val))
        if len(max_heap) > k: # if length of max heap exceeds k, pop the element with the maximum difference from the target
            heappop(max_heap)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    for i in range(len(max_heap)): # for each element in max_heap, 
        max_heap[i] = max_heap[i][1] # get the value of the element for the resulting array
    
    return max_heap

#==========================================================================================================

# ✅ ALGORITHM 3: INORDER TRAVERSAL + SLIDING WINDOW
