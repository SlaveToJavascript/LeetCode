# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# MEDIUM
# Tags: matrixlc, bfslc, graphlc, #1926

# GIVEN:
    # an m x n matrix, maze, (0-indexed) with empty cells (represented as '.') and walls (represented as '+')
    # the entrance of the maze, where entrance = [entrance_row, entrance_col] denotes the row and column of the cell you are initially standing at

# TASK:
    # In one step, you can move one cell up, down, left, or right
    # You cannot step into a cell with a wall, and you cannot step outside the maze
    # Your goal is to find the nearest exit from the entrance
        # An exit is defined as an empty cell that is at the border of the maze
        # The entrance does not count as an exit
    # TODO: Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists

# EXAMPLES:
    # Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
    # Output: 1
    # Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
    # Initially, you are at the entrance cell [1,2].
    # - You can reach [1,0] by moving 2 steps left.
    # - You can reach [0,2] by moving 1 step up.
    # It is impossible to reach [2,3] from the entrance.
    # Thus, the nearest exit is [0,2], which is 1 step away.

    # Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
    # Output: 2
    # Explanation: There is 1 exit in this maze at [1,2].
    # [1,0] does not count as an exit since it is the entrance cell.
    # Initially, you are at the entrance cell [1,0].
    # - You can reach [1,2] by moving 2 steps right.
    # Thus, the nearest exit is [1,2], which is 2 steps away.

    # Input: maze = [[".","+"]], entrance = [0,0]
    # Output: -1
    # Explanation: There are no exits in this maze.

###########################################################################################################

# ✅ ALGORITHM: ITERATIVE BFS
# Add entrance coords into queue, with distance from entrance = 0
    # i.e. format of any q[i] = (row, column, distance_from_entrance)
# Mark entrance as visited in the grid
# While q is not empty:
    # Pop first element (cell) from q
    # Check if this cell is on the border of maze (i.e. it is an exit)
        # If yes, return its distance from entrance (which was also popped)
    # if not, check if this cell has any unvisited neighbors that are within the bounds of maze and that are not walls
        # for each unvisited neighbor cell, mark it as visited, and add it to q with updated distance_from_entrance + 1
# return -1 (if we reach this point, it means there was nothing returned previously -> no exits found)

# TIME COMPLEXITY: O(m*n)
    # m = number of rows
    # n = number of columns
    # In the worst-case scenario, we may have to visit O(m⋅n) cells before the iteration stops
# SPACE COMPLEXITY: O(max(m,n))
    # because this is bfs, in the worst case, the q can either store all cells in the row or all cells in the column -> overall space complexity = O(max(m,n))

def nearestExit(maze, entrance):
    rows, cols = len(maze), len(maze[0])

    q = [ (entrance[0], entrance[1], 0) ] # format of q[i] = (row, column, distance_from_entrance)
    maze[entrance[0]][entrance[1]] = '+' # mark entrance cell as visited

    while q:
        r, c, dist = q.pop(0)
        if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and (r,c) != (entrance[0], entrance[1]): # if maze(r,c) is on the boundary of maze and it is not the entrance -> i.e. it is an exit cell
            return dist
        
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r + x, c + y
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".": # if current neighbor cell maze(nr,nc) is within the boundaries of maze and is not visited and not a wall,
                maze[nr][nc] = "+" # mark this neighbor cell as visited
                q.append((nr, nc, dist+1)) # add this neighbor cell to q and update its distance_from_entrance as +1
    
    return -1 # if we reach this point, it means there was nothing returned previously -> no exits found