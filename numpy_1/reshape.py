import numpy as np

# 2-D (3,4)
ar1 = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,1]])
print(ar1)
print(ar1.reshape([4,3])) #convert to (4,3)
# total number of elements(size) should be same
print(ar1.reshape([2,6]))