import numpy as np
import pandas as pd
from numpy.random import randn

# Index levels

outside = ['G1', 'G1', 'G1', 'G2','G2', 'G2']
inside = [1,2,3,1,2,3]

# Creates a list of tuples
hier_index = list(zip(outside,inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)

# Multi level index
df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
print(df)

# Gets sub data frame
df.loc['G1']

# To get specific values keep indexing
df.loc['G1'].loc[1]


val_get = (df.loc['G2'].loc[2].loc['B'])

# Gets section G1
df.xs('G1')

# Get cross section for both groups
df.xs(1,level='Num')


