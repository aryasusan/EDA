# list is an example for 1D
# 1D slicing is same as list slicing
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])


print(a[2:5]) # prints elements from index 2 to index 4
print(a[2:]) # prints from index 2 to end
print(a[:4]) #prints from index 0 to 3
print(a[1:8:2]) # prints elements in index1,3,5,7 -start:stop:step
print(a[1::3]) #prints elements in index1,4,7,10 start::step
print(a[::2]) #prints elements in 0,2,4,6,8 ::step, from start to end with step count

# negative indexing starts from -1 to -n
print(a[::-1]) #from last index
