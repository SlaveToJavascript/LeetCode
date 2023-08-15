# ARRAYS ##################################################################################################

# GET SUB-MATRIX FROM MATRIX
# Get subset of array with element at index (i,j) being topleft and (x,y) being bottom-right element of new array

array = [
    [0,  1,  2,  3],
    [4,  5,  6,  7],
    [8,  9,  10, 11],
    [12, 13, 14, 15]
]

i, j = 0, 0
x, y = 2, 2

print([elem[j : y+1] for elem in array[i : x+1]])

#==========================================================================================================

# TRANSPOSE N x N MATRIX
# Transpose = rows become columns, columns become rows

# e.g. matrix = [[1,2,3],
               # [4,5,6],
               # [7,8,9]]
# becomes:      [[1,4,7],
              #  [2,5,8],
              #  [3,6,9]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
  for j in range(i+1, len(matrix)):
      matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#==========================================================================================================

# Check if any / all elements in array satisfies x condition
# e.g. return True if array contains even integers

array = [1, 3, 5]

print(any(x % 2 == 0 for x in array)) # for: ANY
print(all(x % 2 == 0 for x in array)) # for: ALL

#==========================================================================================================

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






# STRINGS #################################################################################################

# Remove a character from string at specific index
index = 4
string = "hello"
new_string = string[:index] + string[index+1:]

#==========================================================================================================

# Reverse string
string = "hello"
reversed_string = string[::-1] # Output = "olleh"

#==========================================================================================================

# Split string into array of characters
string = "hello"
chars_array = [*string] # Output = ['h', 'e', 'l', 'l', 'o']





# HASHMAPS ################################################################################################

# Sort hashmap by STRING value
hashmap = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1]) # ascending
sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=True) # descending
# values in hashmaps have an index of 1 in the hashmap
# Output: [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]

# Sort hashmap by INTEGER value
hashmap = {'a': 120, 'b': 104, 'f': 150, 'c': 132, 't': 125}
sorted_hashmap = sorted(hashmap.items(), key=lambda x:int(x[1]))





# GRAPHS #################################################################################################

# convert array of edges into graph adjacency list (hashmap)
edges = [[1,2], [2,3], [3,4], [4,5], [5,6], [6,1]]

graph = {c:[] for c in range(n)} # n is the number of nodes in graph -> nodes are numbered 0 to n-1

for s, e in edges:
    graph[s].append(e)
    graph[e].append(s)

# OR

graph = {}
  
for a, b in edges:
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
        
    graph[a].append(b)
    graph[b].append(a)

# BINARY TREES ############################################################################################

# Preorder traversal (parent → left → right)
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Inorder traversal (left → parent → right)
def inorder(root):
  return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Postorder traversal (left → right → parent)
def postorder(root):
  return postorder(root.left) + postorder(root.right) + [root.val] if root else []