"""4) Replace negative value with zero in numpy array using replace"""

import numpy as np

# Create NumPy array
arr = np.array([[10, -5, 20],
                [-8, 30, -2],
                [15, -12, 25]])

print("Original Array:")
print(arr)

arr[arr < 0] = 0

print("\nArray after replacing negative values with 0:")
print(arr)
