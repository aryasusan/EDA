import numpy as np

ar1 = np.array([[1,2,3],[4,5,6],[7,6,5]])
ar2 = np.array([[6,8,4],[9,7,5],[2,5,3]])

# Addition,subtraction,Multiplication, division- element by element , order shud be same
#


sum = np.add(ar1,ar2)
print(sum)
# [[ 7 10  7]
#  [13 12 11]
#  [ 9 11  8]]

diff = np.subtract(ar1,ar2)
print(diff)
# [[-5 -6 -1]
#  [-5 -2  1]
#  [ 5  1  2]]

prod = np.multiply(ar1,ar2)
print(prod)
# [[ 6 16 12]
#  [36 35 30]
#  [14 30 15]]

div = np.divide(ar1,ar2)
print(div)

