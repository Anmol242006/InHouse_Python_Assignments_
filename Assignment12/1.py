"""1) Create numpy array and perform following operation > Convert 1D array to 2D > Print Array Attributes(Like shape, dimenssion, data type, itemsize) > Create a 3×3 NumPy array of all 9 > Create a 1D array of 10 evenly spaced values between 25 and 125 > Convert a Python list into a NumPy array > Reverse a 1D NumPy array > Create a 4×4×3 array and extract value at its second set, first row and last column > Create a 4×4 and Extract Odd Rows and Even Columns > Slice the first two rows and first two columns of econd set from a 4×4×3 array > Replace all odd numbers in a NumPy array with -1 by itterating using for loop [[23, 56, 78, 93], [71, 82,13, 24]] > Get the indices of non-zero elements in an array [1, 0, 2, 0, 3, 0, 4] > Perform arithmetic operations on two NumPy arrays element-wise Add two NumPy arrays element by element. Multiply two NumPy arrays element by element. > Write a code to compute the dot product of two NumPy arrays arr1 = [15, 20, 25] arr2 = [10,40,37]"""


import numpy as np


arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = arr1d.reshape(2, 3)
print("1D to 2D Array:\n", arr2d)


print("\nArray Attributes:")
print("Shape:", arr2d.shape)
print("Dimension:", arr2d.ndim)
print("Data Type:", arr2d.dtype)
print("Item Size:", arr2d.itemsize)


arr9 = np.full((3, 3), 9)
print("\n3x3 Array of 9:")
print(arr9)

arr_lin = np.linspace(25, 125, 10)
print("\nEvenly Spaced Values:")
print(arr_lin)


lst = [10, 20, 30, 40, 50]
np_arr = np.array(lst)
print("\nList to NumPy Array:")
print(np_arr)

arr = np.array([1, 2, 3, 4, 5])
rev_arr = arr[::-1]
print("\nReversed Array:")
print(rev_arr)


arr3d = np.arange(48).reshape(4, 4, 3)
print("\n4x4x3 Array:")
print(arr3d)


value = arr3d[1, 0, 2]
print("\nSecond Set, First Row, Last Column:")
print(value)


arr4 = np.arange(1, 17).reshape(4, 4)
print("\n4x4 Array:")
print(arr4)

odd_rows_even_cols = arr4[::2, 1::2]
print("\nOdd Rows and Even Columns:")
print(odd_rows_even_cols)

slice_arr = arr3d[1, :2, :2]
print("\nFirst Two Rows and First Two Columns of Second Set:")
print(slice_arr)

arr_replace = np.array([[23, 56, 78, 93],
                        [71, 82, 13, 24]])

for i in range(arr_replace.shape[0]):
    for j in range(arr_replace.shape[1]):
        if arr_replace[i][j] % 2 != 0:
            arr_replace[i][j] = -1

print("\nAfter Replacing Odd Numbers with -1:")
print(arr_replace)

arr_nonzero = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(arr_nonzero)
print("\nIndices of Non-Zero Elements:")
print(indices)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:")
print(a + b)

print("\nMultiplication:")
print(a * b)

arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])

dot_product = np.dot(arr1, arr2)

print("\nDot Product:")
print(dot_product)
