import numpy as np
a = np.array([6,4,21,5,6,73,8,9,2,1,5])

b= np.sort(a) # ascending
print(b)

c= np.sort(a)[::-1] # descending
# c= b[::-1]
print(c)