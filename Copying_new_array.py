#name of array.copy is one of the ways to copy an array.
import numpy as np
arr1=np.array([1,2,3])
arr2=arr1.copy()
print(arr2) #output is [1,2,3]

arr2[0]=10
print(arr2) #output is [10,2,3]
print(arr1) #output is [1,2,3]




