import numpy as np

a = np.array([[1,2,3,4],[2,5,6,7],[3,8,4,6],[9,6,4,2]]) #2D
print(np.sum(a)) # sum of all elements

# can find the sum of each elements in rows or columns using axis value
#  axis=0 --> column
#  axis=1 --> row

column_sum = np.sum(a,axis=0)
print(column_sum, "= column_sum")

row_sum = np.sum(a,axis=1)
print(row_sum, "= row_sum")