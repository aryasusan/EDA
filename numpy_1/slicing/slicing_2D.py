import numpy as np

a = np.array([[2,3,4,5,6],[7,8,9,2,3],[4,3,4,5,2],[2,1,8,7,8]])
print(a[:2,:4])

# a[row_slice, column_slice]

# column  0 1 2 3 4
#  row 0 [2,3,4,5,6]
#      1 [7,8,9,2,3]
#      2 [4,3,4,5,2]
#      3 [2,1,8,7,8]

# sliced = [[2 3 4 5]
#           [7 8 9 2]]


print(a[:4,1:5]) # row index = 0,1,2,3  column_index= 1,2,3,4
# [[3 4 5 6]
#  [8 9 2 3]
#  [3 4 5 2]
#  [1 8 7 8]]

print(a[1:4,2:5]) # row index = 1,2,3  column_index= 2,3,4
# [[9 2 3]
#  [4 5 2]
#  [8 7 8]]

print(a[1::2,1:5:2])  # step 2, row index = 1,3  column_index= 1,3
# [[8 2]
#  [1 7]]

print(a[::2,::2]) # row index = 0,2  column_index= 0,2,4
# [[2 4 6]
#  [4 4 2]]