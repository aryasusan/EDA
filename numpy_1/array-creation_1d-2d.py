import numpy as np

ar = np.array([2,3,4,5,6,7,3]) #1D
print(ar)
print(ar.ndim) # to find the dimension-1
print(ar.shape) # to find the order of the array (7)


# 2-D (3,4)
ar1 = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,1]])
print(ar1)
print(ar1.ndim) # 2
print(ar1.shape) # (3,4)

# ar2 = np.array([[1,2,3,4],[2,5,6,7],[3,8,4,6],[9,6,4,2]])
# print(ar2)
# print(ar2.ndim) # 2
# print(ar2.shape) # (4,4)
#
# ar3 = np.array([[1,2,3],[2,5,6],[3,8,4],[9,6,4],[9,2,3]])
# print(ar3)
# print(ar3.ndim) # 2
# print(ar3.shape) # (5,3)