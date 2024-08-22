# ceil converts a decimal element to its next higher integer

# 3.6 ==> 4
# 3.1 ==> 3
# 1.1 ==> 2

import numpy as np

a = np.array([[3.2,4.5,6.1,8.9],[2.3,5.4,6.8,7.1],[3.2,8.5,4.6,6.7],[9.3,6.4,4.6,2.5]])
b = np.ceil(a)
print(b)