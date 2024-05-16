# 531. Lonely Pixel I
# https://leetcode.com/problems/lonely-pixel-i/
# MEDIUM
# Tags: matrixlc, #531

# GIVEN:
    # an m x n matrix, picture, consisting of black 'B' and white 'W' pixels

# TASK:
    # return the number of black lonely pixels
        # A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels

# EXAMPLES:
    # Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
    # Output: 3
    # Explanation: All the three 'B's are black lonely pixels.

    # Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM 1A: COUNT NO. OF BLACK PIXELS IN EACH ROW AND COLUMN (not space-optimized)
# use an array to store the no. of B's in each row, and use another array to store the no. of B's in each column
# for each B in matrix, check if the corresponding no. of B's in that row and column are both 1

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(m+n)
    # O(m) for row_counts
    # O(n) for col_counts

def findLonelyPixel(picture):
    row_counts = [0] * len(picture) # count of B's in each row
    col_counts = [0] * len(picture[0]) # count of B's in each column
    
    # fill up the counts of B's in each row and column
    for r in range(len(picture)):
        for c in range(len(picture[0])):
            if picture[r][c] == "B":
                row_counts[r] += 1
                col_counts[c] += 1
    
    result = 0 # return value
    for r in range(len(picture)):
        for c in range(len(picture[0])):
            if picture[r][c] == "B" and row_counts[r] == 1 and col_counts[c] == 1: # for each B where there's only 1 B in that row and column,
                result += 1 # it is a lonely black pixel
    
    return result