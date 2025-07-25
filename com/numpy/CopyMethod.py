import numpy as np

arr = np.arange(1,10)
print(arr)
arr[3:] = 100
print(arr)
print('--------------------')
arr1= arr
print(arr1)
arr1[3:] = 500
print(arr1)
print('--------------------')
print(arr)

print('--------------------')

arr2 = arr.copy()
print(arr2)
arr2[3:] = 1000
print(arr2)
print('--------------------')
print(arr)
