# zero matrix - all elements in the array will be 0
# to create a zero matrix, use zero function and pass the order in square brackets

import numpy as np
ar1 = np.zeros([3,4])
print(ar1) # the elements will be in float,so--

ar1 = np.zeros([3,4],dtype=int)
print(ar1)

ar2 = np.zeros([4,5],dtype=int)
print(ar2) # 2D

# 1d with 10 zeroes
ar3 = np.zeros([10],dtype=int)
print(ar3)

ar4 = np.zeros([1,5,4],dtype=int)
print(ar4) # 3D

ar5 = np.zeros([2,5,4],dtype=int) # 2 times 5,4 matrix will be printed with dimension 3D
print(ar5) # 3D
