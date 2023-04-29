# https://www.hackerearth.com/problem/algorithm/monk-and-inversions-arrays-strings-e5aaa427/
# Explanation: https://www.youtube.com/watch?v=ys5ZTg0yIWY&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=45

# GIVEN:
    # Integer matrix M of size N x N
"""
    First line consists of a single integer T denoting the number of test cases.
        First line of each test case consists of one integer denoting N. 
        Following N lines consists of N space separated integers denoting the matrix M.
"""

# TASK
    # Iterate through each element in the matrix M
    # For each element, form a square from that element in the matrix where that element is the topmost, leftmost element in the square
    # Return the sum of the number of integers smaller than each iterated element in the matrix

# OUTPUT
    # Print the required sum for each test case

# SAMPLE INPUT
"""
    2
    3
    1 2 3
    4 5 6
    7 8 9
    2
    4 3
    1 4
"""
# SAMPLE OUTPUT
    # 0
    # 2

    # In first test case there is no pair of cells (x1, y1), (x2, y2), x1 <= x2 and y1 <= y2 having M[x1][y1] > M[x2][y2], so the answer is 0.
    # In second test case M[1][1] > M[1][2] and M [1][1] > M[2][1], so the answer is 2.

T = int(input())

# Return the count of the number of elements < element at the topmost leftmost corner of matrix
def count_less_than(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < matrix[0][0]:
                count += 1
    return count

for _ in range(T):
    count = 0
    arr = []
    N = int(input())
    # Get matrix into array form
    for _ in range(N):
        li = list(map(int, input().split()))
        arr.append(li)
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sub_matrix = [elem[j:] for elem in arr[i:]] # For each element in matrix, form a new sub-matrix where that element is the topmost, leftmost element in the sub-matrix
            count += count_less_than(sub_matrix)
    print(count)

# Time complexity = O(N^4)
# Space complexity = O(N^2)