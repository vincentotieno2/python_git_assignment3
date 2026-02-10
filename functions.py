#this is a file containing practice on arrays
import numpy as np
arr=np.array(["a","b","c"])
print(arr)
arr=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,1])
print(arr[0,2])
print(arr[0,3])
print(arr.ndim)

arr=np.array([1,2,3,4,5,6,7])
print(arr[2])

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr.ndim)
print(arr.shape)

print(arr[1,0,1])