# BINARY TREE RECURSION (DFS) ##################################################################################################
# General steps:
    # 1. Find 1 or more base cases
    # 2. Call the same function on the left subtree
    # 3. Call the same function on the right subtree
    # 4. Join the results

# ========== EXAMPLE 1: GET TREE SUM ==========
def tree_sum(root):
    # 1. base cases
    if not root:
        return 0
    
    # 2. call function on left subtree
    left_sum = tree_sum(root.left)
    # 3. call function on right subtree
    right_sum = tree_sum(root.right)

    # 4. join the results
    return root.val + left_sum + right_sum

# ========== EXAMPLE 2: GET MAX NODE IN TREE ==========
def tree_max(root):
    # 1. base cases
    if not root:
        return float('-inf')
    
    # 2. call function on left subtree
    left_max = tree_max(root.left)
    # 3. call function on right subtree
    right_max = tree_max(root.right)

    # 4. join the results
    return max

# ========== EXAMPLE 3: GET TREE HEIGHT ==========
def tree_height(root):
    # 1. base cases
    if not root:
        return 0
    
    # 2. call function on left subtree
    left_height = tree_height(root.left)
    # 3. Call the same function on the right subtree
    right_height = tree_height(root.right)
    
    # 4. Join the results
    return max(left_height, right_height) + 1 # +1 is for the root node

# ========== EXAMPLE 4: CHECK IF VALUE EXISTS IN TREE ==========
def check_if_exists(root, value):
    # 1. base cases
    if not root:
        return False
    
    # 2. call function on left subtree
    in_left = check_if_exists(root.left, value)
    # 3. Call the same function on the right subtree
    in_right = check_if_exists(root.left, value)

    # 4. Join the results
    return root.val == value or in_left or in_right

# ========== EXAMPLE 5: REVERSE BINARY TREE (LEFT AND RIGHT) ==========
def reverse_tree(root):
    # 1. base cases
    if not root:
        return
    
    # 2. call function on left subtree
    reverse_tree(root.left)
    # 3. Call the same function on the right subtree
    reverse_tree(root.right)

    # 4. Join the results
    root.left, root.right = root.right, root.left



# BINARY TREE ITERATIVE (DFS) ##################################################################################################


# BINARY TREE ITERATIVE (BFS) ##################################################################################################
# General steps:
    # 1. Create queue with only root in it
    # 2. While queue is not empty, pop 1st element from queue
    # 3. Process this node
    # 4. Append node.left and node.left to queue, if not null