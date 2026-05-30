# 2) Flatten a 2d numpy array into 1d array

import pandas as pd
import numpy as np
arr2 = np.array([
    [23, 54, 5, 32],
    [99, 1, 23, 77]
])
print(arr2.reshape(8,))
