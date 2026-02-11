#knowing the array data type ( arr.dtype)
import numpy as np
arr=np.array([1.9,2.4,2.9,1.3,-1.2])
print(arr.dtype)

arr1=np.array([1,2,3,4,5])
print(arr1.dtype)

#converting array data type  ( arr.astype('data type'))
newarr=arr.astype('i')
print(newarr)