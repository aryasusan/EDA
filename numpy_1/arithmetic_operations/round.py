# 1.2 ==> 1
# 1.6 ==> 2
# 1.5 ==> 2
# 5.5 ==> 6
# 2.5 ==> 2
# 4.5 ==> 4

#  if .5 is with even number then it rounds  to lowest integer
#  and if .5 is with odd number it rounds to higher integer

import numpy as np

a = np.array([[3.2,4.5,6.1,8.9],[2.3,5.4,6.8,7.1],[3.2,8.5,4.6,6.7],[9.3,6.4,4.6,2.5]])
b = np.round(a)
print(b)