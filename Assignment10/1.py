"""1) Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]] """
import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

print("Original Array:")
print(arr)


arr = np.nan_to_num(arr, nan=0)

print("\nAfter replacing NaN with 0:")
print(arr)

arr[[0, 1]] = arr[[1, 0]]

print("\nAfter interchanging rows:")
print(arr)

arr = arr[:, [2, 1, 0, 3]]

print("\nAfter interchanging columns:")
print(arr)
