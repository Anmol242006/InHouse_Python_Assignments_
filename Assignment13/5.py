"""5) Study the following program import numpy as np # create a numpy 1d-arrays arr1 = np.array([3, 4]) arr2 = np.array([1, 0]) # find average of NumPy arrays avg = (arr1 + arr2) / 2 print("Average of NumPy arrays:\n", avg) -> Calculate average mean median mode values of two NumPy 2d-arrays """

import numpy as np
from scipy import stats

arr1 = np.array([[10, 20, 30],
                 [40, 50, 60]])

arr2 = np.array([[5, 15, 25],
                 [35, 45, 55]])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

avg = (arr1 + arr2) / 2
print("\nAverage of Two Arrays:")
print(avg)

mean1 = np.mean(arr1)
mean2 = np.mean(arr2)

print("\nMean of Array 1:", mean1)
print("Mean of Array 2:", mean2)

median1 = np.median(arr1)
median2 = np.median(arr2)

print("\nMedian of Array 1:", median1)
print("Median of Array 2:", median2)

mode1 = stats.mode(arr1, axis=None, keepdims=False)
mode2 = stats.mode(arr2, axis=None, keepdims=False)

print("\nMode of Array 1:", mode1.mode)
print("Mode of Array 2:", mode2.mode)
