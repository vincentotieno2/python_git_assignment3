import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
print(arr.ndim) #number of dimensions
print(arr.shape) #size of the array

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim) #number of dimensions
print(arr.shape)

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr.ndim)
print(arr.shape) # layer, row, column

print(arr[1,0,1])