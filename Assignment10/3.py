"""3) Replace NaN values with average of columns 4) Replace negative value with zero in numpy array using replace"""

import numpy as np

arr = np.array([[1, -2, np.nan],
                [4, np.nan, -6],
                [-7, 8, 9]])

print("Original Array:")
print(arr)

arr = np.where(arr < 0, 0, arr)

print("\nAfter replacing negative values with 0:")
print(arr)

col_mean = np.nanmean(arr, axis=0)

inds = np.where(np.isnan(arr))

arr[inds] = np.take(col_mean, inds[1])

print("\nAfter replacing NaN values with column averages:")
print(arr)
