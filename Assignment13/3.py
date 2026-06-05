""" 3) Replace NaN values with average of columns"""

import numpy as np

arr = np.array([[10, np.nan, 30],
                [20, 40, np.nan],
                [30, 50, 60]])

print("Original Array:")
print(arr)

col_mean = np.nanmean(arr, axis=0)

inds = np.where(np.isnan(arr))

arr[inds] = np.take(col_mean, inds[1])

print("\nArray after replacing NaN with column average:")
print(arr)
