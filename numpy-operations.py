import numpy as np
arr = np.arange(0,10)

# Adds index together
# Ex add[0] + arr[0] and arr[1] + arr[1]
arr_additions = arr + arr

# Multiplies indexes together
arr_multi = arr * arr

# Divides
# If divide by zero, it replaces w/ nan
# If divide by 0 by 1, replaces it w/ inf
arr_div = arr/arr

# Other arr operations
arr_pow = arr ** 3
arr_addnum = arr + 100

# Square root every element or e^of ever element
# There are many more
np.sqrt(arr)
np.exp(arr)