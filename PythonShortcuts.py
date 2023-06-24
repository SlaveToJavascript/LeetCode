# ARRAYS =================================================================================================

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

#########################################################################################################

# Check if any / all elements in array satisfies x condition
# e.g. return True if array contains even integers

array = [1, 3, 5]

print(any(x % 2 == 0 for x in array)) # for: ANY
print(all(x % 2 == 0 for x in array)) # for: ALL

#########################################################################################################

# Unpacking arrays
colors = ['red', 'blue', 'green']
color1, color2, color3 = colors
# color1 = 'red'
# color2 = 'blue'
# color3 = 'green'

# If you don't need to assign variables to all values:
colors = ['cyan', 'magenta', 'yellow', 'black']
color1, color2, *other = colors
# color1 = 'cyan'
# color2 = 'magenta'
# other = ['yellow', 'black'] ***






# STRINGS ===============================================================================================

# Remove a character from string at specific index
index = 4
string = "hello"
new_string = string[:index] + string[index+1:]

###########################################################################################################

# Reverse string
string = "hello"
reversed_string = string[::-1] # Output = "olleh"

#########################################################################################################

# Split string into array of characters
string = "hello"
chars_array = [*string] # Output = ['h', 'e', 'l', 'l', 'o']





# HASHMAPS ==============================================================================================

# Sort hashmap by STRING value
hashmap = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1]) # ascending
sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=True) # descending
# values in hashmaps have an index of 1 in the hashmap
# Output: [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]

# Sort hashmap by INTEGER value
hashmap = {'a': 120, 'b': 104, 'f': 150, 'c': 132, 't': 125}
sorted_hashmap = sorted(hashmap.items(), key=lambda x:int(x[1]))