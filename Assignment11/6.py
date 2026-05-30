# 6) Study the following program import numpy as np # create a numpy 1d-arrays
# arr1 = np.array([3, 4]) arr2 = np.array([1, 0]) # find average of NumPy arrays
# avg = (arr1 + arr2) / 2 print("Average of NumPy arrays:\n", avg) ->
# Calculate average mean median mode values of two NumPy 2d-arrays
import pandas as pd
import numpy as np
a9 = np.array(
    [[31, 22, 44, 94, 25], [27, 99, 62, 13, 54], [51, 63, 15, 47, 18]])
a10 = np.array(
    [[30, 92, 38, 94, 25], [27, 45, 37, 80, 36], [60, 63, 64, 47, 80]])

print(f"Array 1: {a9}")
print("___________________________")
print(f"Array 1: {a10}")
print("___________________________")
a11 = np.concatenate((a9.flatten(), a10.flatten()))
print(f"Combined Array: {a11}")
a12 = np.sort(a11)
print(f"Combined & Sorted Array: {a12}")
mean = np.mean(a11)
median = np.median(a11)
values, counts = np.unique(a11, return_counts=True)
mode = values[np.argmax(counts)]

print("Mean:", mean.round(2))
print("Median:", median)
print("Mode:", mode)
