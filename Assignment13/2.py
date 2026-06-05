"""2) Move axes of 3D array to new positions"""

import numpy as np

arr = np.arange(24).reshape(2, 3, 4)

print("Original Array Shape:")
print(arr.shape)

new_arr = np.moveaxis(arr, 0, 2)

print("\nNew Array Shape:")
print(new_arr.shape)

print("\nNew Array:")
print(new_arr)
