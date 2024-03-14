# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix/description/
# MEDIUM
# Tags: matrixlc, bfslc, dplc, graphlc, #542

# GIVEN:
    # an m x n binary matrix, mat

# TASK:
    # return the distance of the nearest 0 for each cell
    # The distance between two adjacent cells is 1

# EXAMPLES:
    # Input: mat = [[0,0,0],
                #   [0,1,0],
                #   [0,0,0]]
    # Output: [[0,0,0],
            #  [0,1,0],
            #  [0,0,0]]

    # Input: mat = [[0,0,0],
                #   [0,1,0],
                #   [1,1,1]]
    # Output: [[0,0,0],
            #  [0,1,0],
            #  [1,2,1]]

###########################################################################################################

# ✅ ALGORITHM 1: BFS (WITH VISITED SET i.e. not space optimized)
# NOTE: approach: instead of focusing on the 1's, we focus on the 0's and update their neighbors, which are 1's, with the respective distance-from-0 values
# Create result matrix of the same dimensions as input matrix
# Create queue and "visited" set
# For every element in matrix, 
    # if element = 0, add it to queue, and add it to visited hashset
        # any q[i] = (r, c, distance_to_nearest_0)
        # we add 0's to visited as we don't need to visit them again (when they become neighbors of some cell), since their distance to nearest 0 is 0
# While queue is not empty, pop current element (and distance from 0) from queue
    # if current element's neighbor is not visited, increment current neighbor's distance from 0 by 1, and in result matrix, update current neighbor's cell with its updated distance-from-0 value
    # add current neighbor to visited
    # add current neighbor to queue, with incremented distance from 0
# Return result matrix

# TIME COMPLEXITY: O(m * n)
    # m = height of matrix, n = length of matrix
# SPACE COMPLEXITY: O(m * n)
    # result array is m * n size
    # set and queue are each approx. m*n size

def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    result = [[0] * len(row) for row in mat]
    q = []
    visited = set()

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == 0:
                q.append((r, c, 0))
                visited.add((r, c))
    
    # Perform bfs to update distance from 0 for each neighbor node
    while q:
        r, c, dist = q.pop(0) # popped elements are 0's and neighbors of 0's

        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # 4 neighbors, 1 in each direction
            nr, nc = r+x, c+y # index row and col of current neighbor
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited: # if current neighbor is within matrix and it is not visited,
                result[nr][nc] = dist + 1 # update current neighbor's distance-from-0 value; since mat(nr,nc) is an immediate neighbor of mat(r,c), the distance-from-0 value of mat(nr, nc) = distance-from-0 value of mat(r,c) + 1
                visited.add((nr, nc))
                q.append((nr, nc, dist + 1)) # add current neighbor to queue, with its updated distance-from-0 value
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: BFS (WITHOUT VISITED SET i.e. space optimized)
# NOTE: approach: instead of focusing on the 1's, we focus on the 0's and update their neighbors, which are 1's, with the respective distance-from-0 values
# Same as above, except we are modifying the matrix in-matrix (i.e. no additional result matrix to return)
# we mark out the 1's until they are updated; everything else (that are not marked) are already updated by previous iterations
# We also don't need a 3rd element in each tuple in the queue (i.e. the distance-from-0 value) to keep track of it

# TIME COMPLEXITY: O(m * n)
    # m = height of matrix, n = length of matrix
# SPACE COMPLEXITY: O(m * n)
    # length of queue might be m*n in the worst case scenario (if matrix contains all 0's)
    # but space complexity is still much better than above as we don't create visited hashset and result matrix

def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    q = []

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == 0:
                q.append((r, c)) # add all 0's to q
            else: # if cell = 1
                mat[r][c] = -1 # mark out all cells that require updating; all other cells (except the -1) are cells that are already updated with distance-from-0 values
    
    # Perform bfs to update distance-from-0 for each neighbor node
    while q:
        r, c = q.pop(0) # popped elements are 0's and neighbors of 0's

        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # 4 neighbors, 1 in each direction
            nr, nc = r+x, c+y # index row and col of current neighbor
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1: # if current neighbor is within matrix and is not visited (if mat(r,c) = -1, it means it's unvisited/un-updated)
                mat[nr][nc] = mat[r][c] + 1 # update current neighbor's distance-from-0 value ; since mat(nr,nc) is an immediate neighbor of mat(r,c), the distance-from-0 value of mat(nr, nc) = distance-from-0 value of mat(r,c) + 1
                q.append((nr, nc)) # add current neighbor to queue, with its updated distance-from-0 value
    
    return mat

#==========================================================================================================

# ✅ ALGORITHM 3: DYNAMIC PROGRAMMING
# MAIN IDEA: 
    # 1) traverse the whole matrix from the element in the top-left corner to the element in the bottom-right corner, checking the element above and left of each "1" cell
        # The minimum distance-to-0 value of current cell = 1 + the minimum of the distance-to-0 values of the cells above and to the left of current cell
            # if current cell is at the border and doesn't have a cell above/left of it, we set above/left as infinity so that it will not become the value assigned to current cell when comparing above and left cells for the minimum of the 2
    # 2) traverse the whole matrix in the reverse direction, i.e., from the element in the bottom-right corner to the element in the top-left corner, checking the element below and right of each non-zero cell
        # The minimum distance-to-0 value of the current cell = 1 + the minimum of the distance-to-0 values of the cells below and to the right of current cell
            # if current cell is at the border and doesn't have a cell below/right of it, we set below/right as infinity so that it will not become the value assigned to current cell when comparing below and right cells for the minimum of the 2
        # Then, we compare this minimum result with the previously stored minimum result in current cell, updating it with the smaller of the 2 values
    # 3) We return the matrix with the updated distance-to-0 values

# TIME COMPLEXITY: O(m * n), where m = height of matrix, n = length of matrix
# SPACE COMPLEXITY: O(1)
    # no extra space is needed

def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])

    # traverse the whole matrix from the element in the top-left corner to the element in the bottom-right corner, checking the element above and left of each "1" cell
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                above = mat[r-1][c] if r > 0 else float('inf')
                left = mat[r][c-1] if c > 0 else float('inf')
                mat[r][c] = 1 + min(above, left)
    
    # traverse the whole matrix in the reverse direction, i.e., from the element in the bottom-right corner to the element in the top-left corner, checking the element below and right of each non-zero cell
    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            if mat[r][c] != 0:
                below = mat[r+1][c] if r < rows-1 else float('inf')
                right = mat[r][c+1] if c < cols-1 else float('inf')
                mat[r][c] = min(mat[r][c], below + 1, right + 1) # we compare the minimum between right and below, with previously stored minimum result in current cell, updating it with the smaller of the 2 values
    
    return mat