#joining numpy arrays
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

arr3=np.array([21,22,23,24,25,26,27,28,29])
arr4=np.array([30,31,32,33,34,35])
arr5=np.concatenate((arr3,arr4))
print(arr5) #[21 22 23 24 25 26 27 28 29 30 31 32 33 34 35]

arr6=np.array([21,22,23,24,25,26,27])
arr7=np.concatenate((arr6,arr5))
print(arr7)