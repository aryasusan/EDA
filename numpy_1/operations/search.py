# search is used to find the indices of the search element, returns the array of indices

import numpy as np

a = np.array([2,3,4,5,6,7,3,6])
b = np.where(a==6)
c = np.where(a==9)
d = np.where(a>5)
print(b)
print(c) #null array as 9 is not present
print(d)

e = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,1]])
f = np.where(e==4)
print(f)
# (array([0, 1, 2]), array([3, 2, 0])) 1st array represent row, 2nd array represents column
# 4 present in (0,3) (1,2) (2,0)
