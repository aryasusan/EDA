import numpy as np
a = np.array([6,4,21,5,6,73,8,9,2,1,5])

b= np.sort(a) # ascending
print(b)

c= np.sort(a)[::-1] # descending
# c= b[::-1]
print(c)

# sort the array in ascending and returns the index of the element
ascend_index = np.argsort(a)
print(ascend_index)

descend_index = np.argsort(-a)
print(descend_index)