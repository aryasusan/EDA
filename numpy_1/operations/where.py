import numpy as np

a = np.array([2,3,4,5,6,7,3])
b = np.array_split(a,3)
print(b)
print(b[0])