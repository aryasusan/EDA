import numpy as np

a = np.array([[5,6,3,2],[2,5,6,7],[3,8,4,6],[9,6,4,2]]) #2D
print(a,'original array')

b = np.sort(a) #--> row sorting
print(b,'row sort')

c = np.sort(a,axis=0) #column sorting
print(c,'column sort')

# sort the array in  row ascending and returns the matrix of the index of the element
ascend_index = np.argsort(a)
print(ascend_index,'row ascending index')

descend_index = np.argsort(-a)
print(descend_index, 'row descending index')

# sort the array in  column ascending and returns the matrix of the index of the element
ascend_index = np.argsort(a,axis=0)
print(ascend_index, 'column ascending index')

descend_index = np.argsort(-a,axis=0)
print(descend_index, ' column descending index')

# get the descending sorting indices of row and returns the matrix of indices:
desc_index = np.argsort(-a)
print(desc_index)
#get the row elements in the corresponding sorted indices
desc_order = np.take_along_axis(a,desc_index,axis=1)
print(desc_order)

# get the descending sorting indices of column and returns the matrix of indices:
desc_index = np.argsort(-a,axis=0)
print(desc_index)
#get the column elements in the corresponding sorted indices
desc_order = np.take_along_axis(a,desc_index,axis=0)
print(desc_order)