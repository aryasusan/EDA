import numpy as np

a = np.array([2,3,4,5,6,7,3]) #1D

b = a>4
print(b)
c = a[b]
print(c)

d = a%2==0 #collect even num
c = a[d]
print(c)