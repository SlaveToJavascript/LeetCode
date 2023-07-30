# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# MEDIUM
# Tags: heaplc, minheaplc, matrixlc, binarysearchlc, #387
# Also works for Kth Smallest Number in M Sorted Lists (KthSmallestNumberInMSortedLists)

# GIVEN:
    # n x n matrix where each of the rows and columns is sorted in ascending order,

# TASK:
    # return the kth smallest element in the matrix
    # NOTE: You must find a solution with a memory complexity better than O(n^2)

# EXAMPLES:
    # Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    # Output: 13
    # Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

    # Input: matrix = [[-5]], k = 1
    # Output: -5

###########################################################################################################

# ✅✅✅ ALGORITHM 1: MIN-HEAP
# Since we know each row and column of the matrix is sorted in ascending order, we can add elements to minHeap from left to right
# 1) Push the 1st element of each array within the matrix into min-heap along with the index of the array within the matrix and the index of the element within the list
    # i.e. any minHeap[i] = (number, index_of_arr_within_matrix, index_of_number_within_arr)
# 2) while minHeap is not empty and numbers processed (popped from minHeap) < k:
    # pop smallest no. from minHeap (every time we pop a smallest no. from minHeap, it means we processed a no., i.e. we are closer to getting the kth smallest no.)
    # break out of while-loop if current number is the kth number processed/popped
    # check if, in the array where this popped element came from, there are any more elements behind the element that got popped (within the array)
        # if there are, push this next element in this array into minHeap
# 3) return the last popped element from minHeap (i.e. the kth smallest element)

# TIME COMPLEXITY: O((n+k) log n)
    # TC of 1st step (pushing 1st element of each array in matrix to minHeap) = O(n log n)
        # n elements will be pushed to the heap * each push operation is O(log n) => O(n log n)
    # TC of while-loop = O(k log n) because we repeat the while-loop k times until the kth smallest no. is found; each while loop has push operation which is O(log n) each
    # O(n log n) + O(k log n) = O((n+k) log n)
    # NOTE: in the worst case when k = n^2, TC = O(n^2 log n)
# SPACE COMPLEXITY: O(n)
    # minHeap will contain at most n elements

from heapq import heappush, heappop

def kthSmallest(matrix, k):
    n = len(matrix)
    minHeap = [] # any minHeap[i] = (no., index_of_arr_within_matrix, index_of_no._within_arr)

    # push the 1st elem of each array in matrix into minHeap
    for i in range(n):
        heappush(minHeap, (matrix[i][0], i, 0))
    
    nums_checked = 0 # if nums_check = k, we've found k smallest element
    while minHeap and nums_checked < k:
        smallest_num, matrix_idx, arr_idx = heappop(minHeap)
        nums_checked += 1 # popping the smallest no. from minHeap means we've checked a no.

        # check if, in the array where this popped element came from, there are any more elements behind the element that got popped
        if arr_idx < n-1:
            heappush(minHeap, (matrix[matrix_idx][arr_idx+1], matrix_idx, arr_idx+1))
        
    return smallest_num # return the last popped element from minHeap (i.e. the kth smallest element)

#==========================================================================================================

# ✅ ALGORITHM 2: BINARY SEARCH (HARD!)
# Solution from https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/1322101/c-java-python-maxheap-minheap-binary-search-picture-explain-clean-concise/

# Define helper method countLessOrEqual(num), where countLessOrEqual(x) returns the no. of elements in matrix that are less than or = x
# MAIN IDEA: binary search to find the smallest number, ans, within the range [ min_no._in_matrix, max_no._in_matrix ] such that the no. of elements that are less than or = ans is greater than or = k

# STEPS:
    # 1) Start with left = min no. in matrix = matrix[0][0], and right = max no. in matrix = matrix[n-1][n-1]
    # 2) Find the mid of left and right (this mid is not necessarily a no. in matrix)
    # 3) If countLessOrEqual(mid) >= k (i.e. if no. of elements in matrix that are less than or = mid is greater than or = k), we search in the left side (i.e. right = mid) and do ans = mid
        # else, search in the right side, (i.e. left = mid)
    # 4) Since ans is the smallest value where countLessOrEqual(ans) >= k, it's the kth smallest element in the matrix

# How to count no. of elements <= x efficiently?
    # Since matrix is sorted in ascending order by rows and cols, use 2 pointers r and c, where r points to the 1st row and c points to the last col
        # If matrix[r][c] <= x, then the no. of elements in row r that are <= x is c+1 (because row[r] is sorted in ascending order, so if matrix[r][c] <= x then matrix[r][c-1] is also <= x)
        # Else if matrix[r][c] > x, decrease column c until matrix[r][c] <= x (because column is sorted in ascending order, so if matrix[r][c] > x then matrix[r+1][c] is also > x => so we have to decrease c)
    # TIME COMPLEXITY = O(m + n)

# TIME COMPLEXITY: O((m+n) log (max-min))
    # m = no. of rows
    # n = no. of cols
    # max-min = difference between the max and min elements in matrix
# SPACE COMPLEXITY: O(1)

def kthSmallest(matrix, k):
    rows, cols = len(matrix), len(matrix[0])

    def countLessOrEqual(x):
        count = 0
        c = cols - 1  # start with the rightmost column
        for r in range(rows):
            while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
            count += (c + 1)
        return count

    left, right = matrix[0][0], matrix[-1][-1]
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if countLessOrEqual(mid) >= k:
            ans = mid
            right = mid - 1  # try to looking for a smaller value in the left side
        else:
            left = mid + 1  # try to looking for a bigger value in the right side

    return ans