import numpy as np

# 2-D (4,5)
ar1 = np.array([[1,2,3,4,5],[2,3,4,5,8],[1,2,3,4,5],[2,3,4,5,8]])
print(ar1)
print(ar1.shape) # (4,5)
print(ar1.reshape([5,4]))
print(ar1.reshape([2,10]))
print(ar1.reshape([20])) # 1D
print(ar1.reshape([1,5,4])) #3D