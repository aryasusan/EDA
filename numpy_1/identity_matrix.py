# identity matrix - square matrix with diagonal element will be 1 and other elemts will be 0
# only in 2D as it is to be square matrix
# to create use either identity(size) or eye(size)

import numpy as np
ar1 = np.identity(4,dtype=int)
print(ar1) #(4,4)

ar2 = np.eye(5,dtype=int)
print(ar2)