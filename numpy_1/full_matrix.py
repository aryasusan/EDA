# the defined element will form the matrix

import numpy as np

ar1 = np.full([4],3)
print(ar1) #1D with value 3--4 times, default datatype will be int

ar2 = np.full([3,4],6)
print(ar2)

ar3 = np.full([1,3,4],8)
print(ar3)