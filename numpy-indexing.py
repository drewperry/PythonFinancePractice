import numpy as np

arr = np.arange(0, 11)

# BROADCASTING
# differs from regular arrays
# np arrays can set certain elements to something
arr[0:5] = 100

arr = np.arange(0, 11)

# Slice_of_arr is actually a pointer
# Now elements 0-5 of arr are set to 99
slice_of_arr = arr[0:5]
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)

# To avoid changing the original do
arr_copy = arr.copy()
arr_copy[:] = 99

# mat[row, col]
# mat[row][col]

mat = np.array([5, 10, 15], [20, 25, 30]);
first_row = mat[0]
mid_index = mat[1][1]  # Gets middle array
mid_index = mat[1, 1]  # Also gets middle array

# 2D array slicing
# Until second row, starting from second column
mat[:2, 1:]

# CONDITIONAL SELECTION
arr = np.arange(1,11)

# Returns booleans of each index greater than 4
bool_arr = arr > 4

# Only returns arr of values > 4
great_four = arr[bool_arr]

# QUICKER STEP
easier_bool = arr[arr > 4]

another_bool = arr[arr % 2 > 1];
