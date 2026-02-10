import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[4:9]) # [5,6,7,8,9]
print(arr[-3:])

#slicing 2D Arrays (row slice, column slice)
arr=np.array([[1,2,3],[4,5,6], [7,8,9]])
print(arr[0:2,:]) #output [[1,2,3],[4,5,6]]
print(arr[:,0:2]) # print all rows, print the first 2 columns(0 and 1)

#3D arrays layers, columns and rows
arr=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr[0]) #print the first layer of the 3D array
print(arr[:,1,:]) #print the second row of all the layers and columns
print(arr[:,:,1:]) #all layers and rows, from column 1 onwards

