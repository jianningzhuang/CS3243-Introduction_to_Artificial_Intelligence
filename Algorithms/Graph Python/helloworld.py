# 1D Array
rows = 5
cols = 6

oneD_arr = [0 for i in range(cols)]
print(oneD_arr)

# 2D Array
twoD_arr = [[0 for i in range(cols)] for j in range(rows)]
print(twoD_arr)
twoD_arr[0][0] = 1
print(twoD_arr)

# Adjacency Matrix

adj_matrix = []
for i in range(rows):
  col = []
  for j in range(cols):
    col.append(0)
  adj_matrix.append(col)
print(adj_matrix)

# Adjacency List
N = 4
AL = [[] for i in range(N)]
print(AL)