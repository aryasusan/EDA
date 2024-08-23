import numpy as np

a = np.array([[2,3,4,5,6],[7,8,9,2,3],[4,3,4,5,2],[2,1,8,7,8]])

# column  0 1 2 3 4
#  row 0 [2,3,4,5,6]
#      1 [7,8,9,2,3]
#      2 [4,3,4,5,2]
#      3 [2,1,8,7,8]

# zeroth_row and zeroth column
print(a[0],'zeroth row')
print(a[:,0],'zeroth column')

# last row and last column
print(a[-1],'last row')
print(a[:,-1],'last column')

print(a[-4:-1,-4:-2])
# [[3 4]
#  [8 9]
#  [3 4]]