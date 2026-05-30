# 4) Practice operations like Get the maximum value from given array
# Get the minimum value from given array Find the number of rows and columns of a given array
# using NumPy Select the elements from a given array (each element and specific element)
# Find the sum of values in a 2D array using for loop
# Adding, Subtracting, multiplying, dividing arrays in Numpy
import pandas as pd
import numpy as np
arr = np.array([22, 54, 21, 78, 55, 11, 90, 34])
print(arr.max())
print(arr.min())
print(arr.size)
print(arr.shape)
print(arr[4])
arr1 = np.array([
    [22, 56, 87, 43, 41],
    [22, 90, 11, 23, 65]
])
for i in arr1:
    a = sum(i)
    print(a, a.dtype)

arr2 = np.array([3, 4, 2, 5])
arr3 = np.array([6, 3, 2, 0])
arr4 = np.array([
    [3, 4, 5, 6],
    [1, 6, 2, 0]
]
)
res1 = arr4 + arr3
print(res1)
res2 = arr3 - arr2
print(res2)
res4 = arr2 * arr4
print(res4)
res5 = arr3 / arr2
print(res5)
