"""
2) Move axes of 3D array to new positions 
"""

import numpy as np

arr = np.array([[[1, 2],
                 [3, 4]],

                [[5, 6],
                 [7, 8]]])

print("Original Array Shape:", arr.shape)
print(arr)

new_arr = np.moveaxis(arr, 0, 2)

print("\nArray After Moving Axes:")
print("New Shape:", new_arr.shape)
print(new_arr)
