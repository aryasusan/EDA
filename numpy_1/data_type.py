import numpy as np

ar = np.array([2,3,4,5,6,7,3]) #1D
print(ar.dtype) # int64

ar1 = np.array([2,3,4.5,5,6,7,3]) #1D
print(ar1.dtype) # float64

# to change datatype---
ar2 = np.array([2,3,45,5,6,7,3],dtype=float)
print(ar2) #[ 2.  3. 45.  5.  6.  7.  3.]
print(ar2.dtype)