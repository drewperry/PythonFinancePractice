import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

# DataFrame (data, row label, column label)
# A bunch of series objects that share an index
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# W column is just a series with row labels
series_w = df['W']

# returns multiple columns
series_wz = df[['W', 'Z']]

# adding a new column
df['new'] = df['W'] + df['Y']
print(df)

# To drop a column, not inplace unless said
# columns are axis 1
df.drop('new', axis=1, inplace=True)
print(df)

# To drop a row, rows are 0 axis
df.drop('E', inplace=True)


# selecting rows, also series
print(df.loc['A'])

# Two ways of selecting rows
df.loc['C']
df.iloc[2]

# Find value at row, column
df.loc['B', 'Y']

# Returns A,W B,W and A,Y B,Y
df.loc[['A', 'B'], ['W','Y']]

booldf = df > 0
df[booldf]

df[df > 0]

# Won't get NaN
resultdf = df[df['W']>0]
resultdf['X']

result = df[df['W']>0]['X']


# Multiple conditions for series
# Must use & and not 'and'
print(df.reset_index())

# Easy way to create a list
newind = 'CA NY WY OR'.split()

# makes new column states
df['States'] = newind

# Sets new index as states
print(df.set_index('States'))


