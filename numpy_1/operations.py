import numpy as np

# 2-D (3,3)
ar1 = np.array([[1,2,3],[2,3,4],[1,2,3]])
print(ar1)
print(ar1.shape) # (3,3)
print(ar1.reshape([9])) # 1D
print(ar1.reshape([1,3,3])) #3D