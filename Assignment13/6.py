""" 6) Solve the following equation using linalg() and inverse Matrix method x - 2y + 3z = 9 -x + 3y - z = -6 2x - 5y + 5z = 17 7) Using "Customizing Matplotlib Visualizations" discussed in Numpy session4 notes plot graph to compare your at least 2 semester result"""


import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])


B = np.array([9, -6, 17])

X = np.linalg.solve(A, B)

print("Solution using linalg.solve():")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])

A_inv = np.linalg.inv(A)
X_inv = np.dot(A_inv, B)

print("\nSolution using Inverse Matrix Method:")
print("x =", X_inv[0])
print("y =", X_inv[1])
print("z =", X_inv[2])
