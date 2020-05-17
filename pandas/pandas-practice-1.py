import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 100}

# Series with labels
series = pd.Series(my_list)
series = pd.Series(my_list, index=labels)

series2 = pd.Series(arr, index=labels)
print(series2)

# Series using dictionary
series3 = pd.Series(d)
print(series3)

# Series using labels as data
series4 = pd.Series(data=labels)

# Series with built in functions
series5 = pd.Series([sum, print, len])
print(series5)

series6 = pd.Series([1, 2, 3, 4], index=['USA', 'CHINA', 'FRANCE', 'GERMANY'])
print(series6)

# Get value at index
usa_value = series6['USA']

# Can add series where the index matches, if no match replaces with NaN
series7 = pd.Series([1, 2, 3, 4], index=['ITALY', 'CHINA', 'FRANCE', 'GERMANY'])
add_series = series6 + series7
print(add_series)


