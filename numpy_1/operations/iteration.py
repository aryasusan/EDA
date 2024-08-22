import numpy as np

ar = np.array([2,3,4,5,6,7,3]) #1D
# for i in ar:
    # print(i)

ar1 = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,1]])
# for i in ar1:
#     for j in i:
        # print(j)


ar2 = np.array([[[1,2,3,4],[2,3,4,5]]])
for i in ar2:
    for j in i:
        for k in j:
            print(k)