import numpy as np

# Creating Numpy array

my_list = [1, 2, 3]
x = np.array(my_list)

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array1 = (np.array(my_matrix))

# Quick making of arrays using np
# start, end, step size
odd_array = (np.arange(0, 10, 2))

# Quick array of zeros
quick_array = (np.zeros(3))

# Quick 2D array
# Pass in tuple
quick2d_array = np.zeros((3, 5))

# Quick array of ones
quick_ones = np.ones((3, 3))

# Evenly spaces number across the interval
# Start, stop, how many numbers
even_spaced = np.linspace(0, 10, 3)

# Identity matrix: Square matrix, diagonal is one
identity_matrix = np.eye(4)

# Random values in a given shape (matrix), uniform distribution
# Creates 5 by 5 matrix
rand_nums = np.random.rand(5, 5)

# Random values from a standard distribution
std_nums = np.random.randn(5, 5)

# Random int
# Start, end, number of numbers
np.random.randint(1, 100, 10)

arr = np.arange(25)
ran_arr = np.random.randint(0, 50, 10)

# Reshapes into 2D array, needs to multiply to size
reshaped = arr.reshape(5, 5)
shape = arr.shape  # Shape of (25,)
shape2 = reshaped.shape  # Shape of (5,5)
type = arr.dtype # says the type in array

# Finds max num in array and its index
max_num = arr.max()
max_num_index = arr.argmax()

# Finds min num in an array and its index
min_num = arr.min()
min_num_index = arr.argmin()
