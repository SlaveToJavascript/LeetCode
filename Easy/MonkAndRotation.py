# https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/

# GIVEN:
    # Integer array A of size N
    # Integer K
"""
    The first line will consist of one integer T denoting the number of test cases.
    For each test case:
    1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
    2) The next line consists of N space separated integers , denoting the elements of the array A.
"""

# TASK:
    # Rotate the array in the right direction by K steps
    # Print the resultant array

# OUTPUT:
    # Print the required array

# SAMPLE INPUT:
    # 1
    # 5 2
    # 1 2 3 4 5
# SAMPLE OUTPUT
    # 4 5 1 2 3

T = int(input())

def rotate_by_k(arr, k):
    k %= len(arr) # If k > len(arr), the final actual number of rotations is the remainder of k/len(arr)
    arr = arr[-k:] + arr[:-k] # Rotation: moving the last k digits to the front
    return arr

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = rotate_by_k(A, K)
    print(*A) # Print array A as a string separated by spaces

# Time complexity = O(n), n = length of array
    # map() functions are O(n) each
# Space complexity = ???