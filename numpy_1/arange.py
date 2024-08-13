# arange - array Range - elements in a given range will form the matrix
# will be created in 1D
import numpy as np
ar1= np.arange(1,10)
print(ar1)

ar2 = np.arange(10,26)
print(ar2)

# ar3 = np.arange(1,26) # create in 1D
# ar4 = ar3.reshape([5,5]) # convert to 2D
ar4 = np.arange(1,26).reshape([5,5])
print(ar4)

ar5 = np.arange(1,31).reshape([1,6,5])
print(ar5)

ar6 = np.arange(1,21,2) #step count
print(ar6)