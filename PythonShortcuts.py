# ARRAYS ===================================================================================================

# GET SUB-MATRIX FROM MATRIX
# Get subset of array with element at index (i, j) being topmost, leftmost element of new array
# https://www.delftstack.com/howto/python/python-subarray/

array = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

i = 1
j = 2

print([elem[j:] for elem in array[i:]])

###########################################################################################################

# Check if any / all elements in array satisfies x condition
# e.g. return True if array contains even integers

array = [1, 3, 5]

print(any(x % 2 == 0 for x in array)) # for: ANY
print(all(x % 2 == 0 for x in array)) # for: ALL

# STRINGS ===================================================================================================

# Remove a character from string at specific index
index = 4
string = "hello"
new_string = string[:index] + string[index+1:]

###########################################################################################################

# Reverse string
string = "hello"
reversed_string = string[::-1]

###########################################################################################################
