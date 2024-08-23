import numpy as np

ar1 = np.array([[1,2,3,4],[2,3,4,5]]) # 2-D (2,4)
print(ar1)
print(ar1.ndim) # 2
print(ar1.shape) # (2,4)
print(ar1.size) #number of elements
print(ar1.dtype) # int64

#create 3*4 in 3D implies its order/shape will be (1,3,4)- (z,x,y) where z will be 1 always in 3d
# 3D (1,2,4)
ar2 = np.array([[[1,2,3,4],[2,3,4,5]]])
print(ar2)
print(ar2.ndim) # 3
print(ar2.shape) # (1,2,4)


# 3D (1,5,5)
ar3 = np.array([[[1,2,3,4,2],[2,3,4,5,6],[6,7,3,8,2],[8,9,4,5,6],[5,7,6,4,7]]])
print(ar3)
print(ar3.ndim) # 3
print(ar3.shape) # (1,5,5)