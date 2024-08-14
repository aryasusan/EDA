import numpy as np

a = np.array([2,3,4,5])
b = np.array([4,5,6,7])
c = np.dot(a,b)
print(c)
# dot_product is the sum of product of elements
# for 1D it will be a scalar value
# dot_prod = [2*4 + 3*5 + 4*6 + 5*7]

a = np.array([[2,3,4],[4,5,6],[8,2,3]])
b = np.array([[7,6,4],[1,5,9],[3,5,3]])
c = np.dot(a,b)
print(c)
# for 2D sum of (row * column)
# [[
# 2*7 + 3*1 + 4*3     2*6 +3*5 + 4*5   2*4 + 3*9 +4*3
# 4*7 + 5*1 + 6*3     4*6 +5*5 + 6*5   4*4 + 5*9 +6*3
# 8*7 + 2*1 + 3*3     8*6 +2*5 + 3*5   8*4 + 2*9 +3*3
# ]]
# [[29 47 47]
#  [51 79 79]
#  [67 73 59]]
