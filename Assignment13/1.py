"""1) Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]]"""

import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

# Replace NaN with 0
arr = np.nan_to_num(arr, nan=0)

print("Array after replacing NaN with 0:")
print(arr)

arr_t = arr.T

print("\nAfter Interchanging Rows and Columns:")
print(arr_t)
