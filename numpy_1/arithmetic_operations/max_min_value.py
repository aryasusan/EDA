import numpy as np

a = np.array([2,3,4,5,6,7,3]) #1D
print(a)
print(np.max(a))
print(np.argmax(a)) #index of the max value
print(np.min(a))
print(np.argmin(a)) #index of the min value

b = np.array([[1,2,3,4],[2,5,6,7],[3,8,4,6],[9,6,4,2]]) #2D
print(b)
print(np.max(b)) # max value in the array
print(np.max(b,axis=0)) # column wise max
print(np.max(b,axis=1)) # row wise max

print(np.argmax(b)) # index of first occurence of max value in the array
print(np.argmax(b,axis=0)) # index of column wise max
print(np.argmax(b,axis=1)) # index of row wise max

print(np.min(b)) # min value in the array
print(np.min(b,axis=0)) # column wise min
print(np.min(b,axis=1)) # row wise min

print(np.argmin(b)) # index of min value in the array
print(np.argmin(b,axis=0)) # index of column wise min
print(np.argmin(b,axis=1)) # index of row wise min

