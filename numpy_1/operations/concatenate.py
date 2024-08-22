import numpy as np

a = np.array([2,3,4,5,6,7,3,4,5,6])
b = np.array([5,7,8,9,6,1,2])

c = np.concatenate((a,b))
# print(c)

a = np.array([[1,2,3],[2,3,4],[4,5,6],[3,4,5]])
b = np.array([[6,2,4],[5,8,9],[5,3,2]])
c = np.concatenate((a,b))
d = np.concatenate((a,b),axis=1) # order shud be same for row wise concatenation
a = np.array([[1,2,3],[2,3,4],[4,5,6]])
e = np.concatenate((a,b),axis=1)
print(c)
print(d)
print(e)